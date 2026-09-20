"""Integration tests against the REAL database (DATABASE_* settings).

Opt-in only: nothing here runs unless RUN_DB_TESTS=1, so a plain `pytest`
never touches the real database. No create_all/drop_all - tests must only
create rows with the unique `test_prefix` and the fixture deletes just those.
"""
import os

# Must come before database_config is imported (it loads env_vars.env), so the
# other integration tests keep their known admin code.
os.environ.setdefault("FIRE_ALARM_ADMIN_CODE", "test-admin-code")

import uuid

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import delete
from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from database import database_config
from districts.model import District
import main as main_module


@pytest.fixture(autouse=True)
def require_opt_in():
    if os.getenv("RUN_DB_TESTS") != "1":
        pytest.skip("real-database tests are opt-in: set RUN_DB_TESTS=1")


@pytest_asyncio.fixture
async def session_factory():
    # NullPool: every test runs on its own event loop, so pooled connections
    # from a previous loop must not be reused.
    engine = create_async_engine(
        URL.create(
            "mysql+aiomysql",
            username=database_config.DB_USER,
            password=database_config.DB_PASSWORD,
            host=database_config.DB_HOST,
            port=int(database_config.DB_PORT),
            database=database_config.DB_NAME,
        ),
        poolclass=NullPool,
    )
    yield sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
    await engine.dispose()


@pytest_asyncio.fixture
async def test_prefix(session_factory):
    """Unique name prefix for rows this test creates; they are deleted afterwards."""
    prefix = f"pytest-{uuid.uuid4().hex[:8]}-"
    yield prefix
    async with session_factory() as session:
        await session.execute(delete(District).where(District.district_name.like(f"{prefix}%")))
        await session.commit()


@pytest_asyncio.fixture
async def client(session_factory):
    async def _get_session():
        async with session_factory() as session:
            yield session

    main_module.app.dependency_overrides[database_config.get_async_db_session] = _get_session
    transport = ASGITransport(app=main_module.app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    main_module.app.dependency_overrides.clear()

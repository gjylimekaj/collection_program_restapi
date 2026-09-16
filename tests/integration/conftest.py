import os

os.environ.setdefault("FIRE_ALARM_ADMIN_CODE", "test-admin-code")

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import database_config
from database.base import Base
import main as main_module

test_engine = create_async_engine(
    "sqlite+aiosqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestAsyncSession = sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def db_session(database):
    async with TestAsyncSession() as session:
        yield session


@pytest_asyncio.fixture
async def client(database):
    async def _override_get_async_db_session():
        async with TestAsyncSession() as session:
            yield session

    main_module.app.dependency_overrides[database_config.get_async_db_session] = _override_get_async_db_session
    transport = ASGITransport(app=main_module.app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
    main_module.app.dependency_overrides.clear()

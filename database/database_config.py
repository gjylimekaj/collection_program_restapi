import traceback
import os
from pathlib import Path
from dotenv import load_dotenv

import redis
import redis.asyncio as aioredis

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from database.base import Base

# Every model must be imported here so all of them are registered on Base's
# mapper registry before any relationship() string (e.g. "ApartmentBuilding")
# gets resolved - otherwise whichever model wasn't imported yet raises a
# clsregistry KeyError the first time a query touches its relationship.
from apartments.model import Apartment, ApartmentBuilding  # noqa: E402,F401
from districts.model import District  # noqa: E402,F401
from humans.model import Human  # noqa: E402,F401


# ---------------------------
# ENV LOADING (SAFE)
# ---------------------------

ENV = os.getenv("ENVIRONMENT", "local")

ENV_FILE = Path(__file__).resolve().parent.parent / "env_vars.env"

if ENV != "production" and ENV_FILE.exists():
    load_dotenv(ENV_FILE)


# ---------------------------
# SAFE ENV ACCESS
# ---------------------------

# ──────────────────────────────────────────────
# Henter en miljøvariabel, med støtte for default-verdi og påkrevd-sjekk
# ──────────────────────────────────────────────
def get_env(key: str, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        raise RuntimeError(f"Missing required env var: {key}")
    return value


DB_NAME = get_env("DATABASE_NAME", "").replace("'", "")
DB_USER = get_env("DATABASE_USER", "").replace("'", "")
DB_PASSWORD = get_env("DATABASE_USER_PASSWORD", "").replace("'", "")
DB_HOST = get_env("DATABASE_HOST", "").replace("'", "")
DB_PORT = get_env("DATABASE_PORT", "").replace("'", "")


# ---------------------------
# DATABASE
# ---------------------------
DATABASE_URL = (f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

async_session = sessionmaker(
    bind=create_async_engine(
        f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        echo=False,
    ),
    class_=AsyncSession,
    expire_on_commit=False,
)


# ---------------------------
# DATABASE SESSIONS
# ---------------------------

# ──────────────────────────────────────────────
# Åpner en async databasesesjon og yielder den til FastAPI sin dependency-injection
# ──────────────────────────────────────────────
async def get_async_db_session() -> AsyncSession:
    async with async_session() as session:
        yield session


# ──────────────────────────────────────────────
# Henter en synkron databasesesjon og lukker den automatisk etter bruk
# ──────────────────────────────────────────────
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------
# REDIS (SAFE)
# ---------------------------

# ──────────────────────────────────────────────
# Bygger konfigurasjonen (host/port/db-nummer) som brukes til å koble til Redis
# ──────────────────────────────────────────────
def get_redis_config():
    return {
        "HOST": get_env("REDIS_HOST", get_env("DATABASE_HOST")),
        "PORT": get_env("REDIS_PORT", 6379),
        "DBNUM": get_env("REDIS_DB", 0),
    }


# ──────────────────────────────────────────────
# Oppretter en async Redis-tilkobling og yielder den, lukker tilkoblingen når den er ferdig brukt
# ──────────────────────────────────────────────
async def get_redis_async_connection():
    conn = None
    try:
        cfg = get_redis_config()

        conn = await aioredis.from_url(
            f"redis://{cfg['HOST']}:{cfg['PORT']}/{cfg['DBNUM']}"
        )
        yield conn

    except aioredis.RedisError:
        print(traceback.format_exc())

    finally:
        if conn:
            await conn.close()


# ──────────────────────────────────────────────
# Oppretter en synkron Redis-tilkobling og yielder den, lukker tilkoblingen når den er ferdig brukt
# ──────────────────────────────────────────────
def get_redis_connection():
    conn = None
    try:
        cfg = get_redis_config()

        conn = redis.Redis(
            host=cfg["HOST"],
            port=cfg["PORT"],
            db=cfg["DBNUM"]
        )
        yield conn

    except redis.RedisError:
        print(traceback.format_exc())

    finally:
        if conn:
            conn.close()
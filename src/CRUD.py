from sqlalchemy import String, create_engine, text, insert, create_async_engine, Table, Column, Integer, String, MetaData, ForeignKey
from config import settings
from models import metadata_obj, workers_table
import asyncio


metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)


# Тест PostgreSQL

# синхронный
with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(res.all())

# асинхронный


async def test_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


asyncio.run(test_async())


# CREATE TABLE


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

# ADD DATA

# by sql


def insert_data_sql():
    with sync_engine.connect() as conn:
        stmt = """INSERT into workers (username) VALUES
        ('Bobr'),
        ('Bobr2')
        """

        conn.commit()

# by orm


def insert_data_orm():
    with sync_engine.connect() as conn:
        # stmt = """INSERT into workers (username) VALUES
        # ('Bobr'),
        # ('Bobr2')
        # """
        # stmt = workers_table.insert().values(username='XXXX')
        # stmt = insert(workers_table).values(username='XXXX')
        stmt = insert(workers_table).values(
            [
                {"username": 'XXXX1'},
                {"username": 'XXXX2'}
            ]
        )
        conn.execute(stmt)
        conn.commit()

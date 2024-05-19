from sqlalchemy import Integer, and_, func, insert, select, text, update
from sqlalchemy.orm import aliased

from database import async_engine, sync_engine
from models import metadata_obj, workers_table


def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


def insert_data():
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

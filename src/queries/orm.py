from database import sync_engine, session_factory, async_session_factory
from models import metadata_obj, WorkerORM


def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True


# def insert_data():
#     with session_factory() as session:
#         worker_1 = WorkerORM(username="worker_1")
#         worker_2 = WorkerORM(username="worker_2")     
#         # session.add(worker_1)
#         session.add_all([worker_1, worker_2])
#         session.commit()


async def insert_data():
    async with async_session_factory() as session:
        worker_1 = WorkerORM(username="worker_3")
        worker_2 = WorkerORM(username="worker_4")     
        # session.add(worker_1)
        session.add_all([worker_1, worker_2])
        await session.commit()
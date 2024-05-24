from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from database import sync_engine, session_factory, async_session_factory, Base
from models import ResumesORM, WorkersORM, Workload


class SyncORM:
    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers():
        with session_factory() as session:
            worker_jack = WorkersORM(username="Jack")
            worker_michael = WorkersORM(username="Michael")
            session.add_all([worker_jack, worker_michael])
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def select_workers():
        with session_factory() as session:
            query = select(WorkersORM)
            result = session.execute(query)
            workers = result.all()
            print(f"{workers=}")

    @staticmethod
    def update_worker(worker_id: int = 2, new_username: str = "Misha"):
        with session_factory() as session:
            worker_michael = session.get(WorkersORM, worker_id)
            worker_michael.username = new_username
            session.refresh(worker_michael)
            session.commit()
            # refresh нужен, если мы хотим заново подгрузить данные модели из базы.
            # Подходит, если мы давно получили модель и в это время
            # данные в базе д

    @staticmethod
    def insert_resumes():
        with session_factory() as session:
            resume_jack_1 = ResumesORM(
                title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, worker_id=1)
            resume_jack_2 = ResumesORM(
                title="Python Разработчик", compensation=150000, workload=Workload.fulltime, worker_id=1)
            resume_michael_1 = ResumesORM(
                title="Python Data Engineer", compensation=250000, workload=Workload.parttime, worker_id=2)
            resume_michael_2 = ResumesORM(
                title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
            session.add_all([resume_jack_1, resume_jack_2, 
                             resume_michael_1, resume_michael_2])
            session.commit()


# def create_tables():
    
#     Base.metadata.drop_all(sync_engine)
#     sync_engine.echo = True    
#     Base.metadata.create_all(sync_engine)
    
#     # metadata_obj.drop_all(sync_engine)
#     # metadata_obj.create_all(sync_engine)
   


# # def insert_data():
# #     with session_factory() as session:
# #         worker_1 = WorkerORM(username="worker_1")
# #         worker_2 = WorkerORM(username="worker_2")     
# #         # session.add(worker_1)
# #         session.add_all([worker_1, worker_2])
# #         session.commit()


# async def insert_data():
#     async with async_session_factory() as session:
#         worker_1 = WorkerORM(username="worker_3")
#         worker_2 = WorkerORM(username="worker_4")     
#         # session.add(worker_1)
#         session.add_all([worker_1, worker_2])
#         await session.commit()
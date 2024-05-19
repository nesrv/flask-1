from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


# декларативный подход (+ ORM)

class WorkerORM(Base):
    __tablename__ = "workers"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    

# императивный подход
metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
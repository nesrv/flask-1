import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, str_256
import enum
from typing import Optional, Annotated


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(
    server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text(
    "TIMEZONE('utc', now())"), onupdate=text("TIMEZONE('utc', now())"))]
# свой собственный кастомный тип

# декларативный подход (+ ORM)


class WorkersORM(Base):
    __tablename__ = "workers"

    id: Mapped[intpk]
    username: Mapped[str]

    resumes: Mapped[list["ResumesORM"]] = relationship(
        back_populates="worker",
    )

    resumes_parttime: Mapped[list["ResumesORM"]] = relationship(
        back_populates="worker",
        primaryjoin="and_(WorkersORM.id == ResumesORM.worker_id, ResumesORM.workload == 'parttime')",
        order_by="ResumesORM.id.desc()",
    )


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class ResumesORM(Base):
    __tablename__ = "resumes"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[Optional[int]]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    worker: Mapped["WorkersORM"] = relationship(
        back_populates="resumes",
    )

    # vacancies_replied: Mapped[list["VacanciesOrm"]] = relationship(
    #     back_populates="resumes_replied",
    #     secondary="vacancies_replies",
    # )

    repr_cols_num = 2
    repr_cols = ("created_at", )

    # __table_args__ = (
    #     Index("title_index", "title"),
    #     CheckConstraint("compensation > 0", name="checl_compensation_positive"),
    # )


# императивный подход
metadata_obj = MetaData()

workers_table = Table(
    "workers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)

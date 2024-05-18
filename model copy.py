import psycopg2
 
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String

postgres_database = "postgresql://postgres:aatpotug_22@localhost/database"

engine = create_engine(postgres_database)

 

class Base(DeclarativeBase): pass
  
class Person(Base):
    __tablename__ = "people"
  
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)
 
Base.metadata.create_all(bind=engine)

# conn = psycopg2.connect(dbname="metanit", user="postgres", password="aatpotug_22", host="127.0.0.1")
# cursor = conn.cursor()
 
# # создаем таблицу people
# cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
# # поддверждаем транзакцию
# conn.commit()
# print("Таблица people успешно создана")
 
# cursor.close()
# conn.close()

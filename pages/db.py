from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# подключение
DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost:5432/shopdb'

# создаем подключение к бд
engine = create_engine(DATABASE_URL)

# создаем базовый класс для всех моделей
Base = declarative_base()

# создаем сессию для взаимодействия с бд
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

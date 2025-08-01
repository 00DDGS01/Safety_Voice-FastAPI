from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Spring과 동일한 DB
DATABASE_URL = "mysql+pymysql://root:youngh29ktj!@localhost:3306/safety_voice"

# SQLAlchemy ORM
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
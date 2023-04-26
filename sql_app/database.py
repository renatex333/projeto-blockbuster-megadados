from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv(override=True)

SQLALCHEMY_DATABASE_URL = URL.create(
    "mysql",
    username=os.getenv('MD_DB_USERNAME'),
    password=os.getenv('MD_DB_PASSWORD'),
    host=os.getenv('MD_DB_SERVER'),
    port=3306,
    database='blockbuster',
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
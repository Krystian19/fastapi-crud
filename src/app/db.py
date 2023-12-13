from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData)
from datetime import datetime as dt
from databases import Database

DATABASE_URL = 'sqlite:///example.db'

engine = create_engine(DATABASE_URL, echo=True)
database = Database(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(50)),
    Column("username", String(50)),
    Column("created_at", String(50), default=dt.now().strftime("%Y-%m-%d %H:%M"))
)

metadata.create_all(engine)

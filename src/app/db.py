from sqlalchemy import (Column, Integer, String, Table, create_engine, MetaData)
from datetime import datetime as dt
from databases import Database

engine = create_engine('sqlite:///example.db', echo=True)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(50)),
    Column("username", String(50)),
    Column("created_at", String(50), default=dt.now().strftime("%Y-%m-%d %H:%M"))
)

database = Database()

from sqlalchemy import inspect
from database import Base, engine
from model import User, Post

inspector = inspect(engine)

if "users" in inspector.get_table_names() and "posts" in inspector.get_table_names():
    print("Tables already exist")
else:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# db_url = "sqlite:///database.db"
db_url = "postgresql://postgres:pgadmin@127.0.0.1:5432/my_pgdb"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    
Base.metadata.create_all(engine)


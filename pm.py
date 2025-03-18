from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL" , "mysql+pymysql://root:Murli@123@localhost:3306/broker_db" )

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()  


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)  
    username = Column(String, unique=True, nullable=False)  
    password = Column(String, nullable=False)


class MarketData(Base):
    __tablename__ = "market_data"
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, unique=True, nullable=False)  
    price = Column(Float, nullable=False)  


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  
    symbol = Column(String, nullable=False)  
    order_type = Column(String, nullable=False)  
    quantity = Column(Integer, nullable=False)  
    price = Column(Float, nullable=False)  

    
    user = relationship("User")


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Broker API is running with MySQL!"}


@app.post("/users/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    new_user = User(username=username, password=password)  
    db.add(new_user)  
    db.commit()  
    db.refresh(new_user)  
    return {"id": new_user.id, "username": new_user.username}


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()

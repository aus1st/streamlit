
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine,select
from fastapi import FastAPI

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    secret_name: str
    age: Optional[int] = None

hero1 = Hero(name="Ali", secret_name="Ali Ahmed")
hero2 = Hero(name="Kazim", secret_name="Khubsurat")
hero3 = Hero(name="Faiz", secret_name="Party")

engine = create_engine("postgresql://aus1st:Me1K5NJWijTr@ep-dark-scene-148946-pooler.us-east-2.aws.neon.tech/university_gpt?sslmode=require")

def create_db_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_tables()


@app.post('/heroes/')
def create_heroes(hero: Hero):
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)
        return hero
    
@app.get('/heroes/')
def get_heroes():
    with Session(engine) as session:
        heroes = session.exec(select(Hero)).all()
        return heroes   
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel


from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine,select
from fastapi import FastAPI

class Location(SQLModel, table=True):
    name: str =  Field(index=True, primary_key=True)
    location: str

app = FastAPI(title="Location API",
               version="0.0.1",
               servers=[
                   
                   {
                       "url": "http://127.0.0.1:8000",
                       "description":"Development Location API"
                   },
                   {
                       "url": "https://precise-bunny-immune.ngrok-free.app",
                       "description":"Production Lcation API"
                   },
               ])

locations= {
    "aliza": Location(name="aliza", location="Karachi"),
    "zimal": Location(name="zimal", location="UK")
}

engine = create_engine("postgresql://aus1st:Me1K5NJWijTr@ep-dark-scene-148946-pooler.us-east-2.aws.neon.tech/university_gpt?sslmode=require")

def create_db_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_tables()
def get_location_or_404(name:str)-> Location:
    with Session(engine) as session:
        stmt = select(Location).where(Location.name == name)
        loc =  session.exec(stmt)
        if not loc:
            raise HTTPException(status_code=404, detail=f"No location found for {name}")
        return loc
@app.get('/persons/')
def get_all_persons_location():
    with Session(engine) as session:
        return session.exec(select(Location)).all()

@app.get("/location/{name}")
def get_person_location(name:str, location: Annotated[Location, Depends(get_location_or_404)]):
    return location


@app.post('/person/')
def create_location(location: Location):
    with Session(engine) as session:
        session.add(location)
        session.commit()
        session.refresh(location)
        return location
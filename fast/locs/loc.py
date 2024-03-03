from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel

class Location(BaseModel):
    name: str
    location: str

app = FastAPI(title="Location API",
               version="0.0.1",
               servers=[
                   {
                       "url": "https://precise-bunny-immune.ngrok-free.app",
                       "description":"Production API"
                   },
                   {
                       "url": "http://localhost:8000",
                       "description":"Development API"
                   },
               ])
locations= {
    "aliza": Location(name="aliza", location="Karachi"),
    "zimal": Location(name="zimal", location="UK")
}

def get_location_404(name:str)-> Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=404, detail=f"No location found for {name}")
    return loc

@app.get("/location/{name}")
def get_person_location(name:str, location: Annotated[Location, Depends(get_location_404)]):
    return location



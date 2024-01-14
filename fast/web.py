
from fast.model import Creature
from fastapi import FastAPI, Params, Depends

app = FastAPI()

def user_dep(name: str = Params, password: str = Params):
    return {"name": name, "valid": True}

@app.get('/user')
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


@app.get('/creature')
def get_All() -> list[Creature]:
    from data import get_creatures
    return get_creatures()
from altair import Header
from fastapi import Body, FastAPI

app = FastAPI()
# @app.get("/hi")
# def greet():
#     return "Hello World"
@app.get("/hi")
def greet(who):
    return f"Hello {who}"

@app.post('/hi')
def greet(who: str= Body(embed=True)):
    return f"Hello {who}"

@app.post('/head')
def greet_with_head(who: str= Header()):
    return f"Hello {who}"


@app.get("/hi/{name}")
def greet_wit_name(name: str):
    return f'Hello {name.title()}'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
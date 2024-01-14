import asyncio
from fastapi import Body, FastAPI

app = FastAPI()

@app.get('/greet')
async def greet():
    await asyncio.sleep(1)
    return 'Async Hello World'
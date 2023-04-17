import asyncio
from fastapi import FastAPI

app = FastAPI()
cache = dict()


@app.get("/expensive_thing")
async def take_a_long_time() -> int:
    key = tuple()
    if key in cache:
        return cache[key]

    await asyncio.sleep(10)
    value = 3

    cache[key] = value
    return value


# uvicorn redis_example:app --host 0.0.0.0 --port 8000
# localhost:8000/docs

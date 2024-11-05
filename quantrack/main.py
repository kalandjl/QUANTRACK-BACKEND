from fastapi import Depends, FastAPI

# from quantrack.config import settings

import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
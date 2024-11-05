# to run the server: uvicorn quantrack.main:app --reload
# or python -m quantrack.main (to run without auto-reload)

from fastapi import Depends, FastAPI

# from quantrack.config import settings

import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
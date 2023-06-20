from fastapi import FastAPI

from .routes import v1

app = FastAPI(title="DAM API : California housing")

app.include_router(v1.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Hello from Data Analytics Meeting!"}

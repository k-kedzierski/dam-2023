from fastapi import FastAPI

app = FastAPI(title="DAM API : California housing")


@app.get("/")
async def root():
    return {"message": "Hello from Data Analytics Meeting!"}

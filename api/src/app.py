from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .exceptions import ModelNotFound

from .routes import v1

app = FastAPI(title="DAM API : California housing")

app.include_router(v1.router, prefix="/api/v1")

@app.exception_handler(ModelNotFound)
async def model_not_found_error(request: Request, ex: ModelNotFound):
    return JSONResponse(status_code=503, content={"message": str(ex)})


@app.get("/")
async def root():
    return {"message": "Hello from Data Analytics Meeting!"}

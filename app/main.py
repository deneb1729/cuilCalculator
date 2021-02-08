from fastapi import FastAPI, Request

from .routers import cuils

app = FastAPI(
    title="Argentina API",
    description="This is a little cuil generator api",
    version="1.0",
)

app.include_router(cuils.router, prefix="/api")


@app.get(
    "/api/healthcheck",
    tags=["healthcheck"],
    responses={
        200: {
            "description": "Healthcheck api server",
            "content": {
                "application/json": {
                    "example": {"message": "Successful 200 OK", "client": "10.0.0.2"}
                }
            },
        },
    },
)
async def healthcheck(request: Request):
    return {"message": "Successful 200 OK", "client": request.client.host}

from fastapi import FastAPI
from app.routers.events import router

app = FastAPI(title="MC Event API")

app.include_router(router=router)

@app.get("/")
async def healthcheck():
    return {"status": "ok"}
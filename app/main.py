from fastapi import FastAPI

app = FastAPI(title="MC Event API")

@app.get("/")
async def healthcheck():
    return {"status": "ok"}
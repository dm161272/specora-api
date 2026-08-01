from fastapi import FastAPI

from .routes.generate import router as generate_router

app = FastAPI(
    title="Specora",
    version="1.0.0",
    description="AI Powered API Generator"
)

app.include_router(generate_router)


@app.get("/")
async def root():
    return {
        "application": "Specora",
        "status": "Running"
    }
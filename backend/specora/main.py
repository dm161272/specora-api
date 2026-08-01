from fastapi import FastAPI

from .routes.generate import router as generate_router
from .routes.health import router as health_router
from .routes.projects import router as projects_router



app = FastAPI(
    title="Specora",
    version="1.0.0",
    description="AI Powered API Generator"
)


app.include_router(generate_router)
app.include_router(health_router)
app.include_router(projects_router)

@app.get("/")
async def root():
    return {
        "application": "Specora",
        "status": "Running"
    }
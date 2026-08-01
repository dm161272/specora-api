from fastapi import APIRouter

router = APIRouter(
    prefix="/generate",
    tags=["Generate"]
)

@router.post("/")
async def generate():

    return {
        "message": "API Generator is working."
    }
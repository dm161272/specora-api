from fastapi import APIRouter, HTTPException
from pymongo.errors import PyMongoError

from specora.database import db

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)

@router.get("/")
async def health():
    try:
        await db.command("ping")

        return {
            "status": "OK",
            "database": "Connected",
        }

    except PyMongoError as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database connection failed: {str(e)}"
        )
from fastapi import APIRouter

from specora.services.project_service import ProjectService


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/")
async def projects():

    return await ProjectService.list_projects()
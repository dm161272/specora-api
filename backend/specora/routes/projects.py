from fastapi import APIRouter
from specora.schemas.project import ProjectCreate
from specora.services.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
async def create_project(project: ProjectCreate):

    project_id = await ProjectService.create_project(project.model_dump())

    return {
        "id": project_id
    }
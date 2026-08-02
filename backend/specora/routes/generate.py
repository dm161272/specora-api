from fastapi import APIRouter

from specora.schemas.generate import GenerateRequest
from specora.schemas.api_spec import ApiSpecification

from specora.services.gemini import generate_api_spec
from specora.services.project_service import ProjectService

router = APIRouter(
    prefix="/generate",
    tags=["Generate"]
)


@router.post("/")
async def generate(
        request: GenerateRequest
):
    result = await generate_api_spec(
        request.prompt
    )

    specification = ApiSpecification(
        **result
    )

    project_id = await ProjectService.save_project(
        request.prompt,
        specification.model_dump()
    )

    return {
        "project_id": project_id,
        "specification": specification
    }

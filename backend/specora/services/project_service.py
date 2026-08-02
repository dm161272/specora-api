from specora.models.project import project_document
from specora.repositories.project_repository import ProjectRepository


class ProjectService:


    @staticmethod
    async def save_project(
        prompt: str,
        specification: dict
    ):

        document = project_document(
            prompt,
            specification
        )

        return await ProjectRepository.create(
            document
        )


    @staticmethod
    async def list_projects():

        return await ProjectRepository.get_all()
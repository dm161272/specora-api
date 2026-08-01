from specora.database import db


class ProjectService:

    @staticmethod
    async def create_project(project: dict):
        result = await db.projects.insert_one(project)
        return str(result.inserted_id)
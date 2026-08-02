from specora.database import db


class ProjectRepository:

    collection = db.projects


    @staticmethod
    async def create(document: dict):

        result = await ProjectRepository.collection.insert_one(
            document
        )

        return str(result.inserted_id)


    @staticmethod
    async def get_all():

        projects = []

        cursor = ProjectRepository.collection.find()

        async for project in cursor:
            project["_id"] = str(project["_id"])
            projects.append(project)

        return projects
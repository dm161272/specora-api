from datetime import datetime, timezone


def project_document(
    prompt: str,
    specification: dict
):
    return {
        "prompt": prompt,
        "specification": specification,
        "status": "created",
        "created_at": datetime.now(tz=timezone.utc),
    }
from google import genai
from google.genai import types

from specora.config import GEMINI_API_KEY


client = genai.Client(
    api_key=GEMINI_API_KEY
)


API_SPEC_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "name": {
            "type": "STRING"
        },
        "description": {
            "type": "STRING"
        },
        "framework": {
            "type": "STRING"
        },
        "database": {
            "type": "STRING"
        },
        "authentication": {
            "type": "STRING"
        },
        "entities": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "name": {
                        "type": "STRING"
                    },
                    "description": {
                        "type": "STRING"
                    },
                    "fields": {
                        "type": "ARRAY",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "name": {
                                    "type": "STRING"
                                },
                                "type": {
                                    "type": "STRING"
                                },
                                "required": {
                                    "type": "BOOLEAN"
                                }
                            }
                        }
                    }
                }
            }
        },
        "endpoints": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "method": {
                        "type": "STRING"
                    },
                    "path": {
                        "type": "STRING"
                    },
                    "description": {
                        "type": "STRING"
                    },
                    "request_body": {
                        "type": "STRING"
                    },
                    "response": {
                        "type": "STRING"
                    }
                }
            }
        },
        "requirements": {
            "type": "ARRAY",
            "items": {
                "type": "STRING"
            }
        }
    }
}


async def generate_api_spec(prompt: str):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Create a production-ready FastAPI API specification.

Customer request:

{prompt}
""",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=API_SPEC_SCHEMA
        )
    )

    return response.parsed
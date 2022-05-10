from pydantic import BaseModel

class APIResponse(BaseModel):
    title : str
    link: str
    source : str
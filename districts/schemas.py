from pydantic import BaseModel

class DistrictScheme(BaseModel):
    name: str
    post_number: int
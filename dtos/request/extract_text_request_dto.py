from pydantic import BaseModel

class ExtractTextRequestDto(BaseModel):
    text: str

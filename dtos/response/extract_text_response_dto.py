from pydantic import BaseModel

class ExtractTextResponseDto(BaseModel):
    word: str
    label: str

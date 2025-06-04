from fastapi import FastAPI
from dtos.request.extract_text_request_dto import ExtractTextRequestDto
from dtos.response.extract_text_response_dto import ExtractTextResponseDto
import spacy

app = FastAPI()

nlp = spacy.load("xx_ent_wiki_sm")

@app.post("/mlner")
def extract_text(request: ExtractTextRequestDto):
    response = []
    doc = nlp(request.text)
    for ent in doc.ents:
        response.append(ExtractTextResponseDto(word=ent.text, label=ent.label_))

    return response

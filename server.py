from __future__ import annotations

from pydantic import BaseModel
from typing import List, Optional
from fastapi import FastAPI, Request, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# USE THIS
# from src.backend.models.user_form import UserForm

class UserForm(BaseModel):
    course_name: str
    difficulty: str
    school_level: str
    subject: str
    subject_material: List[UploadFile]
    num_flash_cards: int | None = None

'''
class FlashCard(BaseModel):
    question: str
    answer: str
'''

class FlashCards(BaseModel):
    #flashCards: List[FlashCard]
    file_name: str


app = FastAPI()

templates = Jinja2Templates(directory="/src/frontend/templates")
@app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
def get_form(request: Request):
    return templates.TemplateResponse(request=request, name="form.html")

@app.post("/build")
def make_cards(reque)

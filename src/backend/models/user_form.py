from pydantic import BaseModel
from typing import List, Optional
from fastapi import UploadFile

class UserForm(BaseModel):
    course_name: str
    difficulty: str
    school_level: str
    subject: str
    subject_material: List[UploadFile]
    num_flash_cards: int | None = None
    

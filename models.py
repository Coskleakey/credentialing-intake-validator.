from pydantic import BaseModel
from typing import Literal
from datetime import date

class FullDeaCertificate(BaseModel):
    dea_number: str
    registrant_name: str
    business_activity: Literal["PRACTITIONER", "MID-LEVEL PRACTITIONER"]
    expiration_date: date

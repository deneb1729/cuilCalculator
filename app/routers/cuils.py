from typing import List
from pydantic import BaseModel, Field, validator
from fastapi import APIRouter, Request


from ..utils.cuil_generator import generator
from ..dependencies import ModelGener

router = APIRouter()


class BaseCuil(BaseModel):
    dni_number: int = Field(..., title="identification number")
    gener: ModelGener = Field(..., title="person gener")

    @validator("dni_number")
    def len_validator(cls, v):
        len_value = len(str(v))

        if not (len_value >= 7 and len_value <= 8):
            raise ValueError("dni_number must have between 7 and 8 digits")
        return v


class ModelCuilOut(BaseCuil):
    cuil: int = Field(..., title="cuil/cuit number")


@router.post("/cuils/", tags=["cuils"])
async def unique_cuil(entry: BaseCuil, request: Request):
    cuil = generator(entry.dni_number, entry.gener.value)
    data = ModelCuilOut(**entry.dict(), cuil=cuil)
    return {"message": "unique cuil", "data": data}


@router.post("/cuils/batch", tags=["cuils"])
async def cuil_list(entry: List[BaseCuil], request: Request):
    batch_data = []
    for e in entry:
        batch_data.append(ModelCuilOut(**e.dict(), cuil=generator(e.dni_number, e.gener.value)))

    return {"message": "cuils list", "data": batch_data}

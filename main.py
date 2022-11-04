from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="HNGi9 TAsk 2 API",
    description="An api endoint that returns a json response for Hng internship",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


class params(BaseModel):
    operation_type: str
    x: int
    y: int


@app.post("/")
def calc(params: params):
    result = None

    if params.operation_type.lower() == 'addition':
        result = params.x + params.y
    elif params.operation_type.lower() == 'subtraction':
        result = params.x - params.y
    elif params.operation_type.lower() == 'multiplication':
        result = params.x * params.y

    answer = {
        "slackUsername": 'Jp',
        "operation_type": params.operation_type,
        "result": result
    }
    return answer

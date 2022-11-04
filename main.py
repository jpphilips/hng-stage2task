from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import nltk

nltk.download('punkt')

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


@ app.get("/home")
def home():
    return {
        "slackUsername": "Jp",
        "backend": True,
        "age": 26,
        "bio": "Life is Uncertain; eat first"
    }


@ app.post("/")
async def calc(params: params):
    result = None
    operation = None

    words = nltk.word_tokenize(params.operation_type)

    if any(operator in words for operator in ['add', 'addition', 'sum', '+', 'combine']):
        operation = 'addition'
        result = params.x + params.y
    elif any(operator in words for operator in ['subtract', 'minus', '-', 'seperate', 'subtraction']):
        operation = 'subtraction'
        result = params.x - params.y
    elif any(operator in words for operator in ['multiply', 'multiplication', '*']):
        operation = 'multiplication'
        result = params.x * params.y
    else:
        raise HTTPException(status_code=404, detail='Operation not found')

    answer = {
        "slackUsername": 'Jp',
        "operation_type": operation,
        "result": result,
    }
    return answer

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel


class RequestBody(BaseModel):
    kek: str


app = FastAPI()

data = {1: "nothing"}


@app.get("/", response_class=HTMLResponse)
def welcome() -> str:
    return "Welcome"


@app.get("/write/{d}", response_class=HTMLResponse)
def write(d: str) -> str:
    data[1] = d
    return "Write successfully"


@app.get("/read", response_class=HTMLResponse)
def read() -> str:
    return f"Your data: {data[1]}"


@app.get("/you", response_class=HTMLResponse)
def you(name: str, surname: str) -> str:
    return f"Hi, {name} {surname}"


@app.post("/with/body", response_class=HTMLResponse)
def with_body(body: RequestBody) -> str:
    return "lol " + body.kek

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def welcome() -> str:
    """Doc."""
    return "Welcome"

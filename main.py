from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI("API de Alunos")

templates = Jinja2Templates(directory="tamplates")

#puxar arquivos css
app.mount("/static", StaticFiles(directory="static"), name="static")

alunos = [
    {"nome": "Felipe", "nota": 8.5},
    {"nome": "Laura", "nota": 5.0}
    ]

@app.get("/", response_class=HTMLResponse)
def exibir_aluno(request: Request):
    return templates.TemplateResponse(
        "alunos.html", {"request": Request, "lista_alunos": alunos}
    )
#pip install fastapi uvicorn jinja2
#jinja2 = auxilia a fazer a conexão entre python e html

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="API de alunos")

#Configurar o diretório dos nossos templates jinja2
templates = Jinja2Templates(directory="templates")

#Pasta static para servir os arquivos (CSS, Imagens ou JS)
app.mount("/static", StaticFiles(directory="static"), name= "static")


alunos = [
    {"nome":"Felipe","nota": 8.5},
    { "nome": "Laura","nota": 9.0},
    {"nome":"Yasmin","nota":8.0}
]


#Rota inicial
@app.get("/", response_class=HTMLResponse)
def exibir_alunos(request: Request):
    return templates.TemplateResponse(
        "Alunos.html", {"request":request, "lista_alunos": alunos}
    )

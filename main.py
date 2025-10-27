#pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

#Rodar o servidor
# python -m uvicorn main:app --reload

app = FastAPI(title="API de Alunos")

#Configura o diretório dos templates jinja2
templates = Jinja2Templates(directory="templates")

#Pasta static para servir os arquivos (CSS, Imagens ou JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

alunos = [
    {"nome": "Felipe", "nota": 8.5},
    {"nome": "Laura", "nota": 9.0},
    {"nome": "Yasmin", "nota": 8.0},
    {"nome": "Vitoria", "nota": 6.0},
    {"nome": "Kazuki", "nota": 5.5}
]

#Rota inicial
@app.get("/", response_class=HTMLResponse)
def exibir_alunos(request: Request):
    return templates.TemplateResponse(
        "alunos.html", {"request": request, "lista_alunos": alunos}
    )

#Rota de cadastro (tela cadastro)
@app.get("/cadastro", response_class=HTMLResponse)
def cadastro_aluno(request: Request):
    return templates.TemplateResponse(
        "cadastro.html", {"request": request}
    )

#Rota de cadastro na lista
@app.post("/cadastro")
def salvar_aluno(nome: str = Form(...), nota: float = Form(...)):
    alunos.append({ "nome": nome, "nota": nota} )
    return RedirectResponse(url="/", status_code=303)


# 🎓 Sistema de Gestão Acadêmica

<div align=\"center\">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

Um sistema moderno e intuitivo para gerenciamento de notas e desempenho acadêmico dos alunos.

[Funcionalidades](#-funcionalidades) • [Tecnologias](#-tecnologias) • [Instalação](#-instalação) • [Uso](#-como-usar) • [API](#-api-endpoints) • [Licença](#-licença)

</div>

---

### Tela Principal - Lista de Alunos
- Visualização completa de todos os alunos cadastrados
- Estatísticas em tempo real (Total, Aprovados, Reprovados, Média Geral)
- Busca dinâmica por nome
- Indicadores visuais de desempenho

### Tela de Cadastro
- Formulário intuitivo para adicionar novos alunos
- Validação de dados em tempo real
- Preview do status baseado na nota inserida

### Tela de Edição
- Atualização rápida dos dados do aluno
- Campos preenchidos automaticamente
- Interface consistente com o restante do sistema

---

## Funcionalidades

### Dashboard Completo
- **Estatísticas em tempo real**: Visualize total de alunos, aprovados, reprovados e média geral
- **Cards informativos**: Design minimalista com dados relevantes
- **Indicadores visuais**: Ícones e cores para fácil identificação

### Gestão de Alunos
- **Cadastrar** novos alunos com nome e nota
- **Editar** informações de alunos existentes
- **Deletar** alunos com confirmação de segurança
- **Listar** todos os alunos em tabela organizada

### Sistema de Avaliação
- **Excelente**: Nota ≥ 9.0 (Roxo)
- **Aprovado**: Nota ≥ 7.0 (Verde)
- **Recuperação**: Nota ≥ 5.0 (Laranja)
- **Reprovado**: Nota < 5.0 (Vermelho)

### Recursos Adicionais
- **Busca em tempo real**: Encontre alunos rapidamente
- **Barra de progresso**: Visualização percentual do desempenho
- **Validação de formulários**: Previne entrada de dados inválidos
- **Design responsivo**: Funciona perfeitamente em qualquer dispositivo
- **Animações suaves**: Experiência de usuário aprimorada

---

## Tecnologias

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido
- **[Jinja2](https://jinja.palletsprojects.com/)** - Engine de templates
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI de alta performance
- **[Python-Multipart](https://andrew-d.github.io/python-multipart/)** - Processamento de formulários

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilização moderna e responsiva
- **JavaScript Vanilla** - Interatividade sem dependências
- **[Font Awesome](https://fontawesome.com/)** - Ícones vetoriais
- **[Google Fonts (Inter)](https://fonts.google.com/)** - Tipografia profissional

### Design
- **Design System**: Minimalista preto e branco
- **Paleta de cores**: 
  - Principal: `#000000` (Preto) e `#FFFFFF` (Branco)
  - Excelente: `#9b59b6` (Roxo)
  - Aprovado: `#2ecc71` (Verde)
  - Recuperação: `#f39c12` (Laranja)
  - Reprovado: `#e74c3c` (Vermelho)
  - Editar: `#3498db` (Azul)

---

## 📁 Estrutura do Projeto

```
sistema-gestao-academica/
│
├── main.py                 # Aplicação principal FastAPI
│
├── templates/              # Templates HTML
│   ├── alunos.html        # Página principal (lista de alunos)
│   ├── cadastro.html      # Formulário de cadastro
│   └── editar.html        # Formulário de edição
│
├── static/                 # Arquivos estáticos
│   └── style.css          # Estilos CSS
│
├── README.md              # Documentação do projeto
└── requirements.txt       # Dependências Python
```

---

## Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/sistema-gestao-academica.git
cd sistema-gestao-academica
```

2. **Crie um ambiente virtual** (recomendado)
```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Instale as dependências**
```bash
pip install fastapi uvicorn jinja2 python-multipart
```

Ou se houver um arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**
```bash
python -m uvicorn main:app --reload
```

5. **Acesse no navegador**
```
http://localhost:8000
```

---

### Rotas Disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/` | Página principal com lista de alunos |
| `GET` | `/cadastro` | Formulário de cadastro |
| `POST` | `/cadastro` | Processa cadastro de novo aluno |
| `GET` | `/editar/{id}` | Formulário de edição |
| `POST` | `/atualizar/{id}` | Atualiza dados do aluno |
| `GET` | `/deletar/{id}` | Remove aluno da lista |


---

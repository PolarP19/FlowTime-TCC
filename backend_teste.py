# backend.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

app = FastAPI()

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MODELOS DE DADOS
class GastosModel(BaseModel):
    anual: float = Field(ge=0)
    mensal: float = Field(ge=0)
    semanal: float = Field(ge=0)
    diario: float = Field(ge=0)

class OrcamentoModel(BaseModel):
    renda: float = Field(ge=0)
    investimento: str
    gastos: GastosModel

class RotinaModel(BaseModel):
    horario: str
    clima: Optional[str] = ""
    agenda: str
    cardio: float = Field(ge=0)
    km: float = Field(ge=0)
    alimentacao: str

# ROTA DE ORÇAMENTO
@app.post("/orcamento")
def avaliar_orcamento(orcamento: OrcamentoModel):
    if orcamento.gastos.mensal > orcamento.renda * 0.5:
        sugestao = "Considere reduzir seus gastos mensais para economizar mais."
    else:
        sugestao = "Seus gastos estão equilibrados com sua renda."
    return {
        "mensagem": "Orçamento processado com sucesso.",
        "sugestao": sugestao
    }

# ROTA DE ROTINA
@app.post("/rotina")
def registrar_rotina(rotina: RotinaModel):
    return {
        "mensagem": "Rotina registrada com sucesso.",
        "detalhes": rotina
    }

# EXECUÇÃO
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)

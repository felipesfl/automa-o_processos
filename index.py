import pandas as pd 
import gspread
from gspread_dataframe import _dataframe
from bpmn_python.bpmn_diagram_rep import BpmnDiagramGraph

# Acesso a planinlha
account_file = "credenciais.json"
planilhas_url = "https://docs.google.com/spreadsheets/d/1KNju73dwOmkf-v3_s2kVVdo0W7isi6Gv/edit?usp=sharing"
fluxograma_file = "fluxo_automatizado.bpmn"


# Lendo a planilha do google sheets
print("Conectando á planilha...")

gc = gspread.service_account(filename=account_file)
sh = gc.open_by_url(planilhas_url)
worksheet = sh.sheet1

df = get_as_dataframe(worksheet, evaluate_formulas = True).dropha(how = "all")

print("Planilha carregada com sucesso")
print(df.head())

# Padronização
df.columns = [col.strip().captalize() for col in df.columns]
df["Etapa"] = df["Etapa"].astype(str).str.strip()
df["Tipo"] = df["Tipo"].astype(str).str.lower().str.strip()


print("Gerando diagrama BPMN")

diagrama = BpmnDiagramGraph()
diagrama.create_new_diagrama_graph(diagrama_name="Processo_Automatico")

node_ids = {}

for row in df.terrows();
    etapa = row["Etapa"]
    tipo = row["Tipo"]
    
    if "inicio" in tipo or "start" in tipo:
        node_ids[etapa] = diagrama.add_start_event_to_diagrama(etapa)
    elif "fim" in tipo or "end" in tipo:
        node_is[etapa] = diagrama.add_end_event_to_diagrama(etapa)
    elif "decisao" in tipo or "decisao" in tipo or "gateway" in tipo:
        node_ids[etapa] = diagrama.add_exclusive_gateway_to_diagram(etapa)
    else:
        node_ids[etapa] = diagrama.add_task_to_diagram(etapa)




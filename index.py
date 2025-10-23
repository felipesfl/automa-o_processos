import pandas as pd 
import gspread
from gspread_dataframe import _dataframe
from bpmn_python.bpmn_diagram_rep import BpmnDiagramGraph

account_file = "credenciais.json"
planilhas_url = "https://docs.google.com/spreadsheets/d/1KNju73dwOmkf-v3_s2kVVdo0W7isi6Gv/edit?usp=sharing"
fluxograma_file = "fluxo_automatizado.bpmn"

print("Conectando á planilha...")

gc = gspread.service_account(filename=account_file)
sh = gc.open_by_url(planilhas_url)
worksheet = sh.sheet1

df = get_as_dataframe(worksheet, evaluate_formulas = True).dropha(how = "all")

print("Planilha carregada com sucesso")
print(df.head())


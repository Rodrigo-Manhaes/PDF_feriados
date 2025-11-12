import tkinter as tk
from tkinter import filedialog
import requests
import PyPDF2
import re

def selecionar_arquivo():
    caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo PDF", filetypes=[("PDF files", "*.pdf")])
    if caminho_arquivo:
        verificar_feriados(caminho_arquivo)

def verificar_feriados(caminho_pdf):
    with open(caminho_pdf, "rb") as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        texto = ""
        for pagina in leitor.pages:
            texto += pagina.extract_text()
    datas_pdf = re.findall(r"\d{4}-\d{2}-\d{2}", texto)

    url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"
    resposta = requests.get(url)
    feriados = resposta.json()

    datas_feriados = [f["date"] for f in feriados]

    comuns = set(datas_pdf) & set(datas_feriados)

    if comuns:
        print("Datas que são feriados:")
        for data in comuns:
            nome = next((f["localName"] for f in feriados if f["date"] == data), "")
            print(f"{data} - {nome}")
    else:
        print("Nenhuma data do PDF é feriado.")

root = tk.Tk()
root.title("Verificador de Feriados")
botao = tk.Button(root, text="Selecionar PDF", command=selecionar_arquivo)
botao.pack(padx=20, pady=20)
root.mainloop()

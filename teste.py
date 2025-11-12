import tkinter as tk
from tkinter import filedialog
import requests

def selecionar_arquivo():
    caminho_do_arquivo = filedialog.askopenfilename(title = "Selecione um Arquivo")

root = tk.Tk()
root.title("Leitor de arquivo")
botao = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
botao.pack(padx=20, pady=20)

url = "https://date.nager.at/api/v3/PublicHolidays/2025/BR"

payload = {}
headers = {
  'accept': 'application/json',
  'X-CSRF-TOKEN': 'pYBqfz7tfH5NFeqA2YXNhdZIsqRCMmef6FjOTNJz'
  }

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)



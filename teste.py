import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    caminho_do_arquivo = filedialog.askopenfilename(title = "Selecione um Arquivo")

root = tk.Tk()
root.title("Leitor de arquivo")
botao = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
botao.pack(padx=20, pady=20)

root.mainloop()







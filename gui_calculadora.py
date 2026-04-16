#importação das bibliotecas necessárias
import tkinter as tk
import math

#janela principal
janela = tk.Tk()
janela.title("Calculadora cientifica")
janela.geometry("350x500")

#visor da calculadora
display = tk.Entry(janela, font=("Times New Roman", 20), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#inserir valor no display
def inserir(valor):
    display.insert(tk.END, valor)

#limpar o display
def limpar():
    display.delete(0, tk.END)

#calcular o resultado da expressão
def calcular():
    try:
        conta = display.get()
        resultado = eval(conta)
        limpar()
        display.insert(tk.END, resultado)
    except:
        limpar()
        display.insert(tk.END, "Erro")


#calcular raiz quadrada, logaritmo, seno e cosseno
def raiz():
    try:
        valor = float(display.get())
        resultado = math.sqrt(valor)
        limpar()
        display.insert(tk.END, resultado)
    except:
        limpar()
        display.insert(tk.END, "Erro")

def logaritmo():
    try:
        valor = float(display.get())
        resultado = math.log10(valor)
        limpar()
        display.insert(tk.END, resultado)
    except:
        limpar()
        display.insert(tk.END, "Erro")

def seno():
    try:
        valor = float(display.get())
        resultado = math.sin(math.radians(valor))
        limpar()
        display.insert(tk.END, resultado)
    except:
        limpar()
        display.insert(tk.END, "Erro")

def cosseno():
    try:
        valor = float(display.get())
        resultado = math.cos(math.radians(valor))
        limpar()
        display.insert(tk.END, resultado)
    except:
        limpar()
        display.insert(tk.END, "Erro")

#botoes da calculadora
def criar_botao(texto, linha, coluna, comando):
    tk.Button(
        janela,
        text=texto,
        width=5,
        height=2,
        bg="orange",
        fg="white",
        activebackground="darkorange",
        activeforeground="white",
        font=("Times New Roman", 14),
        command=comando
    ).grid(row=linha, column=coluna, padx=5, pady=5)

# Primeira linha
criar_botao("7", 1, 0, lambda: inserir("7"))
criar_botao("8", 1, 1, lambda: inserir("8"))
criar_botao("9", 1, 2, lambda: inserir("9"))
criar_botao("/", 1, 3, lambda: inserir("/"))

# Segunda linha
criar_botao("4", 2, 0, lambda: inserir("4"))
criar_botao("5", 2, 1, lambda: inserir("5"))
criar_botao("6", 2, 2, lambda: inserir("6"))
criar_botao("*", 2, 3, lambda: inserir("*"))

# Terceira linha
criar_botao("1", 3, 0, lambda: inserir("1"))
criar_botao("2", 3, 1, lambda: inserir("2"))
criar_botao("3", 3, 2, lambda: inserir("3"))
criar_botao("-", 3, 3, lambda: inserir("-"))

# Quarta linha
criar_botao("0", 4, 0, lambda: inserir("0"))
criar_botao(".", 4, 1, lambda: inserir("."))
criar_botao("=", 4, 2, calcular)
criar_botao("+", 4, 3, lambda: inserir("+"))

# Quinta linha
criar_botao("C", 5, 0, limpar)
criar_botao("√", 5, 1, raiz)
criar_botao("log", 5, 2, logaritmo)
criar_botao("sin", 5, 3, seno)

# Sexta linha
criar_botao("cos", 6, 0, cosseno)
criar_botao("xʸ", 6, 1, lambda: inserir("**"))

# Inicia o loop da interface gráfica
janela.mainloop()




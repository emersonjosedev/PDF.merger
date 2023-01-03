import PyPDF2
import os
import sys


pergunta = input("Quer continuar? digite s! quer sair? digite qualquer letra!")
print(pergunta)
um = "s"
dois = "n"

#DEFININDO FUNÇAO DE INICIAR
def iniciar():
        merger = PyPDF2.PdfMerger()
        lista_arquivos = os.listdir("mesclagem")
        for arquivo in lista_arquivos:
            if ".pdf" in arquivo:
                merger.append(f"mesclagem/{arquivo}")

        merger.write("PDF mesclado.pdf")
        print("sucesso")

#DEFININDO FUNÇAO DE PARAR
def parar():
    print("erro")
    sys.exit()

#CRIANDO LOOP
while True:
    if pergunta == um:
        iniciar()
        break
    else:
        parar()
































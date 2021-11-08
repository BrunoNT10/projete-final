from tkinter import *
import tkinter as tk
import sys

sys.path.insert(1, "diretorio1")

try:
    arquivo = open("cores_capacete.txt")
    capacete = 1
    

except OSError:
    capacete = 0

try:
    arquivo = open("cores_camisa.txt")
    camisa = 1
    

except OSError:
    camisa = 0

try:
    arquivo = open("cores_luvas.txt")
    luvas = 1
    
except OSError:
    luvas = 0

try:
    arquivo = open("cores_botas.txt")
    botas = 1
    

except OSError:
    botas = 0

try:
    arquivo = open("cores_cinto.txt")
    cinto = 1
    

except OSError:
    cinto = 0

try:
    arquivo = open("cores_pa.txt")
    pa = 1
    

except OSError:
    pa = 0

try:
    arquivo = open("cores_mascara.txt")
    mascara = 1
   
except OSError:
    mascara = 0

try:
    arquivo = open("cores_calca.txt")
    calca = 1
    
except OSError:
    calca = 0

def comecar():
    janela1.destroy()
    janela = tk.Tk()
    janela.title("CEPEG - cadastro das EPI's")
    janela.geometry("1300x700")

    def cadastra_capacete():
        import cor_capacete

    def cadastra_luvas():
        import cor_luvas

    def cadastra_camisa():
        import cor_camisa

    def cadastra_calca():
        import cor_calca

    def cadastra_mascara():
        import cor_mascara

    def cadastra_botas():
        import cor_bota

    def cadastra_pa():
        import cor_pa

    def cadastra_cinto():
        import cor_cinto

    lb = Label(janela, 
           text = "Qual EPI deseja cadastrar a cor? \nAs EPI's marcadas em vermelho ainda não tiveram suas cores cadastradas", 
           font=("calibri 18"))
    lb.place(x=310,y=50)

    lb1 = Label(janela, text="Capacete ou alguma outra EPI para a cabeça", font = ("calibri 14"))
    lb1.place(x=310, y=150)

    bt1 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_capacete)
    bt1.place(x=723,y=146)
    bt1["bg"] = "blue"
    bt1["fg"] = "white"

    if capacete == 1:
        lb1["bg"] = "light green"

    elif capacete == 0:
        lb1["bg"] = "red"

    lb2 = Label(janela, text="Colete ou camisa específica de proteção", font=("calibri 14"))
    lb2.place(x=310, y=200)

    bt2 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_camisa)
    bt2.place(x=723,y=196)
    bt2["bg"] = "blue"
    bt2["fg"] = "white"

    if camisa == 1:
        lb2["bg"] = "light green"

    elif camisa == 0:
        lb2["bg"] = "red"

    lb3 = Label(janela, text="Luvas ou alguma outra EPI de proteção às mãos", font=("calibri 14"))
    lb3.place(x=310, y=250)

    bt3 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_luvas)
    bt3.place(x=723,y=246)
    bt3["bg"] = "blue"
    bt3["fg"] = "white"

    if luvas == 1:
        lb3["bg"] = "light green"

    elif luvas == 0:
        lb3["bg"] = "red"

    lb4 = Label(janela, text="Calca específica de proteção", font=("calibri 14"))
    lb4.place(x=310, y=300)

    bt4 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_calca)
    bt4.place(x=723,y=296)
    bt4["bg"] = "blue"
    bt4["fg"] = "white"

    if calca == 1:
        lb4["bg"] = "light green"

    elif calca == 0:
        lb4["bg"] = "red"

    lb5 = Label(janela, text="Botas ou algum sapato de proteção", font=("calibri 14"))
    lb5.place(x=310, y=350)

    bt5 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_botas)
    bt5.place(x=723,y=346)
    bt5["bg"] = "blue"
    bt5["fg"] = "white"

    if botas == 1:
        lb5["bg"] = "light green"

    elif botas == 0:
        lb5["bg"] = "red"

    lb6 = Label(janela, text="Protetor auricular", font=("calibri 14"))
    lb6.place(x=310, y=400)

    bt6 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_pa)
    bt6.place(x=723,y=396)
    bt6["bg"] = "blue"
    bt6["fg"] = "white"

    if pa == 1:
        lb6["bg"] = "light green"

    elif pa == 0:
        lb6["bg"] = "red"

    lb7 = Label(janela, text="Máscara de proteção facial", font=("calibri 14"))
    lb7.place(x=310, y=450)

    bt7 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_mascara)
    bt7.place(x=723,y=446)
    bt7["bg"] = "blue"
    bt7["fg"] = "white"

    if mascara == 1:
        lb7["bg"] = "light green"

    elif mascara == 0:
        lb7["bg"] = "red"

    lb8 = Label(janela, text="Cinto de segurança", font=("calibri 14"))
    lb8.place(x=310, y=500)

    bt8 = Button(janela, text="Cadastrar cor", font=("calibri 14"), width=30, command=cadastra_cinto)
    bt8.place(x=723,y=496)
    bt8["bg"] = "blue"
    bt8["fg"] = "white"

    if cinto == 1:
        lb8["bg"] = "light green"

    elif cinto == 0:
        lb8["bg"] = "red"

janela1 = tk.Tk()

janela1.geometry("1300x700")
janela1.title("CEPEG - Cadastro das EPI's")

lb9 = Label(janela1, 
text="Para cadastrar a cor, você deverá exibir a EPI para a câmera, portanto, use um lugar adequado e\n com boa iluminação. Para a cor ser cadastrada corretamente, posicione a EPI\n ao centro do círculo que irá aparecer na sua câmera.",
font=("calibri 20"))
lb9.place(x=152,y=150)

bt = Button(janela1, text="Começar", font=("calibri 20"), width=40, command=comecar)
bt.place(x=380, y=280)
bt["bg"] = "light green"

janela1.mainloop()





    

from tkinter import *
import tkinter as tk
import serial
import sys
 
def RFID_nome():
        
    def func_nome():
            
        def profissao():

            def cadastra_tag():

                def proximo():
                    import cadastra_func1.py

                def concluido():
                    janela1.destroy()

                x = 0
                for x in range(x, 100):
                    print("tempo")
                print("cheguei aqui")
                ser = serial.Serial("COM3")
                valor_id = ser.readline()
                lb7 = Label(janela1, text = "TAG cadastrada", font=("calibri 14"))
                lb7.place(x=573, y=450)
                lb7["bg"] = "light green"
                ser.close()
                valor_id = valor_id.decode("utf-8")
                valor_id = valor_id.rstrip("\n")
                valor_id = valor_id.rstrip("\r")
                print(valor_id)
                nome_arquivo = valor_id + ".txt"
                arquivo = open(nome_arquivo, "w")
                arquivo.write(nome_func)
                prof_name = ed4.get()
                prof_name = prof_name + ".txt"
                arquivo1 = open(prof_name, "r")
                texto1 = arquivo1.read()
                arquivo = open(nome_arquivo, "a")
                arquivo.writelines(texto1)

                bt5 = Button(janela1, text = "Cadastrar outro funcionário", command=proximo, font=("calibri 14")).place(x=442, y = 500)
                bt6 = Button(janela1, text = "Concluído", command=concluido, font=("calibri 14"), width=15).place(x=708, y=500)


            lb6 = Label(janela1, text="Aproxime o cartão do leitor RFID", font=("calibri 19")).place(x=350,y=400)
            bt7 = Button(janela1, text="Cadastrar TAG RFID", width=20, font = ("calibri 14"), command=cadastra_tag).place(x=695, y=398)
            bt4.destroy()

            lb5 = Label(janela1, text="Salvo corretamente", font=("calibri 11"))
            lb5.place(x=700,y=338)
            lb5["bg"] = "light green"

            
        nome_func = ed3.get() + "\n"

        texto_lb6 = "Digite a profissão de " + nome_func

        bt3.destroy()
        lb5 = Label(janela1, text="Nome salvo corretamente", font=("calibri 11"))
        lb5.place(x=700,y=258)
        lb5["bg"] = "light green"

        lb6 = Label(janela1,text=texto_lb6, font = ("calibri 19"))
        lb6.place(x=442, y=290)
        
        ed4 = Entry(janela1, width=40)
        ed4.place(x=442, y=340)

        bt4 = Button(janela1, text="Enviar", command=profissao, font=("calibri 10"), width=23)
        bt4.place(x=700,y=338)
        bt4["bg"] = "light green"
        
    lb4 = Label(janela1,text="Digite o nome do funcionário (completo)", font = ("calibri 19"))
    lb4.place(x=445, y=210)
    
    ed3 = Entry(janela1, width=40)
    ed3.place(x=442, y=260)

    bt3 = Button(janela1, text="Enviar", command=func_nome, font=("calibri 10"), width=23)
    bt3.place(x=700,y=258)
    bt3["bg"] = "light green"

janela1 = tk.Tk()
janela1.geometry("1300x700")
janela1.title("Cadastrar funcionários")           
lb3 = Label(janela1,text="Cadastre cada funcionário, de acordo com o seu setor de serviço dentro da empresa", font = ("calibri 19"))
lb3.place(x=240,y=105)

bt2 = Button(janela1, text="Começar", command=RFID_nome, font=("calibri 14"), width=23)
bt2.place(x=535,y=148)
bt2["bg"] = "light green"

          
janela1.mainloop()
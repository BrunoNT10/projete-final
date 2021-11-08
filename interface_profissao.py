from tkinter import *
import tkinter as tk
import sys

sys.path.insert(1, "diretorio1")

def janela2():

    janela.destroy() 
    janela3 = tk.Tk()
    janela3.geometry("1300x700")
    janela3.title("Cadastro")
    janela3["bg"] = "light blue"

    
    def nome():
        
        bt2.destroy()
        lb6 = Label(janela3, text = "Função salva com sucesso", font=("calibri 18"))
        lb6.place(x=650, y=193)
        lb6["bg"] = "light green"
        
        #se capacete = Sim
        def capacete_sim():
            #se capacete = Sim e camisa = Sim 
            def camisa_sim():
                #se capacete = Sim, camisa = Sim e luva Sim
                def luva_sim():
                    
                    def calca_sim():
                        def bota_sim():
                            
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")

                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")

                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")


                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")

                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)



                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")

                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)
                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")

                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)

                    lb9["bg"] = "light green"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nluvas")



                def luva_nao():
                    def calca_sim():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():

                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")

                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400) 

                    lb9["bg"] = "red"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nnao")

                #parte de cadastrar luvas
                lb9 = Label(janela3, text= "Luvas ou outra EPI de proteção às mãos")
                lb9.place(x=190, y=500)
                lb9["bg"] = "light blue"

                bt7 = Button(janela3, text="Sim", command=luva_sim)
                bt7.place(x=411,y=498)

                bt8= Button(janela3, text="Não", command=luva_nao)
                bt8.place(x=448,y=498)

                lb5["bg"] = "light green"
                bt5.destroy()
                bt6.destroy()
                lb8 = Label(janela3, text="EPI salva") 
                lb8.place(x=448,y=440)
                lb8["bg"] = "light green"

                arquivo = open(arquivo_nome, 'r')
                conteudo = arquivo.readlines()
                arquivo = open(arquivo_nome, 'w')
                arquivo.writelines(conteudo)
                arquivo.writelines("\ncamisa")


            def camisa_nao():
                
                def luva_sim():
                    def calca_sim():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
 
                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")
                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)
                    lb9["bg"] = "light green"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nluvas")

                def luva_nao():
                    def calca_sim():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")

                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)
                    lb9["bg"] = "red"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nnao")

                #parte de cadastrar luvas
                lb9 = Label(janela3, text= "Luvas ou outra EPI de proteção às mãos")
                lb9.place(x=190, y=500)
                lb9["bg"] = "light blue"

                bt7 = Button(janela3, text="Sim", command=luva_sim)
                bt7.place(x=411,y=498)

                bt8= Button(janela3, text="Não", command=luva_nao)
                bt8.place(x=448,y=498)

                lb5["bg"] = "red"
                bt5.destroy()
                bt6.destroy()
                lb8 = Label(janela3, text="EPI salva") 
                lb8.place(x=448,y=440)
                lb8["bg"] = "light green"

                arquivo = open(arquivo_nome, 'r')
                conteudo = arquivo.readlines()
                arquivo = open(arquivo_nome, 'w')
                arquivo.writelines(conteudo)
                arquivo.writelines("\nnao")

            #parte de cadastrar camiseta de proteção
            lb5 = Label(janela3, text="Algum colete de proteção ou camisa específica\n de proteção")
            lb5.place(x=190,y= 440)
            lb5["bg"] = "light blue"

            bt5 = Button(janela3, text="Sim", command=camisa_sim)
            bt5.place(x=448,y=438)

            bt6= Button(janela3, text="Não", command=camisa_nao)
            bt6.place(x=485,y=438)

            lb3["bg"] = "light green"
            bt3.destroy()
            bt4.destroy()
            lb7 = Label(janela3, text="EPI salva") 
            lb7.place(x=434,y=400)
            lb7["bg"] = "light green"
        
            arquivo = open(arquivo_nome, "w")
            arquivo.write("capacete")
            arquivo.close()

        def capacete_nao():

            def camisa_sim():

                def luva_sim():

                    def calca_sim():

                        def bota_sim():

                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")

                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)

                    lb9["bg"] = "light green"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nluvas")
        
                def luva_nao():
                    def calca_sim():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)  

                                


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)
                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")
                    
                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)

                    lb9["bg"] = "red"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nnao")

                #parte de cadastrar luvas
                lb9 = Label(janela3, text= "Luvas ou outra EPI de proteção às mãos")
                lb9.place(x=190, y=500)
                lb9["bg"] = "light blue"

                bt7 = Button(janela3, text="Sim", command=luva_sim)
                bt7.place(x=411,y=498)

                bt8= Button(janela3, text="Não", command=luva_nao)
                bt8.place(x=448,y=498)

                lb5["bg"] = "light green"
                bt5.destroy()
                bt6.destroy()
                lb8 = Label(janela3, text="EPI salva") 
                lb8.place(x=448,y=440)
                lb8["bg"] = "light green"

                arquivo = open(arquivo_nome, 'r')
                conteudo = arquivo.readlines()
                arquivo = open(arquivo_nome, 'w')
                arquivo.writelines(conteudo)
                arquivo.writelines("\ncamisa")


            def camisa_nao():
                
                def luva_sim():

                    def calca_sim():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")

                    
                    def calca_nao():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")
                    
                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)

                    lb9["bg"] = "light green"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nluvas")
        
                def luva_nao():

                    def calca_sim():
                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)
                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "light green"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\ncalca")
                    
                    def calca_nao():

                        def bota_sim():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)

                            lb13["bg"] = "light green"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nbotas")

                        def bota_nao():
                            def pa_sim():

                                lb15["bg"] = "light green"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nprotetor auricular")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)


                            def pa_nao():
                                
                                lb15["bg"] = "red"
                                bt13.destroy()
                                bt14.destroy()
                                lb16 = Label(janela3, text="EPI salva") 
                                lb16.place(x=656, y=498)
                                lb16["bg"] = "light green"

                                arquivo = open(arquivo_nome, 'r')
                                conteudo = arquivo.readlines()
                                arquivo = open(arquivo_nome, 'w')
                                arquivo.writelines(conteudo)
                                arquivo.writelines("\nnao")
                                def mascara_sim():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)  

                                    lb17["bg"] = "light green"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"                                

                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nmascara")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)
                                    
                                def mascara_nao():

                                    def cinto_sim():

                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\ncinto")

                                        lb18["bg"] = "light green"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)                                       

                                    def cinto_nao():
                                        def cadastra():
                                            janela3.destroy()
                                            import interface_profissao1

                                        def concluido():
                                            janela3.destroy()

                                        arquivo = open(arquivo_nome, 'r')
                                        conteudo = arquivo.readlines()
                                        arquivo = open(arquivo_nome, 'w')
                                        arquivo.writelines(conteudo)
                                        arquivo.writelines("\nnao")

                                        lb18["bg"] = "red"
                                        bt17.destroy()
                                        bt18.destroy()
                                        lb20 = Label(janela3, text="EPI salva") 
                                        lb20.place(x=965, y=438)
                                        lb20["bg"] = "light green"

                                        bt19 = Button(janela3, text = "Cadastrar outra função", command=cadastra)
                                        bt19.place(x=850, y=498)

                                        bt20 = Button(janela3, text="Concluido", command=concluido) 
                                        bt20.place(x=990, y=498)

                                    lb17["bg"] = "red"
                                    bt15.destroy()
                                    bt16.destroy()
                                    lb19 = Label(janela3, text="EPI salva") 
                                    lb19.place(x=1003, y=398)
                                    lb19["bg"] = "light green"
                                    
                                    arquivo = open(arquivo_nome, 'r')
                                    conteudo = arquivo.readlines()
                                    arquivo = open(arquivo_nome, 'w')
                                    arquivo.writelines(conteudo)
                                    arquivo.writelines("\nnao")

                                    lb18 = Label(janela3, text="Cinto de segurança")
                                    lb18.place(x=850, y=440)

                                    lb18["bg"] = "light blue"

                                    bt17 = Button(janela3, text="Sim", command = cinto_sim)
                                    bt17.place(x=965, y=438)

                                    bt18 = Button(janela3, text="Não", command=cinto_nao)
                                    bt18.place(x=1002,y=438)

                                lb17 = Label(janela3, text="Máscara de proteção facial")
                                lb17.place(x=850, y=400)

                                lb17["bg"] = "light blue"
                                 
                                bt15 = Button(janela3, text="Sim", command=mascara_sim)
                                bt15.place(x=1003,y=398)

                                bt16 = Button(janela3, text="Não", command=mascara_nao)
                                bt16.place(x=1040,y=398)

                                
                            #parte de cadastrar protetor auricular
                            lb15 = Label(janela3, text="Protetor auricular")
                            lb15.place(x=550,y=500)
                            lb15["bg"] = "light blue"

                            bt13 = Button(janela3, text="Sim", command=pa_sim)
                            bt13.place(x=656, y=498)

                            bt14 = Button(janela3, text="Não", command=pa_nao)
                            bt14.place(x=693,y=498)
                            
                            lb13["bg"] = "red"
                            bt11.destroy()
                            bt12.destroy()
                            lb14 = Label(janela3, text="EPI salva") 
                            lb14.place(x=746,y=438)
                            lb14["bg"] = "light green"

                            arquivo = open(arquivo_nome, 'r')
                            conteudo = arquivo.readlines()
                            arquivo = open(arquivo_nome, 'w')
                            arquivo.writelines(conteudo)
                            arquivo.writelines("\nnao")

                        #parte de cadastrar botas
                        lb13 = Label(janela3, text="Botas ou algum sapato de proteção")
                        lb13.place(x=550,y=440)
                        lb13["bg"] = "light blue"

                        bt11 = Button(janela3, text="Sim", command=bota_sim)
                        bt11.place(x=756,y=438)

                        bt12 = Button(janela3, text="Não", command=bota_nao)
                        bt12.place(x=793, y=438)

                        lb11["bg"] = "red"
                        bt9.destroy()
                        bt10.destroy()
                        lb12 = Label(janela3, text="EPI salva") 
                        lb12.place(x=752,y=400)
                        lb12["bg"] = "light green"

                        arquivo = open(arquivo_nome, 'r')
                        conteudo = arquivo.readlines()
                        arquivo = open(arquivo_nome, 'w')
                        arquivo.writelines(conteudo)
                        arquivo.writelines("\nnao")
                    
                    #parte de cadastrar calças de proteção
                    lb11 = Label(janela3, text="Alguma calça específica de proteção\n ou algo do tipo")
                    lb11.place(x=550,y=400)
                    lb11["bg"] = "light blue"

                    bt9 = Button(janela3, text="Sim", command=calca_sim)
                    bt9.place(x=752,y=400)

                    bt10 = Button(janela3, text="Não", command=calca_nao)
                    bt10.place(x=789,y=400)

                    lb9["bg"] = "red"
                    bt7.destroy()
                    bt8.destroy()
                    lb10 = Label(janela3, text="EPI salva") 
                    lb10.place(x=411,y=500)
                    lb10["bg"] = "light green"

                    arquivo = open(arquivo_nome, 'r')
                    conteudo = arquivo.readlines()
                    arquivo = open(arquivo_nome, 'w')
                    arquivo.writelines(conteudo)
                    arquivo.writelines("\nnao")

                #parte de cadastrar luvas
                lb9 = Label(janela3, text= "Luvas ou outra EPI de proteção às mãos")
                lb9.place(x=190, y=500)
                lb9["bg"] = "light blue"

                bt7 = Button(janela3, text="Sim", command=luva_sim)
                bt7.place(x=411,y=498)

                bt8= Button(janela3, text="Não", command=luva_nao)
                bt8.place(x=448,y=498)
                
                lb5["bg"] = "red"
                bt5.destroy()
                bt6.destroy()
                lb8 = Label(janela3, text="EPI salva") 
                lb8.place(x=448,y=440)
                lb8["bg"] = "light green"

                arquivo = open(arquivo_nome, 'r')
                conteudo = arquivo.readlines()
                arquivo = open(arquivo_nome, 'w')
                arquivo.writelines(conteudo)
                arquivo.writelines("\nnao")

            #parte de cadastrar camiseta de proteção
            lb5 = Label(janela3, text="Algum colete de proteção ou camisa específica\n de proteção")
            lb5.place(x=190,y= 440)
            lb5["bg"] = "light blue"

            bt5 = Button(janela3, text="Sim", command=camisa_sim)
            bt5.place(x=448,y=438)

            bt6= Button(janela3, text="Não", command=camisa_nao)
            bt6.place(x=485,y=438)
            arquivo_func1.write("nao")
            lb3["bg"] = "red"
            bt3.destroy()
            bt4.destroy()
            lb7 = Label(janela3, text="EPI salva") 
            lb7.place(x=434,y=400)
            lb7["bg"] = "light green"

            arquivo = open(arquivo_nome, 'r')
            conteudo = arquivo.readlines()
            arquivo = open(arquivo_nome, 'w')
            arquivo.writelines(conteudo)
            arquivo.writelines("nao")

        arquivo_nome=ed1.get()
        arquivo_nome=arquivo_nome+".txt"
        arquivo_func1=open(arquivo_nome, "a")
        
        lb4 = Label(janela3, text="Se essa funcao na empresa precisar da EPI, clique em Sim, se não, clique em não",
        font=("calibri 20"))
        lb4.place(x=200,y=300)
        lb4["bg"] = "light blue"
        
        #parte de cadastrar capacete
        lb3 = Label(janela3, text="Capacete ou alguma outra EPI para a cabeça")
        lb3.place(x=190,y=400)
        lb3["bg"] = "light blue"

        bt3 = Button(janela3, text="Sim", command=capacete_sim)
        bt3.place(x=434,y=398)

        bt4= Button(janela3, text="Não", command=capacete_nao)
        bt4.place(x=471,y=398)

    lb2 = Label(janela3, text="Digite o nome do setor a ser cadastrado", font=("calibri 40"))
    lb2.place(x=200,y=100)
    lb2["bg"] = "light blue"

    ed1 = Entry(janela3, width=40)
    ed1.place(x=350, y=200)

    bt2 = Button(janela3, width=40, text="Enviar", command=nome)
    bt2.place(x=650, y=200)
    bt2["bg"] = "light green"
    

janela = tk.Tk()
janela.geometry("1300x700")
janela["bg"] = "light blue"
janela.title("CEPEG")

lb = Label(janela, text="Bem vindo ao CEPEG! Auxiliando \n na proteção da sua empresa!", 
        font = ("calibri 40"))
lb.place(x=250,y=100)
lb["bg"] = "light blue"

bt1 = Button(janela, text="Começar", font = ("calibri 30"), width=20, command=janela2)
bt1.place(x=400, y=350)
bt1["bg"] = "green"
bt1["fg"] = "white"

janela.mainloop()
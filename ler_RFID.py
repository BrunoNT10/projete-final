import cv2
import numpy as np 
import imutils
from time import sleep
import pyrebase
from datetime import *
import serial
import sys
import shutil
import os

sys.path.insert(1, "diretorio1")

def verifica_epi1():
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year
    dia = str(dia)
    mes = str(mes)
    ano = str(ano)

    data_real = dia + "-" + mes + "-" + ano
    print(data_real)

    var_capacete = 0
    try:
        open("cores_capacete.txt")

    except:
        var_capacete = 1
    var_luva= 0
    try:
        open("cores_luvas.txt")

    except:
        var_luva = 1
    var_camisa = 0
    try:
        open("cores_camisa.txt")

    except:
        var_camisa=1
    var_mascara = 0
    try:
        open("cores_mascara.txt")

    except:
        var_mascara = 1
    var_bota=0

    try:
        open("cores_botas.txt")
    except:
        var_bota=1
    var_pa=0
    try:
        open("cores_pa.txt")

    except:
        var_pa=1
    var_cinto=0
    try:
        open("cores_cinto.txt")

    except:
        var_cinto=1
    var_calca=0
    try:
        open("cores_calca.txt")

    except:
        var_calca=1

    config = {

        "apiKey": "AIzaSyBeVBuTS5ZP_7czH3nk2rA6t_aH8vUECOA",
        "authDomain": "projete-2021.firebaseapp.com",
        "databaseURL": "https://projete-2021-default-rtdb.firebaseio.com",
        "projectId": "projete-2021",
        "storageBucket": "projete-2021.appspot.com",
        "messagingSenderId": "720238893966",
        "appId": "1:720238893966:web:9f612342c08fe31ea5a2df",
        "measurementId": "G-FWJH11ZF9M"

    }

    firebase = pyrebase.initialize_app(config)

    dados = firebase.database()

    ler_arquivo = open("nome_do_arquivo.txt","r").readlines()[0]
    ler_arquivo = str(ler_arquivo)
    ler_arquivo = ler_arquivo.rstrip("\n")

    print(ler_arquivo)

    arquivonome = ler_arquivo + ".txt"

    ser = serial.Serial("COM3", 9600)
    valor_botao = ser.readline()
    valor = int(valor_botao)
    ser.close()
    camera = cv2.VideoCapture(0)
   
    var = 0

    if valor == 1:
        black = (0, 0, 0)
        while var < 350:

            var = var + 1
            _, video = camera.read()

            video = imutils.resize(video, width=600)
            video = cv2.flip(video, 1)
            cv2.rectangle(video, (270,1), (400, 70), black, 1)#capacete
            cv2.rectangle(video, (315, 70), (355, 120), black, 1)#mascara
            cv2.rectangle(video, (270, 45), (333, 105), black, 1)#pa1
            cv2.rectangle(video, (337, 45), (395, 105), black, 1)#pa2
            cv2.rectangle(video, (250, 140), (420, 200), black, 1)#camisa
            cv2.rectangle(video, (250, 220), (420, 280), black, 1)#cinto
            cv2.rectangle(video, (250, 340), (420, 380), black, 1)#calca
            cv2.rectangle(video, (250, 390), (330, 449), black, 1)#bota1
            cv2.rectangle(video, (340, 390), (420, 449), black, 1)#bota2
            cv2.rectangle(video, (170, 215), (230, 275), black, 1)#luva1
            cv2.rectangle(video, (440, 215), (500, 275), black, 1)#luva2
    
            cv2.imshow("video", video)
            if cv2.waitKey(1) == ord("q"):
                break
    
        
    arduino = serial.Serial("COM3", 9600)

    nomefunc = open(arquivonome,"r").readlines()[0]

    print(nomefunc)
    nomefunc = str(nomefunc)

    nomefunc = nomefunc.rstrip("\n")
    print(nomefunc)

    dados.child().update({"Nome": nomefunc})

    print("verificação do capacete")

    ler = open(arquivonome, "r").readlines()[1]
    capacete = str(ler)
    print(capacete)

    teste = open("cores_capacete.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_capacete.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_capacete.txt", "r").readlines()[2]
    b3 = teste

    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_capacete==1:
        ler = "nao"

    capacete_sim = 0

    if ler == "capacete\n":
        var = 0
        while True: 
            var = var+ 1
            y = 1
            for y in range(y, 70): #valor max = 70
                x = 270
                for x in range(x, 400): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 20
                                if w >= 70:
                                    w = 69

                                z = x + 20
                                if z >=400:
                                    z = 399
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    capacete_sim = 1

                                    break
                if capacete_sim == 1:
                    print("Capacete encontrado")

                    break
        
            if capacete_sim == 1:
            
                break
            if var == 2:
                break

        if capacete_sim == 1:
            capacete1 = 1

        else:
            capacete1 = 0
            print("Capacete não encontrado")

    else: 
        capacete1 = 2
        print("capacete desnecessário")

    print("----------------------------------")
    print("verificação dados mascara")

    ler = open(arquivonome, "r").readlines()[7]

    teste = open("cores_mascara.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_mascara.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_mascara.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_mascara==1:
        ler = "nao"

    mascara_sim = 0

    if ler == "mascara\n":
        var = 0
        var2 = 0
        while True: 
            var = var + 1
            y = 70
            for y in range(y, 120): #valor max = 70
                x = 315
                for x in range(x, 355): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 130:
                                    w = 119

                                z = x + 10
                                if z >=355:
                                    z = 354
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    mascara_sim = 1

                                    break
                if mascara_sim == 1:
                    print("mascara encontrado")

                    break
        
            if mascara_sim == 1:
            
                break
            if var == 2:
                break

        if mascara_sim == 1:
            mascara1 = 1

        else:
            mascara1 = 0
            print("mascara não encontrado")

    else: 
        mascara1 = 2
        print("mascara desnecessário")

    print("----------------------------------")
    print("verificação do protetor auricular lado direito")

    ler = open(arquivonome, "r").readlines()[6]

    teste = open("cores_pa.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_pa.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_pa.txt", "r").readlines()[2]
    b3 = teste

    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_pa==1:
        ler = "nao"

    pa_sim = 0

    if ler == "protetor auricular\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 45
            for y in range(y, 105): #valor max = 70
                x = 270
                for x in range(x, 333): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 105:
                                    w = 104

                                z = x + 10
                                if z >=333:
                                    z = 332
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                
                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    pa_sim = 1

                                    break
                if pa_sim == 1:
                    print("pa encontrado")

                    break
        
            if pa_sim == 1:
                break

            if var == 2:
                break

        if pa_sim == 1:
            pa1 = 1

        else:
            pa1 = 0
            print("pa não encontrado")

    else: 
        pa1 = 2
        print("pa desnecessário")

    print("----------------------------------")
    print("verificação do protetor auricular lado esquerdo")

    pa_sim = 0

    if ler == "protetor auricular\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 45
            for y in range(y, 105): #valor max = 70
                x = 337
                for x in range(x, 395): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 4
                                if w >= 105:
                                    w = 104

                                z = x + 4
                                if z >=395:
                                    z = 395
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    pa_sim = 1

                                    break
                if pa_sim == 1:
                    print("pa encontrado")

                    break
        
            if pa_sim == 1:
            
                break
            if var == 2:
                break

        if pa_sim == 1:
            pa2 = 1

        else:
            pa2 = 0
            print("pa não encontrado")

    else: 
        pa1 = 2
        print("pa desnecessário")

    print("----------------------------------")
    print("verificação da camisa de segurança")
    
    ler = open(arquivonome, "r").readlines()[2]

    teste = open("cores_camisa.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_camisa.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_camisa.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)
    if var_camisa==1:
        ler = "nao"

    camisa_sim = 0

    if ler == "camisa\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 140
            for y in range(y, 200): #valor max = 70
                x = 250
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 20
                                if w >= 200:
                                    w = 199

                                z = x + 30
                                if z >=420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    camisa_sim = 1

                                    break
                if camisa_sim == 1:
                    print("camisa encontrado")

                    break
        
            if camisa_sim == 1:
            
                break
            if var == 2:
                break

        if camisa_sim == 1:
            camisa1 = 1

        else:
            camisa1 = 0
            print("camisa não encontrado")

    else: 
        camisa1 = 2
        print("camisa desnecessário")

    print("----------------------------------")
    print("verificação da cinto de segurança")

    ler = open(arquivonome, "r").readlines()[8]

    teste = open("cores_cinto.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_cinto.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_cinto.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_cinto==1:
        ler = "nao"

    cinto_sim = 0

    if ler == "cinto\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 250
            for y in range(y, 280): #valor max = 70
                x = 250
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 30
                                if w >= 280:
                                    w = 279

                                z = x + 30
                                if z >=420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                   for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    
                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    cinto_sim = 1

                                    break
                if cinto_sim == 1:
                    print("cinto encontrado")

                    break
        
            if cinto_sim == 1:
            
                break
            if var == 2:
                break

        if cinto_sim == 1:
            cinto1 = 1

        else:
            cinto1 = 0
            print("cinto não encontrado")

    else: 
        cinto1 = 2
        print("cinto desnecessário")

    print("----------------------------------")
    print("verificação da luva de segurança")

    ler = open(arquivonome, "r").readlines()[3]

    teste = open("cores_luvas.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_luvas.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_luvas.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_luva==1:
        ler = "nao"

    luva_sim = 0

    if ler == "luvas\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 215
            for y in range(y, 275): #valor max = 70
                x = 170
                for x in range(x, 230): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 270:
                                    w = 269

                                z = x + 10
                                if z >=230:
                                    z = 229
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    luva_sim = 1

                                    break
                if luva_sim == 1:
                    print("luva direita encontrado")

                    break
        
            if luva_sim == 1:
            
                break
            if var == 2:
                break

        luva_sim1 = 0
        var = 0
        while True: 
            var = var+ 1
            y = 215
            for y in range(y, 275): #valor max = 70
                x = 440
                for x in range(x, 500): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 270:
                                    w = 269

                                z = x + 10
                                if z >=500:
                                    z = 499
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    
                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    luva_sim1 = 1

                                    break
                if luva_sim1 == 1:
                    print("luva esquerda encontrado")

                    break
        
            if luva_sim1 == 1:
            
                break
            if var == 2:
                break

        if luva_sim == 1:
            luva1 = 1

        else:
            luva1 = 0
            print("luva direita não encontrado")

        if luva_sim1 == 1:
            luva2 = 1
    
        else:
            luva2 = 0
            print("luva esquerda não encontrado")

    else: 
        luva1 = 2
        print("luva desnecessário")


    print("----------------------------------")
    print("verificação da calca de segurança")

    ler = open(arquivonome, "r").readlines()[4]

    teste = open("cores_calca.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_calca.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_calca.txt", "r").readlines()[2]
    b3 = teste

    if var_calca==1:
        ler = "nao"

    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    calca_sim = 0

    if ler == "calca\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 340
            for y in range(y, 380): #valor max = 70
                x = 250
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 20
                                if w >= 380:
                                    w = 279

                                z = x + 20
                                if z >=420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    calca_sim = 1

                                    break
                if calca_sim == 1:
                    print("calca encontrado")

                    break
            
            if calca_sim == 1:
            
                break
            if var == 2:
                break

        if calca_sim == 1:
            calca1 = 1

        else:
            calca1 = 0
            print("calca não encontrado")

    else: 
        calca1 = 2
        print("calca desnecessário")

    print("----------------------------------")
    print("verificação da bota de segurança")

    ler = open(arquivonome, "r").readlines()[5]

    teste = open("cores_botas.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_botas.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_botas.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_bota==1:
        ler = "nao"

    bota_sim = 0

    if ler == "botas\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 390
            for y in range(y, 449): #valor max = 70
                x = 250
                for x in range(x, 330): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]
    
                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 448:
                                    w = 447

                                z = x + 10
                                if z >=330:
                                    z = 329
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    bota_sim = 1

                                    break
                if bota_sim == 1:
                    print("bota direita encontrado")

                    break
        
            if bota_sim == 1:
            
                break
            if var == 2:
                break

        bota_sim1 = 0
        var = 0
        while True: 
            var = var+ 1
            y = 390
            for y in range(y, 449): #valor max = 70
                x = 340
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 448:
                                    w = 447

                                z = x + 10
                                if z >= 420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    bota_sim1 = 1

                                    break
                if bota_sim1 == 1:
                    print("bota esquerda encontrado")

                    break
        
            if bota_sim1 == 1:
            
                break
            if var == 2:
                break

        if bota_sim == 1:
            bota1 = 1

        else:
            bota1 = 0
            print("bota direita não encontrado")

        if bota_sim1 == 1:
            bota2 = 1
    
        else:
            bota2 = 0
            print("bota esquerda não encontrado")

    else: 
        bota1 = 2
        bota2 = 2
        print("bota desnecessário")


    print("capacete = ", capacete1)
    print("mascara = ", mascara1)
    print("protetor auricular lado direito = ", pa1)
    print("protetor auricular lado esquerdo = ", pa2)
    print("camisa = ", camisa1)
    print("cinto = ", cinto1)
    print("luva direita = ", luva1)
    print("luva esquerda = ", luva2)
    print("calca = ", calca1)
    print("bota direita = ", bota1)
    print("bota esquerda = ", bota2)

    green = (0, 255, 0)
    red = (0, 0, 255)
    blue = (255, 0, 0)

    if capacete1 == 1:
        cv2.rectangle(video, (270,1), (400, 70), green, 2)#capacete
        arquivo_erro = open("erro.txt", "w")
        arquivo_erro.writelines("ok")   

    elif capacete1 == 0:
        cv2.rectangle(video, (270,1), (400, 70), red, 2)#capacete
        arquivo_erro = open("erro.txt", "w")
        arquivo_erro.writelines("nao")

    else:
        cv2.rectangle(video, (270,1), (400, 70), blue, 2)#capacete
        arquivo_erro = open("erro.txt", "w")
        arquivo_erro.writelines("1")

    if luva1 == 1:
        cv2.rectangle(video, (170, 215), (230, 275), green, 2)#luva1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif luva1 == 0:
        cv2.rectangle(video, (170, 215), (230, 275), red, 2)#luva1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (170, 215), (230, 275), blue, 2)#luva1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if luva2 == 1: 
        cv2.rectangle(video, (440, 215), (500, 275), green, 2)#luva2
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif luva2 == 0:
        cv2.rectangle(video, (440, 215), (500, 275), red, 2)#luva2
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (440, 215), (500, 275), blue, 2)#luva2
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    if pa2 == 1 or pa1 == 1:
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif pa2 == 0 and pa1 == 0:
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    if pa2 == 1:
        cv2.rectangle(video, (337, 45), (395, 105), green, 2)#pa2

    elif pa2 == 0:
        cv2.rectangle(video, (337, 45), (395, 105), red, 2)#pa2

    else:
        cv2.rectangle(video, (337, 45), (395, 105), blue, 2)#pa2

    if pa1 == 1:
        cv2.rectangle(video, (270, 45), (333, 105), green, 2)#pa1

    elif pa1 == 0:
        cv2.rectangle(video, (270, 45), (333, 105), red, 2)#pa1

    else:
        cv2.rectangle(video, (270, 45), (333, 105), blue, 2)#pa1

    if mascara1 == 1:
        cv2.rectangle(video, (315, 70), (355, 120), green, 2)#mascara
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif mascara1 == 0:
        cv2.rectangle(video, (315, 70), (355, 120), red, 2)#mascara
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        cv2.rectangle(video, (315, 70), (355, 120), blue, 2)#mascara
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if camisa1 == 1:
        cv2.rectangle(video, (250, 140), (420, 200), green, 2)#camisa
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif camisa1 == 0:
        cv2.rectangle(video, (250, 140), (420, 200), red, 2)#camisa
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        cv2.rectangle(video, (250, 140), (420, 200), blue, 2)#camisa
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if cinto1 == 1:
        cv2.rectangle(video, (250, 220), (420, 280), green, 2)#cinto
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif cinto1 == 0:
        cv2.rectangle(video, (250, 220), (420, 280), red, 2)#cinto
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        cv2.rectangle(video, (250, 220), (420, 280), blue, 2)#cinto
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if calca1 == 1:
        cv2.rectangle(video, (250, 340), (420, 380), green, 2)#calca
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif calca1 == 0:
        cv2.rectangle(video, (250, 340), (420, 380), red, 2)#calca
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (250, 340), (420, 380), blue, 2)#calca
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    if bota1 == 1:
        cv2.rectangle(video, (250, 390), (330, 449), green, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
        
    elif bota1 == 0:
        cv2.rectangle(video, (250, 390), (330, 449), red, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (250, 390), (330, 449), blue, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if bota2 == 1:
        cv2.rectangle(video, (340, 390), (420, 449), green, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif bota2 == 0:
        cv2.rectangle(video, (340, 390), (420, 449), red, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (340, 390), (420, 449), blue, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    arquivo_imagem = nomefunc + data_real + ".png"

    cv2.imwrite(arquivo_imagem, video)

    foto = cv2.imread(arquivo_imagem)

    cv2.destroyAllWindows()
    var_time = 0
    while var_time < 700:
        var_time = var_time + 1
        cv2.imshow("imagem", foto)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()
    
    if capacete1 == 0 or (luva1 == 0 and luva2 == 0) or (pa2 == 0 and pa1 == 0) or mascara1 == 0 or cinto1== 0 or camisa1 == 0 or calca1 == 0 or (bota1 == 0 and bota2 == 0):
        print("Erro")
        arduino.close()
        verifica_epi_func()
        
    else:
        print("tudo ok")
        sleep(1)
        variavel = 0
        while True:
            valor = 'c'                
            arduino.write(valor.encode())
            arduino.flush()
            if arduino.inWaiting()>0:
                print("valor recebido")
                break
            
        path_on_cloud = "imagens funcionarios/" + arquivo_imagem

        storage = firebase.storage()

        storage.child(path_on_cloud).put(arquivo_imagem)

        dados.child().update({"Arquivo": arquivo_imagem})

        dados.child().update({"Capacete": capacete1})
        dados.child().update({"Máscara": mascara1})
        dados.child().update({"Protetor auricular": pa1})
        dados.child().update({"Camisa": camisa1})
        dados.child().update({"Cinto": cinto1})
        dados.child().update({"Luva": luva1})

        oldAdress = 'C:/Users/danie/OneDrive/Área de Trabalho/projete_final-main/projete/'
        newAdress = 'C:/Users/danie/OneDrive/Área de Trabalho/armazenar/' 

        lista = os.listdir(oldAdress)

        lista_len = len(lista)
        x = 0

        while x < lista_len:

            caminhoCompleto_old = oldAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
            caminhoCompleto_new = newAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
            arquivo_certo = oldAdress + arquivo_imagem
            if caminhoCompleto_old == arquivo_certo:
                shutil.move(caminhoCompleto_old, caminhoCompleto_new) #módulo 'shutil.move()' move os arquivos
            x += 1

    arduino.close()

def verifica_epi_func():
    data = date.today()
    dia = data.day
    mes = data.month
    ano = data.year
    dia = str(dia)
    mes = str(mes)
    ano = str(ano)

    data_real = dia + "-" + mes + "-" + ano
    print(data_real)

    var_capacete = 0
    try:
        open("cores_capacete.txt")

    except:
        var_capacete = 1
    var_luva= 0
    try:
        open("cores_luvas.txt")

    except:
        var_luva = 1
    var_camisa = 0
    try:
        open("cores_camisa.txt")

    except:
        var_camisa=1
    var_mascara = 0
    try:
        open("cores_mascara.txt")

    except:
        var_mascara = 1
    var_bota=0

    try:
        open("cores_botas.txt")
    except:
        var_bota=1
    var_pa=0
    try:
        open("cores_pa.txt")

    except:
        var_pa=1
    var_cinto=0
    try:
        open("cores_cinto.txt")

    except:
        var_cinto=1
    var_calca=0
    try:
        open("cores_calca.txt")

    except:
        var_calca=1

    config = {

        "apiKey": "AIzaSyBeVBuTS5ZP_7czH3nk2rA6t_aH8vUECOA",
        "authDomain": "projete-2021.firebaseapp.com",
        "databaseURL": "https://projete-2021-default-rtdb.firebaseio.com",
        "projectId": "projete-2021",
        "storageBucket": "projete-2021.appspot.com",
        "messagingSenderId": "720238893966",
        "appId": "1:720238893966:web:9f612342c08fe31ea5a2df",
        "measurementId": "G-FWJH11ZF9M"

    }

    firebase = pyrebase.initialize_app(config)

    dados = firebase.database()

    ler_arquivo = open("nome_do_arquivo.txt","r").readlines()[0]
    ler_arquivo = str(ler_arquivo)
    ler_arquivo = ler_arquivo.rstrip("\n")

    print(ler_arquivo)

    arquivonome = ler_arquivo + ".txt"

    ser = serial.Serial("COM3", 9600)
    valor_botao = ser.readline()
    valor = int(valor_botao)
    ser.close()

    camera = cv2.VideoCapture(0)

    var = 0

    if valor == 1:
        black = (0, 0, 0)
        while var < 350:

            var = var + 1
            _, video = camera.read()

            video = imutils.resize(video, width=600)
            video = cv2.flip(video, 1)
            cv2.rectangle(video, (270,1), (400, 70), black, 1)#capacete
            cv2.rectangle(video, (315, 70), (355, 120), black, 1)#mascara
            cv2.rectangle(video, (270, 45), (333, 105), black, 1)#pa1
            cv2.rectangle(video, (337, 45), (395, 105), black, 1)#pa2
            cv2.rectangle(video, (250, 140), (420, 200), black, 1)#camisa
            cv2.rectangle(video, (250, 220), (420, 280), black, 1)#cinto
            cv2.rectangle(video, (250, 340), (420, 380), black, 1)#calca
            cv2.rectangle(video, (250, 390), (330, 449), black, 1)#bota1
            cv2.rectangle(video, (340, 390), (420, 449), black, 1)#bota2
            cv2.rectangle(video, (170, 215), (230, 275), black, 1)#luva1
            cv2.rectangle(video, (440, 215), (500, 275), black, 1)#luva2
    
            cv2.imshow("video", video)
            if cv2.waitKey(1) == ord("q"):
                break
    
        
    arduino = serial.Serial("COM3", 9600)

    nomefunc = open(arquivonome,"r").readlines()[0]

    print(nomefunc)
    nomefunc = str(nomefunc)

    nomefunc = nomefunc.rstrip("\n")
    print(nomefunc)

    dados.child().update({"Nome": nomefunc})

    print("verificação do capacete")

    ler = open(arquivonome, "r").readlines()[1]
    capacete = str(ler)
    print(capacete)

    teste = open("cores_capacete.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_capacete.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_capacete.txt", "r").readlines()[2]
    b3 = teste

    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_capacete==1:
        ler = "nao"

    capacete_sim = 0

    if ler == "capacete\n":
        var = 0
        while True: 
            var = var+ 1
            y = 1
            for y in range(y, 70): #valor max = 70
                x = 270
                for x in range(x, 400): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 20
                                if w >= 70:
                                    w = 69

                                z = x + 20
                                if z >=400:
                                    z = 399
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 20 and r > r3 - 20) and (g < g3 + 20 and g > g3 - 20) and (b > b3 - 20 and b < b3 + 20):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    capacete_sim = 1

                                    break
                if capacete_sim == 1:
                    print("Capacete encontrado")

                    break
        
            if capacete_sim == 1:
            
                break
            if var == 2:
                break

        if capacete_sim == 1:
            capacete1 = 1

        else:
            capacete1 = 0
            print("Capacete não encontrado")

    else: 
        capacete1 = 2
        print("capacete desnecessário")

    print("----------------------------------")
    print("verificação dados mascara")

    ler = open(arquivonome, "r").readlines()[7]

    teste = open("cores_mascara.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_mascara.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_mascara.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_mascara==1:
        ler = "nao"

    mascara_sim = 0

    if ler == "mascara\n":
        var = 0
        var2 = 0
        while True: 
            var = var + 1
            y = 70
            for y in range(y, 120): #valor max = 70
                x = 315
                for x in range(x, 355): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 130:
                                    w = 119

                                z = x + 10
                                if z >=355:
                                    z = 354
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    mascara_sim = 1

                                    break
                if mascara_sim == 1:
                    print("mascara encontrado")

                    break
        
            if mascara_sim == 1:
            
                break
            if var == 2:
                break

        if mascara_sim == 1:
            mascara1 = 1

        else:
            mascara1 = 0
            print("mascara não encontrado")

    else: 
        mascara1 = 2
        print("mascara desnecessário")

    print("----------------------------------")
    print("verificação do protetor auricular lado direito")

    ler = open(arquivonome, "r").readlines()[6]

    teste = open("cores_pa.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_pa.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_pa.txt", "r").readlines()[2]
    b3 = teste

    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_pa==1:
        ler = "nao"

    pa_sim = 0

    if ler == "protetor auricular\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 45
            for y in range(y, 105): #valor max = 70
                x = 270
                for x in range(x, 333): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 105:
                                    w = 104

                                z = x + 10
                                if z >=333:
                                    z = 332
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                
                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    pa_sim = 1

                                    break
                if pa_sim == 1:
                    print("pa encontrado")

                    break
        
            if pa_sim == 1:
                break

            if var == 2:
                break

        if pa_sim == 1:
            pa1 = 1

        else:
            pa1 = 0
            print("pa não encontrado")

    else: 
        pa1 = 2
        print("pa desnecessário")

    print("----------------------------------")
    print("verificação do protetor auricular lado esquerdo")

    pa_sim = 0

    if ler == "protetor auricular\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 45
            for y in range(y, 105): #valor max = 70
                x = 337
                for x in range(x, 395): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 4
                                if w >= 105:
                                    w = 104

                                z = x + 4
                                if z >=395:
                                    z = 395
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    pa_sim = 1

                                    break
                if pa_sim == 1:
                    print("pa encontrado")

                    break
        
            if pa_sim == 1:
            
                break
            if var == 2:
                break

        if pa_sim == 1:
            pa2 = 1

        else:
            pa2 = 0
            print("pa não encontrado")

    else: 
        pa1 = 2
        print("pa desnecessário")

    print("----------------------------------")
    print("verificação da camisa de segurança")
    
    ler = open(arquivonome, "r").readlines()[2]

    teste = open("cores_camisa.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_camisa.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_camisa.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)
    if var_camisa==1:
        ler = "nao"

    camisa_sim = 0

    if ler == "camisa\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 140
            for y in range(y, 200): #valor max = 70
                x = 250
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 20
                                if w >= 200:
                                    w = 199

                                z = x + 30
                                if z >=420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    camisa_sim = 1

                                    break
                if camisa_sim == 1:
                    print("camisa encontrado")

                    break
        
            if camisa_sim == 1:
            
                break
            if var == 2:
                break

        if camisa_sim == 1:
            camisa1 = 1

        else:
            camisa1 = 0
            print("camisa não encontrado")

    else: 
        camisa1 = 2
        print("camisa desnecessário")

    print("----------------------------------")
    print("verificação da cinto de segurança")

    ler = open(arquivonome, "r").readlines()[8]

    teste = open("cores_cinto.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_cinto.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_cinto.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_cinto==1:
        ler = "nao"

    cinto_sim = 0

    if ler == "cinto\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 250
            for y in range(y, 280): #valor max = 70
                x = 250
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 30
                                if w >= 280:
                                    w = 279

                                z = x + 30
                                if z >=420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                   for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    
                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    cinto_sim = 1

                                    break
                if cinto_sim == 1:
                    print("cinto encontrado")

                    break
        
            if cinto_sim == 1:
            
                break
            if var == 2:
                break

        if cinto_sim == 1:
            cinto1 = 1

        else:
            cinto1 = 0
            print("cinto não encontrado")

    else: 
        cinto1 = 2
        print("cinto desnecessário")

    print("----------------------------------")
    print("verificação da luva de segurança")

    ler = open(arquivonome, "r").readlines()[3]

    teste = open("cores_luvas.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_luvas.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_luvas.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_luva==1:
        ler = "nao"

    luva_sim = 0

    if ler == "luvas\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 215
            for y in range(y, 275): #valor max = 70
                x = 170
                for x in range(x, 230): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 270:
                                    w = 269

                                z = x + 10
                                if z >=230:
                                    z = 229
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    luva_sim = 1

                                    break
                if luva_sim == 1:
                    print("luva direita encontrado")

                    break
        
            if luva_sim == 1:
            
                break
            if var == 2:
                break

        luva_sim1 = 0
        var = 0
        while True: 
            var = var+ 1
            y = 215
            for y in range(y, 275): #valor max = 70
                x = 440
                for x in range(x, 500): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 270:
                                    w = 269

                                z = x + 10
                                if z >=500:
                                    z = 499
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    
                                        if (r < r3 + 30 and r > r3 - 30) and (g < g3 + 30 and g > g3 - 30) and (b > b3 - 30 and b < b3 + 30):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    luva_sim1 = 1

                                    break
                if luva_sim1 == 1:
                    print("luva esquerda encontrado")

                    break
        
            if luva_sim1 == 1:
            
                break
            if var == 2:
                break

        if luva_sim == 1:
            luva1 = 1

        else:
            luva1 = 0
            print("luva direita não encontrado")

        if luva_sim1 == 1:
            luva2 = 1
    
        else:
            luva2 = 0
            print("luva esquerda não encontrado")

    else: 
        luva1 = 2
        print("luva desnecessário")


    print("----------------------------------")
    print("verificação da calca de segurança")

    ler = open(arquivonome, "r").readlines()[4]

    teste = open("cores_calca.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_calca.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_calca.txt", "r").readlines()[2]
    b3 = teste

    if var_calca==1:
        ler = "nao"

    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    calca_sim = 0

    if ler == "calca\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 340
            for y in range(y, 380): #valor max = 70
                x = 250
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 20
                                if w >= 380:
                                    w = 279

                                z = x + 20
                                if z >=420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    calca_sim = 1

                                    break
                if calca_sim == 1:
                    print("calca encontrado")

                    break
            
            if calca_sim == 1:
            
                break
            if var == 2:
                break

        if calca_sim == 1:
            calca1 = 1

        else:
            calca1 = 0
            print("calca não encontrado")

    else: 
        calca1 = 2
        print("calca desnecessário")

    print("----------------------------------")
    print("verificação da bota de segurança")

    ler = open(arquivonome, "r").readlines()[5]

    teste = open("cores_botas.txt", "r").readlines()[0]
    r3 = teste
    teste = open("cores_botas.txt", "r").readlines()[1]
    g3 = teste
    teste = open("cores_botas.txt", "r").readlines()[2]
    b3 = teste


    r3 = int(r3)
    g3 = int(g3)
    b3 = int(b3)

    if var_bota==1:
        ler = "nao"

    bota_sim = 0

    if ler == "botas\n":
        var = 0
        var2 = 0
        while True: 
            var = var+ 1
            y = 390
            for y in range(y, 449): #valor max = 70
                x = 250
                for x in range(x, 330): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]
    
                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 448:
                                    w = 447

                                z = x + 10
                                if z >=330:
                                    z = 329
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    bota_sim = 1

                                    break
                if bota_sim == 1:
                    print("bota direita encontrado")

                    break
        
            if bota_sim == 1:
            
                break
            if var == 2:
                break

        bota_sim1 = 0
        var = 0
        while True: 
            var = var+ 1
            y = 390
            for y in range(y, 449): #valor max = 70
                x = 340
                for x in range(x, 420): 
            
                    (b, g, r) = video[y, x]
        
                    if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                        (b, g, r) = video[y, x + 2]

                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                            (b, g, r) = video[y, x + 4]

                            if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):
                            
                                pixel_sim = 0
                                pixel_nao = 0
                                num_pixel = 0

                                w = y + 10
                                if w >= 448:
                                    w = 447

                                z = x + 10
                                if z >= 420:
                                    z = 419
                        
                                for y in range(y, w):
                            
                                    for x in range(x, z):

                                        (b, g, r) = video[y, x]

                                        num_pixel = num_pixel + 1
                                    

                                        if (r < r3 + 40 and r > r3 - 40) and (g < g3 + 40 and g > g3 - 40) and (b > b3 - 40 and b < b3 + 40):

                                            pixel_sim = pixel_sim + 1

                                        else:
                                            pixel_nao = pixel_nao + 1

                                if (pixel_sim >= (0.6*num_pixel)):
                                    bota_sim1 = 1

                                    break
                if bota_sim1 == 1:
                    print("bota esquerda encontrado")

                    break
        
            if bota_sim1 == 1:
            
                break
            if var == 2:
                break

        if bota_sim == 1:
            bota1 = 1

        else:
            bota1 = 0
            print("bota direita não encontrado")

        if bota_sim1 == 1:
            bota2 = 1
    
        else:
            bota2 = 0
            print("bota esquerda não encontrado")

    else: 
        bota1 = 2
        bota2 = 2
        print("bota desnecessário")


    print("capacete = ", capacete1)
    print("mascara = ", mascara1)
    print("protetor auricular lado direito = ", pa1)
    print("protetor auricular lado esquerdo = ", pa2)
    print("camisa = ", camisa1)
    print("cinto = ", cinto1)
    print("luva direita = ", luva1)
    print("luva esquerda = ", luva2)
    print("calca = ", calca1)
    print("bota direita = ", bota1)
    print("bota esquerda = ", bota2)

    green = (0, 255, 0)
    red = (0, 0, 255)
    blue = (255, 0, 0)

    if capacete1 == 1:
        cv2.rectangle(video, (270,1), (400, 70), green, 2)#capacete
        arquivo_erro = open("erro.txt", "w")
        arquivo_erro.writelines("ok")   

    elif capacete1 == 0:
        cv2.rectangle(video, (270,1), (400, 70), red, 2)#capacete
        arquivo_erro = open("erro.txt", "w")
        arquivo_erro.writelines("nao")

    else:
        cv2.rectangle(video, (270,1), (400, 70), blue, 2)#capacete
        arquivo_erro = open("erro.txt", "w")
        arquivo_erro.writelines("1")

    if luva1 == 1:
        cv2.rectangle(video, (170, 215), (230, 275), green, 2)#luva1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif luva1 == 0:
        cv2.rectangle(video, (170, 215), (230, 275), red, 2)#luva1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (170, 215), (230, 275), blue, 2)#luva1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if luva2 == 1: 
        cv2.rectangle(video, (440, 215), (500, 275), green, 2)#luva2
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif luva2 == 0:
        cv2.rectangle(video, (440, 215), (500, 275), red, 2)#luva2
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (440, 215), (500, 275), blue, 2)#luva2
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    if pa2 == 1 or pa1 == 1:
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif pa2 == 0 and pa1 == 0:
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    if pa2 == 1:
        cv2.rectangle(video, (337, 45), (395, 105), green, 2)#pa2

    elif pa2 == 0:
        cv2.rectangle(video, (337, 45), (395, 105), red, 2)#pa2

    else:
        cv2.rectangle(video, (337, 45), (395, 105), blue, 2)#pa2

    if pa1 == 1:
        cv2.rectangle(video, (270, 45), (333, 105), green, 2)#pa1

    elif pa1 == 0:
        cv2.rectangle(video, (270, 45), (333, 105), red, 2)#pa1

    else:
        cv2.rectangle(video, (270, 45), (333, 105), blue, 2)#pa1

    if mascara1 == 1:
        cv2.rectangle(video, (315, 70), (355, 120), green, 2)#mascara
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif mascara1 == 0:
        cv2.rectangle(video, (315, 70), (355, 120), red, 2)#mascara
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        cv2.rectangle(video, (315, 70), (355, 120), blue, 2)#mascara
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if camisa1 == 1:
        cv2.rectangle(video, (250, 140), (420, 200), green, 2)#camisa
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif camisa1 == 0:
        cv2.rectangle(video, (250, 140), (420, 200), red, 2)#camisa
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        cv2.rectangle(video, (250, 140), (420, 200), blue, 2)#camisa
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if cinto1 == 1:
        cv2.rectangle(video, (250, 220), (420, 280), green, 2)#cinto
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif cinto1 == 0:
        cv2.rectangle(video, (250, 220), (420, 280), red, 2)#cinto
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")

    else:
        cv2.rectangle(video, (250, 220), (420, 280), blue, 2)#cinto
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if calca1 == 1:
        cv2.rectangle(video, (250, 340), (420, 380), green, 2)#calca
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")

    elif calca1 == 0:
        cv2.rectangle(video, (250, 340), (420, 380), red, 2)#calca
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (250, 340), (420, 380), blue, 2)#calca
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    if bota1 == 1:
        cv2.rectangle(video, (250, 390), (330, 449), green, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
        
    elif bota1 == 0:
        cv2.rectangle(video, (250, 390), (330, 449), red, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (250, 390), (330, 449), blue, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")
    if bota2 == 1:
        cv2.rectangle(video, (340, 390), (420, 449), green, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nok")
    elif bota2 == 0:
        cv2.rectangle(video, (340, 390), (420, 449), red, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\nnao")
    else:
        cv2.rectangle(video, (340, 390), (420, 449), blue, 2)#bota1
        arquivo_erro = open("erro.txt", "a")
        arquivo_erro.writelines("\n1")

    arquivo_imagem = nomefunc + data_real + ".png"

    cv2.imwrite(arquivo_imagem, video)

    foto = cv2.imread(arquivo_imagem)

    cv2.destroyAllWindows()
    var_time = 0
    while var_time < 700:
        var_time = var_time + 1
        cv2.imshow("imagem", foto)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()
    
    if capacete1 == 0 or (luva1 == 0 and luva2 == 0) or (pa2 == 0 and pa1 == 0) or mascara1 == 0 or cinto1== 0 or camisa1 == 0 or calca1 == 0 or (bota1 == 0 and bota2 == 0):
        print("Erro")

        path_on_cloud = "imagens funcionarios/" + arquivo_imagem

        storage = firebase.storage()
        print("cheguei aqui")

        storage.child(path_on_cloud).put(arquivo_imagem)

        dados.child().update({"Capacete": capacete1})
        dados.child().update({"Máscara": mascara1})
        dados.child().update({"Protetor auricular": pa1})
        dados.child().update({"Camisa": camisa1})
        dados.child().update({"Cinto": cinto1})
        dados.child().update({"Luva": luva1})
        dados.child().update({"Calca": calca1})
        dados.child().update({"Bota": bota1}) 
        dados.child().update({"Arquivo": arquivo_imagem})
        dados.child().update({"Problema": 1})
        sleep(3)
        dados.child().update({"Problema": 0})
        oldAdress = 'C:/Users/danie/OneDrive/Área de Trabalho/projete_final-main/projete/'
        newAdress = 'C:/Users/danie/OneDrive/Área de Trabalho/armazenar/' 

        lista = os.listdir(oldAdress)

        lista_len = len(lista)
        x = 0

        while x < lista_len:

            caminhoCompleto_old = oldAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
            caminhoCompleto_new = newAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
            arquivo_certo = oldAdress + arquivo_imagem
            if caminhoCompleto_old == arquivo_certo:
                shutil.move(caminhoCompleto_old, caminhoCompleto_new) #módulo 'shutil.move()' move os arquivos
            x += 1

        print("Aguarde")
        moment = datetime.now() 
        minutos = moment.minute
        segundos = moment.second

        segundo_inicial = segundos
        minuto_inicial = minutos
        variavel_tempo=0
        while True:
            var_aciona = dados.child("users").get()
            var_time = 0
            
            for var in var_aciona.each():
                moment = datetime.now() 
                minutos = moment.minute
                segundos = moment.second
                acionar = var.val()
                acionar = int(acionar)
                if acionar != 0:
                    if acionar == 1:
                        while var_time < 5:
                            var_time = var_time + 1
                            valor = 'c'        
                            arduino.write(valor.encode())
                            arduino.flush()
                            print("funcionário liberado")
                            if arduino.inWaiting()>0:                
                                break

                        sleep(3)
                        break

                    elif acionar == 2:
                        arduino.close()
                        print("Verificando novamente o funcionário...")
                        sleep(3)
                        verifica_epi_func()
                        break

                    elif acionar == 3:
                        print("Funcionario ", nomefunc, " aguarde...")
                        sleep(3)

                        break

                if (minutos == minuto_inicial + 1) and (segundos == segundo_inicial):
                    print("passou um minuto")
                    variavel_tempo = 1
                    break 

            if acionar == 1 or acionar == 2 or acionar == 3 or variavel_tempo==1:
                break 
        
    else:
        print("tudo ok")
        sleep(1)
        variavel = 0
        while True:
            valor = 'c'                
            arduino.write(valor.encode())
            arduino.flush()
            if arduino.inWaiting()>0:
                print("valor recebido")
                break
            
        path_on_cloud = "imagens funcionarios/" + arquivo_imagem

        storage = firebase.storage()

        storage.child(path_on_cloud).put(arquivo_imagem)

        dados.child().update({"Arquivo": arquivo_imagem})

        dados.child().update({"Capacete": capacete1})
        dados.child().update({"Máscara": mascara1})
        dados.child().update({"Protetor auricular": pa1})
        dados.child().update({"Camisa": camisa1})
        dados.child().update({"Cinto": cinto1})
        dados.child().update({"Luva": luva1})

        oldAdress = 'C:/Users/danie/OneDrive/Área de Trabalho/projete_final-main/projete/'
        newAdress = 'C:/Users/danie/OneDrive/Área de Trabalho/armazenar/' 

        lista = os.listdir(oldAdress)

        lista_len = len(lista)
        x = 0

        while x < lista_len:

            caminhoCompleto_old = oldAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
            caminhoCompleto_new = newAdress + lista[x] #variável recebe caminho + arquivo, conforme indice
            arquivo_certo = oldAdress + arquivo_imagem
            if caminhoCompleto_old == arquivo_certo:
                shutil.move(caminhoCompleto_old, caminhoCompleto_new) #módulo 'shutil.move()' move os arquivos
            x += 1

    arduino.close()

x = 0
for x in range(x, 4):
    
    ser = serial.Serial('COM3', 9600)

    dados = ser.readline()

    ser.close()

    cartao = dados.decode("utf-8")
    cartao = str(cartao)
    cartao = cartao.rstrip("\n")

    print(cartao)

    escreve = open("nome_do_arquivo.txt", "w")
    escreve.write(cartao)
    escreve.close()
    verifica_epi1()   

   

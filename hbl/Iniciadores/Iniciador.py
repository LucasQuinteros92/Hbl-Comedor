import os
from tkinter import Menu
from colorama import Fore , Style
import time
import json
import VerEstado

Folder_Iniciadores_Path  = "/usr/programas/hbl/Iniciadores/"
Folder_Logs_Path  = "/usr/programas/hbl/log/"
os.system("clear")




def MenuInformacion():

    print(Fore.MAGENTA + "********************************************")
    print("******      Menu de Informacion        *****")
    print(Fore.MAGENTA + "********************************************")
    print("\n")


    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del comando que desea ejecutar:\n")

    print(Fore.LIGHTBLUE_EX + "1) Informacion de version \n")
    print("2) Informacion de CPU \n")
    print("3) Medir Temperatura \n")
    print("4) Mostrar IP \n")
    print("5) Informacion de particiones \n")
    print("6) Informacion de RAM \n")
    print("7) Ver Fecha \n")
    print("8) Ver estado de programa \n")
    print("9) Volver al Menu Principal \n")

    InfoInput=int(input())

    print(Fore.LIGHTYELLOW_EX + "\n\n\n")
    if InfoInput==1:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Version_Info.sh")
    if InfoInput==2:
        os.system("sudo sh " + Folder_Iniciadores_Path + "CPU_Info.sh")
    if InfoInput==3:
        os.system("sudo sh " + Folder_Iniciadores_Path + "MedirTemperatura.sh")
    if InfoInput==4:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Mostrar_IP.sh")
    if InfoInput==5:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Particiones_Info.sh")
    if InfoInput==6:
        os.system("sudo sh " + Folder_Iniciadores_Path + "RAM_Info.sh")
    if InfoInput==7:
        os.system("sudo sh " + Folder_Iniciadores_Path + "VerFecha.sh")
    if InfoInput==8:
        VerEstado.EstadoPrograma()
        #os.system("sudo sh " + Folder_Iniciadores_Path + "VerEstado.sh")
    if InfoInput==9:
        os.system("clear")
        return 0
    

    print(Fore.LIGHTMAGENTA_EX + "\n\n\n" +"Ingrese 'ENTER' para volver al menu principal")
    input()
    os.system("clear")

def MenuComandos():
    print(Fore.MAGENTA + "********************************************")
    print("*******      Menu de Comandos        *******")
    print(Fore.MAGENTA + "********************************************")
    print("\n")


    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del comando que desea ejecutar:\n")

    print(Fore.LIGHTBLUE_EX + "1) Apagar \n")
    print("2) Reiniciar \n")
    print("3) Ocultar aviso de baja tension \n")
    ##print("4) Actualizar HBL \n")
    print("4) Volver al Menu Principal \n")

    CommandInput=int(input())

    print(Fore.LIGHTYELLOW_EX + "\n\n\n")
    if CommandInput==1:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Apagar.sh")
    if CommandInput==2:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Reiniciar.sh")
    if CommandInput==3:
        os.system("sudo sh " + Folder_Iniciadores_Path + "Ocultar_Aviso_Baja_Tension.sh")
    #if CommandInput==4:
    #    os.system("sudo sh " + Folder_Iniciadores_Path + "ActualizarHBL.sh")
    if CommandInput==4:
        os.system("clear")
        return 0
    

    print(Fore.LIGHTMAGENTA_EX + "\n\n\n" +"Ingrese 'ENTER' para volver al menu principal")
    input()
    os.system("clear")

def MenuLogs():
    print(Fore.MAGENTA + "********************************************")
    print("*********      Menu de Logs        *********")
    print(Fore.MAGENTA + "********************************************")
    print("\n")


    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del comando que desea ejecutar:\n")

    print(Fore.LIGHTBLUE_EX + "1) Todos \n")
    print("2) Cacheo \n")
    print("3) Conexiones \n")
    print("4) Core \n")
    print("5) Entradas \n")
    print("6) FTP \n")
    print("7) hidDevice \n")
    print("8) HTPP \n")
    print("9) I2C \n")
    print("10) Kiosco \n")
    print("11) Reporte \n")
    print("12) Serial \n")
    print("13) TCP \n")
    print("14) Wiegand \n")
    print("15) Volver al Menu Principal \n")

    LogInput=int(input())

    os.system("cd " + Folder_Logs_Path)

    print(Fore.LIGHTYELLOW_EX + "\n\n\n")
    if LogInput==1:
        os.system("sudo tail -f *")
    if LogInput==2:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblCacheo.log")
    if LogInput==3:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblConexiones.log")
    if LogInput==4:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblCore.log")
    if LogInput==5:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblEntradas.log")
    if LogInput==6:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblFTP.log")
    if LogInput==7:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblhidDevice.log")
    if LogInput==8:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblHTTP.log")
    if LogInput==9:
        os.system("sudo tail -f " + Folder_Logs_Path + "hbli2c.log")
    if LogInput==10:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblKiosco.log")
    if LogInput==12:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblReporte.log")
    if LogInput==13:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblSerial.log")
    if LogInput==14:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblTcp.log")
    if LogInput==15:
        os.system("sudo tail -f " + Folder_Logs_Path + "hblWiegand.log")
    if LogInput==16:
        os.system("clear")
        return 0
    

    print(Fore.LIGHTMAGENTA_EX + "\n\n\n" +"Ingrese 'ENTER' para volver al menu principal")
    input()
    os.system("clear")


def MenuConfiguracion():
    print(Fore.MAGENTA + "********************************************")
    print("******     Menu de Configuracion      ******")
    print(Fore.MAGENTA + "********************************************")
    print("\n")


    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del comando que desea ejecutar:\n")

    print(Fore.LIGHTBLUE_EX + "1) Setear fecha y hora RTC \n")
    print("2) Volver al Menu Principal \n")

    ConfInput=int(input())

    print(Fore.LIGHTYELLOW_EX + "\n\n\n")
    if ConfInput==1:
        dateInput= input("Ingrese la fecha y hora como indica el siguiente ejemplo 'jan 5 2016 23:09:40' y presione 'ENTER':\n")
        os.system("sudo date -s " + dateInput + " CLST")
        os.system("sudo hwclock -w")
    if ConfInput==2:
        os.system("clear")
        return 0
        
    print(Fore.LIGHTMAGENTA_EX + "\n\n\n" +"Ingrese 'ENTER' para volver al menu principal")
    input()
    os.system("clear")


def MenuJSON():
    print(Fore.MAGENTA + "********************************************")
    print("******    Menu de Configuracion       ******")
    print(Fore.MAGENTA + "********************************************")
    print("\n")

    file_path_JSON = '/usr/programas/hbl/modulos/hbl.json'
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
    with open(os.path.join(__location__ , file_path_JSON), "r") as f:
        data = json.load(f)
        f.close()
    
    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del comando que desea ejecutar:\n")

    print(Fore.LIGHTBLUE_EX + "1) JSON Completo \n")
    dict={}
    i=2
    for key in data:
        print(str(i) + ") " + key + "\n")
        dict[str(i)] = key
        i=i+1
    
    print(str(i) + ") " + "Volver al Menu Principal \n")

    ConfInput=int(input())

    print(Fore.LIGHTYELLOW_EX + "\n\n\n")

    if ConfInput == 1:
        print(json.JSONEncoder(indent=2).encode(data))
    if ConfInput>=2 and ConfInput<i:
        print(json.JSONEncoder(indent=2).encode(data[dict[str(ConfInput)]]))
    if ConfInput<=0 and ConfInput>=i:
        os.system("clear")
        return 0
        
    

    print(Fore.LIGHTMAGENTA_EX + "\n\n\n" +"Ingrese 'ENTER' para volver al menu principal")
    input()
    os.system("clear")


while 1:
    print(Fore.MAGENTA + "********************************************")
    print("********      Menu Principal        ********")
    print(Fore.MAGENTA + "********************************************")
    print("\n")
    print(Style.BRIGHT + Fore.GREEN + "Ingrese el numero del menu que desea ingresar:\n")

    print(Fore.LIGHTBLUE_EX + "1) Información \n")
    print("2) Comandos \n")
    print("3) Logs \n")
    print("4) Configuración \n")
    print("5) JSON \n")

    MenuInput=int(input())

    os.system("clear")

    


    if MenuInput==1:
        MenuInformacion()
    if MenuInput==2:
        MenuComandos()
    if MenuInput==3:
        MenuLogs()
    if MenuInput==4:
        MenuConfiguracion()
    if MenuInput==5:
        MenuJSON()



    
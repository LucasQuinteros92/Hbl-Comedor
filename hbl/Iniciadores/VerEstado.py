import time
def EstadoPrograma():
    myFile = open(r'C:\Users\Diego Scicchitano\Documents\Desarrollo HBL\hbl\Seguimiento.txt', 'r')
    texto=myFile.readline()
    texto=texto.replace(" ","")
    texto=texto.split("-")
    fecha=time.strftime("%d/%m/%y").replace(" ","")
    hora=time.strftime("%H").replace(" ","")
    minuto=time.strftime("%M").replace(" ","")
    if (fecha==texto[1]) and (hora==texto[2].split(":")[0]) and (int(minuto)-int(texto[2].split(":")[1])<=5):
        print("El HBL esta corriendo")
    else:
        print("El HBL NO esta corriendo")


EstadoPrograma()
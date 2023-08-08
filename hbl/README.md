## HBL  
 
--- 

### Instalación 


### **OS** [^first]

> Configuracion teclado y zona horaria, WLAN
> Habilitacion de modulos de hardware (I2C, Serie, etc) 
> Seleccion de USB como unidad de BOOT
``` 
sudo raspi-config
```

> Instalacion pip3
``` 
sudo apt-get install python3-pip 
```

> Instalacion pigpio
``` 
sudo pip3 install pigpio & sudo apt-get install pigpio
```
 
> DHCP + DNS

``` 
sudo apt-get install dnsmasq
```

---

### Dependencias de librerías segun módulo:

> hidDevice.py

``` 
**usb.core**
  
sudo pip3 install pyusb
sudo apt-get install python-usb python3-usb

```

> conexiones.py

```
sudo apt-get install wvdial
```

> hblCore.py (oled)

```
sudo pip3 install cbor2
sudo pip3 install smbus2
sudo pip3 install Pillow 
sudo apt-get install libopenjp2-7 
sudo apt install libtiff5 
```

---

### Ejecución


> Dar permisos de ejecución a los scripts de ejecucion

```
ej : sudo chmod +x start.sh
```

> Agregar a rc.local

```
sh /usr/programas/hbl/start.sh
``` 

---

### Scripts

> Inicializador de RPI - Actualizacion pkg Raspbian - Actualizacion EEPROM - Seteo huso horario - Instalacion GIT

```
./initHBL.sh
``` 

> Instalador de dependencias

```
./install.sh
``` 

> Start HBL

```
./start.sh
``` 

> Stop HBL y eliminacion de memoria de procesos python activos

```
./stop.sh
``` 

> Compartir la conexion 4G con Ethernet

```
./share4G.sh
``` 

> Dejar de compartir la conexion 4G con Ethernet

```
./NOTshare4G.sh
``` 


---

### Logs

> Ubicación de los logs del HBL

```
/usr/programas/hbl/log
```

> Ubicación de los logs historicos del HBL

```
/usr/programas/hbl/log/backup
```

---

### FTP

> Ubicación de la carpeta temporal para la compresion y envio de logs al FTP

```
/usr/programas/hbl/temp
```


---

#### Notas

---

[^first]: módulos instalables solo en versión lite de OS (sin desktop).
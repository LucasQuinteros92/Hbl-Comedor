#!/bin/sh
sudo su <<EOF
apt-get update && sudo apt-get upgrade -y
apt-get -y install python3-pip
apt-get install rpi-eeprom-update -y
pip3 install pigpio
apt-get install pigpio -y
pip3 install pyusb
apt-get install dnsmasq -y
apt-get install python-usb python3-usb -y
apt-get install wvdial -y 
pip3 install cbor2 
pip3 install smbus2
pip3 install Pillow
pip3 install websocket-client
apt-get install libopenjp2-7 -y
apt install libtiff5 -y
apt install git -y
apt-get install dialog -y
apt install jq  #Instala libreria para parsear el json
sudo apt-get install python3-paho-mqtt

# Descargo AnyDesk si no existe
if [ ! -e /home/pi/anydesk_6.1.1-1_armhf.deb ]; then
    echo "----------- Instalando AnyDesk -----------"
    wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | apt-key add -
    echo "deb http://deb.anydesk.com/ all main" > /etc/apt/sources.list.d/anydesk-stable.list
    apt update
    apt install anydesk
    echo Jphlionshbl | anydesk --set-password
    echo "----------- AnyDesk Instalado -----------"
fi



# Descargo la carpeta de git
if [ -e /usr/programas ]; then
    echo "----------- Borrando repositorio local -----------"    
    sudo rm -rfv /usr/programas  
    echo "----------- Repositorio local borrado -----------"      
fi
echo "----------- Clonando repositorio -----------"
mkdir /usr/programas
sudo git clone https://github.com/ScicchitanoJPH/Desarrollo-HBL.git /usr/programas    
echo "+++++++++++ Repositorio clonado ++++++++++++"





# Descargo Firefox
sudo apt install firefox-esr

# Configuracion POS-80
sudo chmod a+w /dev/usb/lp0
sudo apt-get install git cups
chmod u+x /usr/programas/POS-80/install.sh
sudo /usr/programas/POS-80/install.sh
sudo usermod -a -G lpadmin pi
sudo cupsctl --remote-any
sudo /etc/init.d/cups restart

timedatectl set-timezone America/Argentina/Buenos_Aires

# desactivacion del switch automatico del modem usb para poder realizarlo manualmente desde el hbl
awk '{sub("DisableSwitching=0","DisableSwitching=1")}1' /etc/usb_modeswitch.conf > temp.txt && mv temp.txt /etc/usb_modeswitch.conf --force

# forzado del hdmi para que inicie la raspberry sin la necesidad de tener conectado un monitor
awk '{sub("#hdmi_force_hotplug=1","hdmi_force_hotplug=1")}1' /boot/config.txt > /home/pi/temp.txt && mv /home/pi/temp.txt /boot/config.txt --force

# habilitacion del bus i2c
awk '{sub("#dtparam=i2c_arm=on","dtparam=i2c_arm=on")}1' /boot/config.txt > /home/pi/temp.txt && mv /home/pi/temp.txt /boot/config.txt --force

# habilitacion del bus spi
awk '{sub("#dtparam=spi=on","dtparam=spi=on")}1' /boot/config.txt > /home/pi/temp.txt && mv /home/pi/temp.txt /boot/config.txt --force

# habilita el modulo uart para la comunicacion Serial
echo "enable_uart=1" >> /boot/config.txt
 
# cambio de password
FIRSTUSER=`getent passwd 1000 | cut -d: -f1`
FIRSTUSERHOME=`getent passwd 1000 | cut -d: -f6`
echo "$FIRSTUSER:"'$5$v/ct2C0c4l$n0ewGbF1fmbMh66XrvHOBkVm5eN0D2CLLgwqxj8Hrt1' | chpasswd -e 

# seteo de propiedades de timezone y el layout del teclado
rm -f /etc/xdg/autostart/piwiz.desktop
rm -f /etc/localtime
echo "America/Buenos_Aires" >/etc/timezone
dpkg-reconfigure -f noninteractive tzdata
cat >/etc/default/keyboard <<'KBEOF'
XKBMODEL="pc105"
XKBLAYOUT="es"
XKBVARIANT=""
XKBOPTIONS=""
KBEOF
dpkg-reconfigure -f noninteractive keyboard-configuration  

# Realizar un backup de la configuración original
mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig




# editar archivo inicio /home/pi/.config/autostart/Start.desktop

if [ ! -e /home/pi/.config/autostart/Start.desktop ]; then
    echo "----------- Creando Autostart -----------"
    mkdir /home/pi/.config/autostart
    echo "[Desktop Entry]" >> /home/pi/.config/autostart/Start.desktop
    echo "Type=Application" >> /home/pi/.config/autostart/Start.desktop
    echo "Name=Start" >> /home/pi/.config/autostart/Start.desktop
    echo "Exec=sh /usr/programas/hbl/start.sh" >> /home/pi/.config/autostart/Start.desktop
    echo "----------- Autostart creado -----------"
fi


# Cambiar fondo de pantalla
if [ -e /usr/programas/FondoPantalla.jpg ]; then
    echo "----------- JPG -----------"
    pcmanfm --set-wallpaper /usr/programas/FondoPantalla.jpg     
fi
if [ -e /usr/programas/FondoPantalla.png ]; then
    echo "----------- PNG -----------"
    pcmanfm --set-wallpaper /usr/programas/FondoPantalla.png     
fi


reboot
EOF
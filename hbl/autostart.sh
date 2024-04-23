#!/bin/sh
dirExist(){
    if test -d $dir;then
        return 0
    else 
        return 1

    fi
}


crearDir() {
    
    if test -d $dir; then 
        echo "El directorio $dir ya existe"
        return 0
    else
        echo "El directorio $dir no existe"
        sudo mkdir -p $dir 
        if ! dirExist $1; then 
            echo "$dir no se pudo crear"
            exit 1
        fi
        
        echo "Se creo el directorio $dir"
        

    fi
}
crearAutostart(){
   filename="/home/pi/.config/autostart/Start.desktop"
   hblDir="/usr/programas/hbl/start.sh"
   dirActual="$PWD"
   
   echo
   echo Se creo $filename  
   #echo "#!/bin/bash" > $filename
   echo "[Desktop Entry]" > $filename
   echo Name=HBL >> $filename
   echo Type=Application >> $filename
   echo Exec=sudo sh $hblDir >> $filename
   #echo "Terminal=false" >> $filename
   cat $filename
   echo  
   #sudo chmod +x "$hblDir"
   #sudo chmod +x "$filename"
   echo
   
}
fileExist(){
    
    if test -f "Start.Desktop";then
        
        return 0
    else 
        
        return 1

    fi
}
desinstalar(){
    if dirExist $1; then 
        cd $dir
        
        if fileExist $1;then
            sudo rm -r Start.Desktop
        fi
        echo "Se desinstalo correctamente"
    else
        echo "El directorio $dir no existe"
    fi
}
menu(){
    echo "Uso: i instalar"
    echo "     u desinstalar"
}
cd 
cd /home/pi/.config
pwd
dir=autostart 

# Comprueba si se ha pasado exactamente un argumento
if [ "$#" -ne 1 ]; then
    menu
    exit 1
fi
arg="$1"

if [ "$arg" = "i" ];then
    echo instalando...
    crearDir
    cd $dir
    crearAutostart
    echo "Instalado"
elif [ "$arg" = "u" ];then
    desinstalar
else
    echo parametro desconocido
    menu
fi


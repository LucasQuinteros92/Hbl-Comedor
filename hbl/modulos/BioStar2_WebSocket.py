import websocket
import time
#import rel
import requests
import ssl
import json
from threading import Thread 
from modulos import hbl as hbl
from modulos import log as log
from modulos import variablesGlobales as vg
from modulos.timer import temporizador 

"""
    *Para usar la libreria de websocket, hay que instalar:
        pip install websocket-client
        pip install rel
    Si se comete el error de instalar el paquete de websocket, hacer lo siguiente:
        pip uninstall websocket
        pip uninstall websocket-client
        pip install websocket-client

    *Hay dos tipos de eventos:
        # IDENTIFY_SUCCESS_FINGERPRINT
        # VERIFY_SUCCESS_CARD
"""

        
class BioStar2_WebSocket(object):
    def __init__(self) :
        if hbl.BioStar2_WebSocket_activado:
            #websocket.enableTrace(True)
            self.temporizadorSinEventos = temporizador(segundos=hbl.BioStar2_WebSocket_TiempoPermitidoSinEventos,
                                                       name="tempSinEventosWebsocket",
                                                       callback=self.cb)
            self.conectar()
    def __run(self):
    
        self.ws.run_forever(reconnect=5,
                            ping_interval=hbl.BioStar2_WebSocket_TiempoEntreReconexiones/3,
                            ping_timeout= hbl.BioStar2_WebSocket_TiempoEntreReconexiones/4, 
                            sslopt={"cert_reqs": ssl.CERT_NONE})  
              
    def cb(self):

        self.ws.close()
        #self.reconectarSiEsNecesario()
        #self.temporizadorSinEventos.start()
        log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
        log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket, "Tiempo sin eventos superado")
        
            
        
    def conectar(self):
        try:
            self.connected = False
            
            self.reRun = hbl.BioStar2_WebSocket_Reconectar

            self.ws = websocket.WebSocketApp(hbl.BioStar2_WebSocket_WebSocket_Host + '/wsapi',
                                                on_open=self.on_open,
                                                on_message=self.on_message,
                                                on_error=self.on_error,
                                                on_close=self.on_close)
            
            self.t = Thread( target=self.__run, daemon=False,name ="hblBiostarWeb")
            self.t.start()
        except Exception as e:
            log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Conexion no establecida")

    def on_open(self,ws):
        try:
            self.SuscribirseAEventos()
            log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket, "Conexion establecida")
            self.connected = True
            
            self.temporizadorSinEventos.start()
        except Exception as e:
            log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket, "Error al iniciar sesion")
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,str(e))

    def SuscribirseAEventos(self):
        bs_session_id = self.Get_bs_session_id()
        self.ws.send('bs-session-id' + "=" + bs_session_id)
        self.Inicializar_Eventos(bs_session_id)

    def Get_bs_session_id(self):
        url = hbl.BioStar2_WebSocket_Api_Host + '/api/login'
        payload = "{\r\n    \"User\": {\r\n        \"login_id\": \"" + hbl.BioStar2_WebSocket_BioStar2_User + "\",\r\n        \"password\": \"" + hbl.BioStar2_WebSocket_BioStar2_Password + "\"\r\n    }\r\n}"
        headers = {}
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        
        response = requests.request("POST", url, headers=headers, data=payload,verify=False, timeout= 5)
        bs_session_id = response.headers['bs-session-id']

        #print(bs_session_id)
        return bs_session_id
    
    def Inicializar_Eventos(self, bs_session_id):
        url = hbl.BioStar2_WebSocket_Api_Host + '/api/events/start'
        payload = "{\r\n    \"User\": {\r\n        \"login_id\": \"" + hbl.BioStar2_WebSocket_BioStar2_User + "\",\r\n        \"password\": \"" + hbl.BioStar2_WebSocket_BioStar2_Password + "\"\r\n    }\r\n}"
        headers = {"bs-session-id" : bs_session_id}
        requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
        response = requests.request("POST", url, headers=headers, data=payload,verify=False, timeout= 5)
        #print(response.text)
        time.sleep(4)
        
    def on_message(self, ws, message):
        self.temporizadorSinEventos.stop()
        self.temporizadorSinEventos.start()
        message_json = json.loads(message)

        event_type_name = message_json["Event"]["event_type_id"]["name"]
        device_id = message_json["Event"]["device_id"]["id"]
        device = self.CoincidenciaDeEquipo(device_id)  
        event = self.CoincidenciaDeEvento(event_type_name)
        #log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
        #log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,str(message_json))
            
        if event and device:
            log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Tipo de evento : " + event_type_name)
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Device ID : " + device_id)
            id = message_json["Event"]["user_id"]["user_id"]
            vg.WebSock_User_id = id
            vg.WebSock_Device_id = device_id
            vg.WebSock_Event = event_type_name
            vg.WebSock_Data = id
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"ID : " + id)
          
    def CoincidenciaDeEquipo(self,device_id):
        if device_id == hbl.BioStar2_WebSocket_Device_ID1:
            return True
        elif device_id == hbl.BioStar2_WebSocket_Device_ID2:
            return True
        elif device_id == hbl.BioStar2_WebSocket_Device_ID3:
            return True
        elif device_id == hbl.BioStar2_WebSocket_Device_ID4:
            return True
        else:
            return False
    
    def CoincidenciaDeEvento(self, event):
        for i in hbl.BioStar2_WebSocket_Tipo_Evento: 
            if i == event:
                return True
        return False
    
    def on_error(self,ws, error):
        self.connected = False 
        #log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Error : " + str(error))
        #self.ws.ping_timeout = 3
        #self.ws.ping_interval = 5
        ##f str(error) == "ping/pong timed out" or str(error) == "[Errno 113] No route to host":
        #time.sleep(2)
        if str(error) != "'Event'":
            log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
            log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"ERROR : " + str(error))
        if str(error) == "ping/pong timed out" or str(error) == "[Errno 113] No route to host":
            self.ws.close()
            self.temporizadorSinEventos.stop()
            self.reconectarSiEsNecesario()

    def reconectarSiEsNecesario(self):
        if self.reRun:
                log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
                log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"Reconeccion en "+ str(hbl.BioStar2_WebSocket_TiempoEntreReconexiones) + "segundos")
                time.sleep(hbl.BioStar2_WebSocket_TiempoEntreReconexiones)
                self.conectar()
                
                

    def on_close(self,ws, close_status_code, close_msg):
        self.temporizadorSinEventos.stop()
        self.connected = False
        log.escribeSeparador(hbl.LOGS_hblBioStar2_WebSocket)
        log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"CLOSED")
        self.reconectarSiEsNecesario()

    def on_data(self,arg1,arg2,arg3):
        log.escribeLineaLog(hbl.LOGS_hblBioStar2_WebSocket,"DATA NUEVA")

    def stop(self):
        if hbl.BioStar2_WebSocket_activado:
            self.reRun = False
            self.temporizadorSinEventos.close()   
            self.ws.close()
            
from threading import Thread
import modulos.variablesGlobales as vg
import requests
import random, time
import modulos.hbl as hbl
import modulos.log as log


class requestnblck(object):
    def __init__(self, dni, urlseleccion) -> None:
        if hbl.REQ_activado == 0:
            self.__running = False
            self.dni = dni
            self.urlseleccion = urlseleccion
            
            if self.urlseleccion == 1:
                self.UrlCompletaReq = hbl.REQ_urlRequest1 + str(dni)
            elif self.urlseleccion == 2:
                self.UrlCompletaReq = hbl.REQ_urlRequest2 + str(dni)
            elif self.urlseleccion == 3:
                self.UrlCompletaReq = hbl.REQ_urlRequest3 + str(dni)
            elif self.urlseleccion == 4:
                self.UrlCompletaReq = hbl.REQ_urlRequest4 + str(dni)
            elif self.urlseleccion == 5:
                self.UrlCompletaReq = hbl.REQ_urlRequest5 + str(dni)
            else:
                self.UrlCompletaReq = "http://www.google.com"
            
            
            self.t = Thread(target=self.__run, daemon=False)
            
    def is_running(self):
        return self.__running
    
    def start(self):
        self.__running = True
        self.t.start()
        
    def pause(self):
        self.is_running = False
    
    def __run(self):
        
        try:
            #time.sleep(random.randint(5,9))
            req = requests.get(self.UrlCompletaReq, timeout=int(hbl.REQ_timeoutRequest))
            self.__Logreport("request exitoso:"+ str(self.UrlCompletaReq) +str(req) )
            
        except Exception as e:
            self.__Logreport("Error al intentar hacer req: "+ str(e))
            '''if self.urlseleccion == 1:
                vg.LastID1 = ""
            elif self.urlseleccion == 2:
                vg.LastID2 = ""
            elif self.urlseleccion == 3:
                vg.LastID3 = ""
            elif self.urlseleccion == 4:
                vg.LastID4 = ""'''
                
                
    def __Logreport(self,texto):
        log.escribeSeparador(hbl.LOGS_hblReqNoBlck)
        log.escribeLineaLog(hbl.LOGS_hblReqNoBlck,texto)
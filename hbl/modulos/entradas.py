
import pigpio
import datetime 
import time

from modulos import log as log
import modulos.variablesGlobales as VG
from modulos import hbl as hbl
#from modulos import cacheo as cacheo
#from picamera import PiCamera
from datetime import datetime


 
""" --------------------------------------------------------------------------------------------


   Clase entradas hbl


-------------------------------------------------------------------------------------------- """

class Entradas(object): 

    def __init__(self, pi, in1 = VG.Pin_Entrada1
                         , in2 = VG.Pin_Entrada2
                         , in3 = VG.Pin_Entrada3
                         , in4 = VG.Pin_Entrada4
                         , in5 = None
                         , in6 = None
                         , callback1 = None
                         , callback2 = None
                         , callback3 = None
                         , callback4 = None
                         , callback5 = None
                         , callback6 = None):

        self.pi : pigpio.pi = pi
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
        self.in4 = in4
        self.in5 = in5
        self.in6 = in6

        self.callback1 = callback1
        self.callback2 = callback2 
        self.callback3 = callback3 
        self.callback4 = callback4
        self.callback5 = callback5
        self.callback6 = callback6
        
        self.pi.set_mode(in1, pigpio.INPUT)
        self.pi.set_mode(in2, pigpio.INPUT)
        self.pi.set_mode(in3, pigpio.INPUT)
        self.pi.set_mode(in4, pigpio.INPUT)

        if in5 is not None: 
            self.pi.set_mode(in5, pigpio.INPUT) 
            #self.pi.set_pull_up_down(in5,pigpio.PUD_UP)
        if in6 is not None:
            self.pi.set_mode(in6, pigpio.INPUT) 
            #self.pi.set_pull_up_down(in6,pigpio.PUD_UP)
            
        
        
        self.setCallbacks()

        log.escribeSeparador(hbl.LOGS_hblEntradas)
        log.escribeLineaLog(hbl.LOGS_hblEntradas,"Entradas Inicializadas")
        
    def setCallbacks(self):

        if self.callback1 is not None:
            self.in1 = self.pi.callback(self.in1, pigpio.FALLING_EDGE, self.callback1)
        else:
            self.in1 = self.pi.callback(self.in1, pigpio.FALLING_EDGE, self.callbackIN1)
        
        if self.callback2 is not None:
            self.in2 = self.pi.callback(self.in2, pigpio.FALLING_EDGE, self.callback2)
        else:
            self.in2 = self.pi.callback(self.in2, pigpio.FALLING_EDGE, self.callbackIN2)
            
        if self.callback3 is not None:
            self.in3 = self.pi.callback(self.in3, pigpio.EITHER_EDGE, self.callback3)
        else:
            self.in3 = self.pi.callback(self.in3, pigpio.EITHER_EDGE, self.callbackIN3)
        
        if self.callback4 is not None:
            self.in4 = self.pi.callback(self.in4, pigpio.FALLING_EDGE, self.callback4)
        else:
            self.in4 = self.pi.callback(self.in4, pigpio.FALLING_EDGE, self.callbackIN4)
            
        if self.in5 is not None:
            if self.callback5 is not None:
                self.in5 = self.pi.callback(self.in5, pigpio.FALLING_EDGE, self.callback5)
            else:
                self.in5 = self.pi.callback(self.in5, pigpio.FALLING_EDGE, self.callbackIN5)
        
        if self.in6 is not None:
            if self.callback6 is not None: 
                self.in6 = self.pi.callback(self.in6, pigpio.FALLING_EDGE, self.callback6)  
            else:
                self.in6 = self.pi.callback(self.in6, pigpio.FALLING_EDGE, self.callbackIN6)  


    # ***************************************************************************************

    #   callback interrupcion entrada 1 HBL

    # ***************************************************************************************    
    
    def callbackIN1(self, gpio, level, tick): 

        diff = pigpio.tickDiff(VG.pressTick, tick)

        #log.escribeSeparador(hbl.LOGS_hblEntradas) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "VG.pressTick : " + str(VG.pressTick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff))  

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "IN1")
            print("IN1")
            VG.flagRequest = True 
            
    
    # ***************************************************************************************

    #   callback interrupcion entrada 2 HBL

    # ***************************************************************************************

    def callbackIN2(self, gpio, level, tick):  
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        #log.escribeSeparador(hbl.LOGS_hblEntradas) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "VG.pressTick : " + str(VG.pressTick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "IR2") 

             
    def callbackIN3(self, gpio, level, tick):  
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        #log.escribeSeparador(hbl.LOGS_hblEntradas) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "VG.pressTick : " + str(VG.pressTick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay:
            
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "Puerta abierta")
           

    
    def callbackIN4(self, gpio, level, tick):  
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        #log.escribeSeparador(hbl.LOGS_hblEntradas) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "VG.pressTick : " + str(VG.pressTick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas) 
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "P2_CERRADO") 


    def callbackIN5(self, gpio, level, tick):  
 
        diff = pigpio.tickDiff(VG.pressTick, tick)

        #log.escribeSeparador(hbl.LOGS_hblEntradas) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "VG.pressTick : " + str(VG.pressTick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > hbl.DIG_in_pushDelay: 
            log.escribeSeparador(hbl.LOGS_hblEntradas)
            log.escribeLineaLog(hbl.LOGS_hblEntradas,"ORDEN_DE_ACTIVAR_P1" ) 

                                                    
    def callbackIN6(self, gpio, level, tick):  
        
        diff = pigpio.tickDiff(VG.pressTick, tick)

        #log.escribeSeparador(hbl.LOGS_hblEntradas) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "VG.pressTick : " + str(VG.pressTick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "tick : " + str(tick)) 
        #log.escribeLineaLog(hbl.LOGS_hblEntradas, "Diff : " + str(diff)) 

        VG.pressTick = tick

        if diff > (hbl.DIG_in_pushDelay): #10*hbl.DIG_in_pushDelay
            log.escribeSeparador(hbl.LOGS_hblEntradas) 
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "ORDEN_DE_ACTIVAR_P2") 
            '''
            try:
                camera = PiCamera()
                camera.resolution = (640,480)
                camera.start_preview()
                time.sleep(2)
                
                now = datetime.now()
                dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
                camera.start_recording("Videos/" + dt_string + ".h264")
                time.sleep(5)
                camera.stop_recording()
                camera.close()
            except Exception as e:
                log.escribeSeparador(hbl.LOGS_hblEntradas) 
                log.escribeLineaLog(hbl.LOGS_hblEntradas, e) 
            '''

        

        
 

    @staticmethod
    def readPin(pi, pin):
        valorPin = pi.read(pin)
        return valorPin

 
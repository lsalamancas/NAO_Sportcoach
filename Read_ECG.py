import csv
import sys
import serial
import struct
import time
import threading
import sensors
import logging
import win32com.client as comclt
from naoqi import ALProxy
from movements_sportcoach import ip

logging.basicConfig(level = logging.DEBUG, format = '[%(levelname)s] (%(threadName)-9s) %(message)s',)

class EcgSensor(sensors.sensor):
    def __init__(self, port = "/dev/rfcomm0",name_csv = "Ecg_Data.csv",sample = 1):
        super(EcgSensor, self).__init__(sample_time = sample,name = "Ecg-thread",header_file ="fid, fiv, hid, hiv, batt, hr, hbn, hbts1, hbts2, hbts3, hbts4, hbts5, hbts6, hbts7, hbts8, hbts9, hbts10, hbts11, hbts12, hbts13, hbts14, hbts15, distance, speed, strides",file_name = name_csv)
        #defining the serial port that will be used.
        self.__ser=serial.Serial(port, 115200, timeout=1)
        #Flag used to check the synchronization.
        self.__async=False
        #Variables used in the zephyr's serial protocol.
        self.__stx = struct.pack("<B", 0x02)
        self.__etx = struct.pack("<B", 0x02)
        self.__rate = struct.pack("<B", 0x26)
        self.__dlc_byte = struct.pack("<B", 55)
        #Array where the EKG data will be saved.
        self.__data_temp=[]
        #Flag that is used in case of pause.
        self.__pause=True
        self.sample_time=sample
        self.lock = threading.Lock()
        """
        *********************************************************************************************
        *********************************************************************************************
        *** Override of the [sensor]'s process method, in this case [process] is a controlled and ***
        *** infinite loop which interacts with the serial port that is assigned after linking the ***
        *** bluetooth devices.                                                                    ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def process(self):
        while self.go_on:
            if not self.__pause:
                try:
                    d = self.__ser.read()
                    #print(str(d))
                    if d != self.__stx:
                        if not self.__async:
                            print >>sys.stderr, "Not synched"
                            self.__async = True
                        continue

                    self.__async = False
                    type = self.__ser.read()	# Msg ID
                    if type != self.__rate:
                        print >>sys.stderr, "Unknown message type"
                    dlc = self.__ser.read()	# DLC
                    len, = struct.unpack("<B", dlc)
                    if len != 55:
                        print >>sys.stderr, "Bad DLC"
                    payload = self.__ser.read(len)
                    crc, = struct.unpack("<B", self.__ser.read())
                    end, = struct.unpack("<B", self.__ser.read())
                    sum = 0
                    #print "L: " + str(len)

                    for i in xrange(len):
                        b, = struct.unpack("<B", payload[i])
                        #print "Data: 0x%02x" % b
                        sum = (sum ^ b) & 0xff
                        for j in xrange(8):
                            if sum & 0x01:
                                sum = (sum >> 1) ^ 0x8c
                            else:
                                sum = (sum >> 1)
                    #print "CRC:  0x%02x" % crc
                    if crc != sum:
                        print >>sys.stderr, "Bad CRC: " + str(sum) + " is not " + str(crc)
                    else:
                        pass #print "CRC validated!"
                    if end != 0x03:
                        print >>sys.stderr, "Bad ETX"

                    #Saving data into the backup file.
                    with self.lock:
                        self.__data_temp=list(struct.unpack("<H2sH2sBBB15H6xHHB3x", payload))

                    self.val=reduce(lambda a,b:str(a)+','+str(b),self.__data_temp)+'\n'
                    self.load_data(self.val)
                    time.sleep(self.sample_time)
                except:
                    print("problems with ECG acquisition ")
                    pass
            else:
                time.sleep(1)
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [pause] method changes the [__pause] flag, which means that the thread will be    ***
        *** paused until the flag is changed to a False value.                                    ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def pause(self):
        self.__pause=True
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [play] method changes the [__pause] flag, which means that the thread will run    ***
        *** until the flag is changed to a True value.
        *********************************************************************************************
        *********************************************************************************************
        """
    def play(self):
        self.__pause=False
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [close] method is used to close the serial port that is being used.               ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def close(self):
        self.shutdown()
        self.__ser.close()
        """
        *********************************************************************************************
        *********************************************************************************************
        *** The [get_data] method is used to return the data collected by the Zephyr sensor.      ***
        *********************************************************************************************
        *********************************************************************************************
        """
    def get_data(self):
        return self.__data_temp

    def Sleep(self):
        self.pause()

    def WakeUp(self):
        self.play()


def start_hxm():
    global ecg  
    ecg = EcgSensor(port='COM10',name_csv = 'Ecg_Data_prueba.csv' )    #change COM port and file's name
    ecg.start() 
    ecg.play()


def get_hr():
    datos = ecg.get_data()
    #print(len(datos))
    while len(datos)== 0:
        datos = ecg.get_data()
	#logging.debug(ecg.get_data())
    return datos[5]


def stop_hxm():
    ecg.close()


def check_hr(frec_cardiac_40,frec_cardiac_70,hr,l_t):
    file = open('tiempo_intervalos.csv', 'ab')
    writer = csv.writer(file)
    if (hr < frec_cardiac_40):
        print("La actual", hr , "Hr 40", frec_cardiac_40)
        tts = ALProxy("ALTextToSpeech", ip(), 9559) 
        tts.say("Vamos a subir el ritmo")
        leds = ALProxy("ALLeds",ip(),9559)
        #leds = ALProxy("ALLeds","192.168.0.102",9559)
        leds.on("AllLedsBlue")
        for _ in range(5):
            wsh = comclt.Dispatch("WScript.Shell")
            wsh.AppActivate('Reaper.exe') 
            wsh.SendKeys("^i")
        writer.writerow(['menor',str(l_t)+ 's'])

    elif (hr > frec_cardiac_70):
        print("La actual", hr , "Hr 70", frec_cardiac_70)
        tts = ALProxy("ALTextToSpeech", ip(), 9559) 
        tts.say("Reduce el ritmo")
        leds = ALProxy("ALLeds",ip(),9559)
        leds.off("AllLeds")
        leds = ALProxy("ALLeds",ip(),9559)
        leds.on("AllLedsRed")
        for _ in range(5):
            wsh = comclt.Dispatch("WScript.Shell")
            wsh.AppActivate('Reaper.exe') 
            wsh.SendKeys("^-")
        writer.writerow(['mayor',str(l_t) + 's'])
		# --------------------------------------------------------------------------------------------------------
    else:
        print("La actual", hr)
        tts = ALProxy("ALTextToSpeech", ip(), 9559) # cambiar el ip adress
        tts.say("Continua asi, ZONA DE EJERCICIO")
        leds = ALProxy("ALLeds",ip(),9559)
        leds.off("AllLeds")
        leds = ALProxy("ALLeds",ip(),9559)
        leds.on("AllLedsGreen")
        writer.writerow(['normal', str(l_t) + 's'])
        #leds.off()



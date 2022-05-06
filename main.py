import time
import numpy as np
import win32com.client as comclt
from threading import *
from Read_ECG import *
from movements_sportcoach import *
from naoqi import ALProxy

def hr_rest():
	v_hr_rest = np.empty((100,0),dtype=float)
	t_total = time.time() + 60*3  
	while time.time() < t_total: 
		v_hr_rest = np.append(v_hr_rest,get_hr())
		time.sleep(0.1)
	return np.mean(v_hr_rest)


def user_data():
	global hr_40,hr_70, p_name
	tts = ALProxy("ALTextToSpeech", ip(), 9559)
	tts.say('Hola como te llamas')
	p_name = raw_input('Ingrese el nombre: ')
	tts.say('cuantos anios tienes')
	age = raw_input('Ingrese la edad: ')
	tts.say('Mantente en reposo durante 3 minutos, por favor')
	rest_hr = hr_rest()
	print(rest_hr) #need save this in a file
	max_hr = 208 - (0.7*int(age))
	hr_40 = rest_hr + 0.4*(max_hr-rest_hr)
	hr_70 = rest_hr + 0.7*(max_hr-rest_hr)


def beginning():
	tts = ALProxy("ALTextToSpeech", ip(), 9559)
	tts.say("Hola" + p_name+ "bienvenido a la prueba")
	tts.say("Se que lo haras muy bien")
	tts.say("3")
	tts.say("2")
	tts.say("1")
	tts.say("ya!")
	wsh = comclt.Dispatch("WScript.Shell")
	wsh.AppActivate('Reaper.exe') 
	wsh.SendKeys("{ENTER}")


def session(excs):    
	t_time =  time.time() + 30	
	m_hr = np.empty((100,0))
	while time.time() < t_time:
		m_hr = np.append(m_hr,get_hr()) 
		if excs == 'BM':
			basicmarching()
		if excs == 'SU':
			stepup()
		if excs == 'LK':
			lateralqnees()
		if excs == 'BAF':
			botharms_forward()		
	c_t = time.time()
	check_hr(hr_40,hr_70,np.mean(m_hr),round(c_t-t_i,3))		

#WARMING UP  

def f_calentamiento():	
	tts = ALProxy("ALTextToSpeech", ip(), 9559) 
	tts.say("Empecemos con marcha basica")
	session('BM') 
	session('BM')
	tts.say("Vamos con estep ap")
	session('SU') 
	session('SU') 
	
# CONDITIONING

def f_acondicionamiento():	
	tts = ALProxy("ALTextToSpeech", ip(), 9559) 
	tts.say("Empecemos con marcha basica")
	session('BM') 
	session('BM') 
	tts.say("Ahora vamos con rodillas laterales")
	session('LK') 
	session('LK') 
	tts.say("Volvamos con marcha basica")
	session('BM') 
	session('BM') 
	tts.say("Sigamos con ambos brazos al frente")
	session('BAF')
	session('BAF')
	tts.say("Nuevamente con marcha basica")
	session('BM') 
	session('BM') 
	tts.say("Ya casi acabamos, vamos con rodillas laterales")
	session('LK') 
	session('LK') 
	tts.say("Vamos con marcha basica")
	session('BM') 
	session('BM') 

#COOLING

def f_enfriamiento():
	tts = ALProxy("ALTextToSpeech", ip(), 9559) 
	tts.say("Terminemos con marcha basica")
	session('BM') 
	session('BM') 


def main():
	global t_i
	start_hxm()
	user_data()
	beginning()
	t_i = time.time()
	for fase in range(3):
		if(fase==1):
			tts = ALProxy("ALTextToSpeech", ip(), 9559) 
			tts.say("Fase de calentamiento")
			print("CALENTAMIENTO*")
			f_calentamiento()
		if(fase==2):
			tts = ALProxy("ALTextToSpeech", ip(), 9559) 
			tts.say("Fase de acondicionamiento")
			print("ACONDICIONAMIENTO*")
			f_acondicionamiento()
		if(fase==3):
			tts = ALProxy("ALTextToSpeech", ip(), 9559) 
			tts.say("Fase de enfriamiento")
			print("ENFRIAMIENTO**")
			f_enfriamiento()
	stop_hxm()
		

if __name__ == '__main__':
	main()
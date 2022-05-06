from naoqi import ALProxy

#Change NAO ip

def ip():
	return "10.10.20.131"

def botharms_forward():
	
	leds = ALProxy("ALLeds",ip(),9559)
	leds.off("AllLeds")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.17, -0.17, -0.17])

	names.append("HeadYaw")
	times.append([5.96, 9.52, 12.8])
	keys.append([0, 0, 0])

	names.append("LAnklePitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.0733724, 0.0733724, 0.0733724])

	names.append("LAnkleRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.113483, -0.113483, -0.113483])

	names.append("LElbowRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.505407, -0.505407, -0.505407])

	names.append("LElbowYaw")
	times.append([5.96, 9.52, 12.8])
	keys.append([-1.2174, -1.2174, -1.2174])

	names.append("LHand")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.27019, 0.27019, 0.27019])

	names.append("LHipPitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.168429, 0.168429, 0.168429])

	names.append("LHipRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.122589, 0.122589, 0.122589])

	names.append("LHipYawPitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.159941, -0.159941, -0.159941])

	names.append("LKneePitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.0906351, -0.0906351, -0.0906351])

	names.append("LShoulderPitch")
	times.append([3.16, 5.96, 7.76, 9.52, 11.28, 12.8])
	keys.append([-0.872665, 1.48422, -0.872665, 1.48422, -0.872665, 1.48422])

	names.append("LShoulderRoll")
	times.append([3.16, 5.96, 9.52, 12.8])
	keys.append([0.191986, 0.201915, 0.201915, 0.201915])

	names.append("LWristYaw")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.105863, 0.105863, 0.105863])

	names.append("RAnklePitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.0773586, 0.0773586, 0.0773586])

	names.append("RAnkleRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.0767987, 0.0767987, 0.0767987])

	names.append("RElbowRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.44793, 0.44793, 0.44793])

	names.append("RElbowYaw")
	times.append([5.96, 9.52, 12.8])
	keys.append([1.25906, 1.25906, 1.25906])

	names.append("RHand")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.310403, 0.310403, 0.310403])

	names.append("RHipPitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.16018, 0.16018, 0.16018])

	names.append("RHipRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.0778176, -0.0778176, -0.0778176])

	names.append("RHipYawPitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.159941, -0.159941, -0.159941])

	names.append("RKneePitch")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.0822982, -0.0822982, -0.0822982])

	names.append("RShoulderPitch")
	times.append([3.16, 5.96, 7.76, 9.52, 11.28, 12.8])
	keys.append([-0.872665, 1.45715, -0.872665, 1.45715, -0.872665, 1.45715])

	names.append("RShoulderRoll")
	times.append([5.96, 9.52, 12.8])
	keys.append([-0.179022, -0.179022, -0.179022])

	names.append("RWristYaw")
	times.append([5.96, 9.52, 12.8])
	keys.append([0.13037, 0.13037, 0.13037])

	leds.on("AllLedsGreen")

	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		motion = ALProxy("ALMotion", ip(), 9559)
		#motion = ALProxy("ALMotion")
		motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  	print err
	leds = ALProxy("ALLeds",ip(),9559)
	leds.on("AllLedsGreen")
	#leds.off()

def lateralqnees():
#def feedback_positivo(ip_robot):
	#from naoqi import ALProxy # SE DEBE IMPORTAR ESTO:

	#leds = ALProxy("ALLeds","192.168.1.100",9559)
	#print("la IP ingresada es:", ip_robot)
	# CAMBIAR VALOR DE LA IP 
	leds = ALProxy("ALLeds",ip(),9559)
	leds.off("AllLeds")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.151908, -0.14884, -0.158044, -0.158044, -0.158044])

	names.append("HeadYaw")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.00302602, -0.00771189, -0.00771189, -0.00771189, -0.00771189])

	names.append("LAnklePitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.091998, 0.091998, 0.0858622, 0.0858622, 0.0843279])

	names.append("LAnkleRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.110406, -0.118076, -0.110406, -0.110406, -0.116542])

	names.append("LElbowRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.406468, -0.397265, -0.383458, -1.02774, -0.516916])

	names.append("LElbowYaw")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-1.18122, -1.18122, -1.19656, 0.00609397, -1.14287])

	names.append("LHand")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.288, 0.2928, 0.2868, 0.2868, 0.2868])

	names.append("LHipPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.12583, 0.12583, 0.124296, 0.124296, 0.122762])

	names.append("LHipRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.12583, 0.122762, 0.12583, 0.12583, 0.122762])

	names.append("LHipYawPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.177901, -0.171766, -0.176367, -0.176367, -0.171766])

	names.append("LKneePitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.0966839, -0.0923279, -0.090548, -0.090548, -0.0951499])

	names.append("LShoulderPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([1.46953, 1.44192, 0.18097, 0.101202, 1.54009])

	names.append("LShoulderRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.184038, 0.194775, -0.039926, -0.144238, 0.239262])

	names.append("LWristYaw")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.0797259, 0.078192, 0.0904641, 0.0904641, 0.0966001])

	names.append("RAnklePitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.0890141, 0.0859461, 0.092082, 0.092082, 0.0890141])

	names.append("RAnkleRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.11049, 0.119694, 0.11816, 0.11816, 0.119694])

	names.append("RElbowRoll")
	times.append([1, 2.32, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.391212, 1.54462, 0.377407, 0.38661, 0.38661, 0.385075])

	names.append("RElbowYaw")
	times.append([1, 2.32, 3.68, 5.04, 6.64, 7.76])
	keys.append([1.19341, 0.174533, 1.18574, 1.19648, 1.19648, 1.19341])

	names.append("RHand")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.2884, 0.2848, 0.2984, 0.2984, 0.2952])

	names.append("RHipPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.130348, 0.130348, 0.12728, 0.12728, 0.130348])

	names.append("RHipRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.12728, -0.12728, -0.121144, -0.121144, -0.128814])

	names.append("RHipYawPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.177901, -0.171766, -0.176367, -0.176367, -0.171766])

	names.append("RKneePitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.095066, -0.091998, -0.0873961, -0.0873961, -0.095066])

	names.append("RShoulderPitch")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.092082, 1.36223, 1.5187, 1.5187, 1.52177])

	names.append("RShoulderRoll")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([-0.0598679, -0.17185, -0.208666, -0.208666, -0.228608])

	names.append("RWristYaw")
	times.append([1, 3.68, 5.04, 6.64, 7.76])
	keys.append([0.0889301, 0.105804, 0.107338, 0.107338, 0.110406])

	leds.on("AllLedsBlue")

	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		motion = ALProxy("ALMotion", ip(), 9559)
		#motion = ALProxy("ALMotion")
		motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
		print err

	leds = ALProxy("ALLeds",ip(),9559)
	leds.on("AllLedsBlue")
	#leds.off()

def stepup():
#def feedback_positivo(ip_robot):
	#from naoqi import ALProxy # SE DEBE IMPORTAR ESTO:

	#leds = ALProxy("ALLeds","192.168.1.100",9559)
	#print("la IP ingresada es:", ip_robot)
	# CAMBIAR VALOR DE LA IP 
	leds = ALProxy("ALLeds",ip(),9559)
	leds.off("AllLeds")

	
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.14884, -0.14884, -0.14884, -0.14884])

	names.append("HeadYaw")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.00464392, -0.00771189, -0.00464392, -0.00771189])

	names.append("LAnklePitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.0873961, 0.091998, 0.0873961, 0.091998])

	names.append("LAnkleRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.113474, -0.118076, -0.113474, -0.118076])

	names.append("LElbowRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-1.48353, -0.397265, -1.48353, -0.397265])

	names.append("LElbowYaw")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.122173, -1.18122, -0.122173, -1.18122])

	names.append("LHand")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.2896, 0.2928, 0.2896, 0.2928])

	names.append("LHipPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.12583, 0.12583, 0.12583, 0.12583])

	names.append("LHipRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.119694, 0.122762, 0.119694, 0.122762])

	names.append("LHipYawPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.170232, -0.171766, -0.170232, -0.171766])

	names.append("LKneePitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.0966839, -0.0923279, -0.0966839, -0.0923279])

	names.append("LShoulderPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0, 1.44192, 0, 1.44192])

	names.append("LShoulderRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.610865, 0.194775, 0.610865, 0.194775])

	names.append("LWristYaw")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.0996681, 0.078192, 0.0996681, 0.078192])

	names.append("RAnklePitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.0874801, 0.0859461, 0.0874801, 0.0859461])

	names.append("RAnkleRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.115092, 0.119694, 0.115092, 0.119694])

	names.append("RElbowRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([1.48353, 0.377407, 1.48353, 0.377407])

	names.append("RElbowYaw")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.122173, 1.18574, 0.122173, 1.18574])

	names.append("RHand")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.2888, 0.2848, 0.2888, 0.2848])

	names.append("RHipPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.131882, 0.130348, 0.131882, 0.130348])

	names.append("RHipRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.12728, -0.12728, -0.12728, -0.12728])

	names.append("RHipYawPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.170232, -0.171766, -0.170232, -0.171766])

	names.append("RKneePitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.0889301, -0.091998, -0.0889301, -0.091998])

	names.append("RShoulderPitch")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.0813439, 1.36223, 0.0813439, 1.36223])

	names.append("RShoulderRoll")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([-0.668866, -0.17185, -0.668866, -0.17185])

	names.append("RWristYaw")
	times.append([2.16, 4.16, 6.16, 8.04])
	keys.append([0.0981341, 0.105804, 0.0981341, 0.105804])

	leds.on("AllLedsBlue")

	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		motion = ALProxy("ALMotion", ip(), 9559)
		#motion = ALProxy("ALMotion")
		motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  	print (err)

	leds = ALProxy("ALLeds",ip(),9559)
	leds.on("AllLedsBlue")
	#leds.off()
	
	leds.on("AllLedsBlue")

def basicmarching():
#def feedback_positivo(ip_robot):
	#from naoqi import ALProxy # SE DEBE IMPORTAR ESTO:

	#leds = ALProxy("ALLeds","192.168.1.100",9559)
	#print("la IP ingresada es:", ip_robot)
	# CAMBIAR VALOR DE LA IP 
	leds = ALProxy("ALLeds",ip(),9559)
	leds.off("AllLeds")


	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1.56, 4.76])
	keys.append([-0.144238, -0.144238])

	names.append("HeadYaw")
	times.append([1.56, 4.76])
	keys.append([-0.00771189, -0.00771189])

	names.append("LAnklePitch")
	times.append([1.56, 4.76])
	keys.append([0.0889301, 0.0889301])

	names.append("LAnkleRoll")
	times.append([1.56, 4.76])
	keys.append([-0.113474, -0.113474])

	names.append("LElbowRoll")
	times.append([1.56, 4.76])
	keys.append([-0.408002, -0.377323])

	names.append("LElbowYaw")
	times.append([1.56, 4.76])
	keys.append([-1.2073, -1.2073])

	names.append("LHand")
	times.append([1.56, 4.76])
	keys.append([0.2916, 0.2916])

	names.append("LHipPitch")
	times.append([1.56, 4.76])
	keys.append([0.128898, 0.128898])

	names.append("LHipRoll")
	times.append([1.56, 4.76])
	keys.append([0.122762, 0.122762])

	names.append("LHipYawPitch")
	times.append([1.56, 4.76])
	keys.append([-0.168698, -0.168698])

	names.append("LKneePitch")
	times.append([1.56, 4.76])
	keys.append([-0.093616, -0.093616])

	names.append("LShoulderPitch")
	times.append([1.56, 3.16, 4.76, 5.96])
	keys.append([1.5708, 1.22173, 0, 1.5708])

	names.append("LShoulderRoll")
	times.append([1.56, 3.16, 4.76, 5.96])
	keys.append([0.226991, 0.139626, 0.139626, 0.174533])

	names.append("LWristYaw")
	times.append([1.56, 4.76])
	keys.append([0.11194, 0.11194])

	names.append("RAnklePitch")
	times.append([1.56, 4.76])
	keys.append([0.0890141, 0.0890141])

	names.append("RAnkleRoll")
	times.append([1.56, 4.76])
	keys.append([0.115092, 0.115092])

	names.append("RElbowRoll")
	times.append([1.56, 4.76])
	keys.append([0.389678, 0.377407])

	names.append("RElbowYaw")
	times.append([1.56, 4.76])
	keys.append([1.18881, 1.18881])

	names.append("RHand")
	times.append([1.56, 4.76])
	keys.append([0.2916, 0.2916])

	names.append("RHipPitch")
	times.append([1.56, 4.76])
	keys.append([0.130348, 0.130348])

	names.append("RHipRoll")
	times.append([1.56, 4.76])
	keys.append([-0.122678, -0.122678])

	names.append("RHipYawPitch")
	times.append([1.56, 4.76])
	keys.append([-0.168698, -0.168698])

	names.append("RKneePitch")
	times.append([1.56, 4.76])
	keys.append([-0.091998, -0.091998])

	names.append("RShoulderPitch")
	times.append([1.56, 3.16, 4.76])
	keys.append([0, 1.5708, 1.5708])

	names.append("RShoulderRoll")
	times.append([1.56, 3.16, 4.76])
	keys.append([-0.174533, -0.174533, -0.181053])

	names.append("RWristYaw")
	times.append([1.56, 4.76])
	keys.append([0.0904641, 0.0904641])

	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		motion = ALProxy("ALMotion", ip(), 9559)
		#motion = ALProxy("ALMotion")
		motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
	  	print err
	leds = ALProxy("ALLeds",ip(),9559)
	leds.on("AllLedsBlue")
	#leds.off()
	
	leds.on("AllLedsBlue")

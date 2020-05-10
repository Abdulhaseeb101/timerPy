import time
import os

class Methods():
	
	def start():

		print('3...')		# Countdown for the user to get ready.
		time.sleep(1)	
		print('2...')
		time.sleep(1)
		print('1 Start')

	def workCount(workTime, second):
		
		for second in range(workTime):		# Counts and prints the 
				print(workTime - second)	# time left.
				time.sleep(1)

	def restCount(restTime, second):
		
		for second in range(restTime):		# Counts and prints the
				print(restTime - second)	# time left.
				time.sleep(1)

	def setsCount(workTime, restTime, sets):

		for set in range(sets):		# This function makes the function 
								# calls for the workCount and 
			second = 0			# restCount functions. It keeps 
			os.system('aplay whistle.wav')# record of the sets left.
			print('\n WORK !!\n')	
			Methods.workCount(workTime, second)

			second = 0
			os.system('aplay whistle.wav')
			print('\n REST !!\n')
			Methods.restCount(restTime, second)
						
			print('\n SET ' + str(set + 1) + ' COMPLETE !! \n')

		os.system('aplay whistle.wav')

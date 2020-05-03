from timerPyDep import Methods		# Importing required methods from 
									# a different file.
workTime = input('Enter the work time:- ')		# Getting input the 
restTime = input('Enter the rest time:- ')		# required.
sets = input('Enter the number of total sets :- ')

workTime = int(workTime)		# Converting input into usable 
restTime = int(restTime)		# integers
sets = int(sets)

Methods.start()		# Calling start and setsCount functions.
Methods.setsCount(workTime, restTime, sets)

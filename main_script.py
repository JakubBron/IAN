from speech_to_text import *
import text_to_speech as TTS
from logScript import *
from multiprocessing import Process, Queue
from bluetoothServer import bluetoothServer

logger = initLogs('main.log')
logger.info("##############################################################################\n\tNew session started.")

# Import modules (new).
import os
import importlib

moduleInits = {}
errors = 0
good = 0

queue_bluetooth = Queue()

logger.info('Adding modules...')
print('Dodawanie modulow...')
for root, _, files in os.walk('modules'):
	for file in files:
		if file[-3:].lower() == '.py' and file[:3].lower() == 'mod':
			try:
				module = importlib.import_module('modules.' + file[:-3])
				for key in module.keys():
					moduleInits[key] = module.operation
			except Exception as e:
				logger.error('Error while adding ' + file + ' ' +  str('modules.' + file[:-3]) + '\nError: ' + str(e))
				errors += 1
			else:
				logger.info('Added ' + file + ' ' + str(module) + '\nWith keys: ' + str(module.keys()))
				print('Dodano ' + file + '\n\tZ kluczem wykonania: ' + str(module.keys()))
				good += 1
			finally:
				pass
logger.info(('Done!' + 'Loaded' + str(good) + 'modules.' + str(errors) + 'error modules').join(' '))
print(('Ukonczono!' + 'Dodano' + str(good) + 'modulow.' + str(errors) + 'blednych modulow.').join(' '))

"""Printing start screen"""

logger.info("Loading start screen...")
	
with open("startScreen_data.txt", "r") as f:
	for line in f:
		print(line)
print("                             Inteligentny Asystent Nowoczesności")
print("\n")
print("(C) 2019 Autorzy: Jakub Bronowski, Bartłomiej Krawisz, Kondrad Obernikowicz - powiat gdański")
print("\n")
	
logger.info("Printed start screen.")


def removeFirsts(data, numberToRemove):
	"""Return text without numberToRemove first letters."""
	return data[numberToRemove::]

def recognizeAndExecute(recognized):
	"""Recognize variable 'recognized', execute appriopriate command and return results."""
	global logger
	
	recognized = recognized.lower()

	for _ in moduleInits:
		findResult = recognized.find(_)
		if not findResult == -1:
			return moduleInits[_](removeFirsts(recognized, findResult + len(_)))
	
	logger.warning("Didn't recognize anything.")
	
	return None

def loop():
	"""Listen to user, try execute the user's command and repeat."""
	global logger
	
	while 1:
		logger.info("Listening to user...")
		
		is_recognized = True
		recognized = listenTo()
		if recognized == None:
			logger.warning("Didn't hear anything.")
			is_recognized = False
		
		if is_recognized:
			logger.info("Recognized: '" + recognized + "'.")
	
			recognized = recognized.lower()
		
			print(recognized)

		if queue_bluetooth.qsize() > 0:
			recognized_blue = queue_bluetooth.get()
			logger.info("BUT received from bluetooth: '" + recognized_blue + "'.")
			print("BUT received from bluetooth: " + recognized_blue)
			recognized = recognized_blue
			is_recognized = True
		if is_recognized:
			TTS.textToSpeech(recognizeAndExecute(recognized))
		

if __name__ == "__main__":
	######## DEBUG ##########
#	while(1):
#		TTS.textToSpeech(recognizeAndExecute(input()))
	#####################
	
	blue_process = Process(target=bluetoothServer, args=(queue_bluetooth,))
	blue_process.start()
	loop()

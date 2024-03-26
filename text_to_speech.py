from gtts import gTTS
import os
from logScript import * # Debugging.

def textToSpeech(text):
	"""Translate text to speech and play it."""
	# Debug.
	logger = initLogs("main.log")
	logger.info("Translating...")
	
	if text == None:
		return
	
	number = 0
	error = True
	
	while error:
		try:
			os.remove("./tts" + str(number) + ".mp3")
		except Exception as e:
			if str(e)[:12] == "[WinError 5]":
				number += 1
			else:
				error = False
		else:
			error = False
	
	text = str(text)

	# Debug.
	print(text)
	
	try:
		# Debug.
		logger.info("Trying to send data...")  

		tts = gTTS(text=text, lang='pl')
		tts.save("./tts" + str(number) + ".mp3")
	except Exception as e:
		logger.error(e)
  
	# Debug.
	logger.info("Data sent!")
	logger.info("Playing sound...")

	# Play tts1 sound.
	try:
		os.system("mpg321 tts" + str(number) + ".mp3")
	except Exception as e:
		logger.warning(e)
		
	try:
		os.remove("./tts" + str(number) + ".mp3")
	except Exception as e:
		pass

if __name__ == "__main__":
	textToSpeech(input())
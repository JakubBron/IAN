import speech_recognition as sr
import pyttsx3
from logScript import * # Debugging.

def listenTo():
	"""Listen to user and translate it to text."""
	# Debug.
	logger = initLogs("main.log")
	logger.info("Listening...")
	
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Powiedz komendę.")
		audio = r.listen(source)

	recognized = None

	try:
		recognized = r.recognize_google(audio, language="pl-PL")
	except sr.UnknownValueError:
		logger.error("Audio unintelligible")
		
	return recognized
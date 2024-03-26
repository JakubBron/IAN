from math import pi
from logScript import *

# Dictionary for polish numbers.
polishNumberDictionary = {
	"jeden" : 1,
	"dwa" : 2,
	"trzy" : 3,
	"dodać" : '+',
	"plus" : '+',
	"odjąć" : '-',
	"minus" : '-',
	"x" : '*',
	"razy" : '*',
	"podzielić na" : "/",
	"%" : "/100",
	"z liczby" : "*",
	"shrek" : "*95",
	"shreków" : "*95",
	"minuty" : "*60",
	"minut" : "*60",
	"sekundy" : "",
	"sekund" : "",
	"i" : "+"
}

def textToNumber(text):
	"""Return number."""
	# Debug.
	logger = initLogs("main.log")
	logger.info("textToNumbering...")

	for _ in polishNumberDictionary:
		text = text.replace(_, str(polishNumberDictionary[_]))

	return text

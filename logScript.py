import logging
import inspect
import os

def initLogs(file, name=None):
	"""Initialize logs and return logger."""

	if name == None:
		name = os.path.basename(inspect.currentframe().f_back.f_code.co_filename)[:-3]
	
	# create logger with 'main_script'
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)
	# create file handler which logs even debug messages
	fh = logging.FileHandler(file)
	fh.setLevel(logging.DEBUG)
	# create console handler with a higher log level
	ch = logging.StreamHandler()
	ch.setLevel(logging.ERROR)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s\n\t - %(message)s')
	fh.setFormatter(formatter)
	ch.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(fh)
	logger.addHandler(ch)
	
	return logger
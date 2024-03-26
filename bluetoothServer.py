import subprocess
from bluetooth import *

def bluetoothServer(q):
	# CONFIG #
	auth_method = "AUTH-METHOD_PIN"
	pin = "1234"

	lines = None
	with open("config.txt", 'r') as file:
		lines = file.readlines()

	pin = str(lines[0])
	pin = pin[0:4]
	print(pin)
	cmd = "sudo hciconfig hci0 piscan"
	subprocess.check_output(cmd, shell = True)

	serverSock = BluetoothSocket(RFCOMM)
	serverSock.bind(("", PORT_ANY))
	serverSock.listen(1)

	port = serverSock.getsockname()[1]
	uuid = "24751908-0d51-4f75-83e7-2f76d32658b5"
	advertise_service(serverSock, "IAN Bluetooth Server", service_id = uuid, service_classes = [uuid, SERIAL_PORT_CLASS], profiles = [SERIAL_PORT_PROFILE])
	while True:
		try:
			clientSock, clientInfo = serverSock.accept()
			print("Zaakceptowano polaczenie od: ", clientInfo)
			clientSock.send(auth_method)        
			recvPin = str(clientSock.recv(1024))
			recvPin = recvPin[2:len(recvPin)-1]
			if(recvPin == pin):
				clientSock.send("AUTH_OK")
			else:
				clientSock.send("AUTH_ERROR")
				clientSock.close()
				continue
			while True:
				command = str(clientSock.recv(1024))
				command = command[2:len(command)-1]
				print(command)
				if(command == "COMMAND_SHUTDOWN"):
					cmd = "sudo shutdown now"
					subprocess.check_output(cmd, shell=True)
					clientSock.close()
					break
				if(command == "COMMAND_REBOOT"):
					cmd = "sudo reboot now"
					subprocess.check_output(cmd, shell=True)
					clientSock.close()
					break
				if(command == "COMMAND_TEXT-COMMAND"):
					clientSock.send("OK")
					textCommand = str(clientSock.recv(1024))
					textCommand = textCommand[2:len(textCommand)-1]
					print(textCommand)
					q.put(textCommand)

				
		except IOError:
			pass
		print("Rozlaczono")
		clientSock.close()


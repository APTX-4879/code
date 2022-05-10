import socket
import optparse
parser=optparse.OptionParser()
parser.add_option("-u","--url",dest="url")
parser.add_option("-p","--port",dest="port")
(optionss,arguments)=parser.parse_args()
host=optionss.url
ports=optionss.port
if ports is None:
	scanport=0
else:
	scanport=1
def scan(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host, port))	
		print("Port open: " + str(port))
		s.close()
	except:
		print("Port closed: " + str(port))
if scanport==0:
	for port in range(1,1000):
		scan(host,port)
else:
	scan(host,int(ports))
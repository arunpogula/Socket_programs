import socket              
  
#socket object  
s = socket.socket()          
# conecting port of server 
port = 12345                
# cconnecting 
s.connect(('127.0.0.1', port))
# receive data from the server  
print (s.recv(1024) ) 
# close the connection  
s.close()
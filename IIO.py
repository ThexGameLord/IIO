from time import sleep
import requests
from urllib.parse import urlparse
import urllib3
import os

print(" ___________________________________________________ ")
print("|       Welcome to IsItOnline program aka IIO       |")
print("|___________________________________________________|")

sleep(1.5)

print("        ___________________________________ ")
print("       |       Made By Thexgamelord_       |")
print("       |___________________________________|")

print("       _____________________________________ ")
print("      |       github.com/Thexgamelord       |")
print("      |_____________________________________|")

while True:
    myreq= input("enter destination to check: ")
    if myreq != "http://"+myreq:
        myreq = myreq.replace("http://","")
        myreq = myreq.replace("https://","")
        myreq = myreq.replace("/","")
        finalreq = "http://"+myreq+"/"
    #print(finalreq)
    try:
        domain = "???"
        rqchk = requests.get(finalreq, timeout=3)
        domain = urlparse(finalreq).netloc
        if rqchk.status_code == 200:
            print(f"[INFO] {domain} is online!")
        else:
            print(f"[INFO] {domain} is not online or doesnt respond to requests.")
    
        
    except requests.exceptions.InvalidURL:
        print("[ERROR] Please make sure to input a valid ip or url")
    except ConnectionRefusedError:
        print(f"[ERROR] Connection Refused by {domain}")
    except urllib3.exceptions.NewConnectionError:
        print("[ERROR] New connection error")
    except urllib3.exceptions.MaxRetryError:
        print("[ERROR] Max retry error")
    except requests.exceptions.ConnectionError:
        print("[ERROR] Connection error")
    except requests.exceptions.ReadTimeout:
        print("[ERROR] ReadTimeout {0}".format(domain))
        
    sleep(1)
#    domain = urlparse(finalreq).netloc
    
#    if rqchk.status_code == 200:
#        print(f"[INFO] {domain} is online!")
#    else:
#        print(f"[INFO] {domain} is not online or doesnt respond to requests.")

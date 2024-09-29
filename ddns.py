
import sys
import requests
from datetime import datetime

#Loggin
logfile = "./log.txt"
def logging(mensaje):
    with open(logfile,"a") as log:
        hora = datetime.now()
        logeo = str(hora) + " " + mensaje + "\n"
        log.write(logeo)

#DNS Edit Record by Domain, Subdomain and Type. Endpoint
endpoint = "https://api.porkbun.com/api/json/v3/dns/editByNameType/"

#Pass the last part of the endpoint /DOMAIN/TYPE/[SUBDOMAIN] like kkpj.pro/A/www
modifyendpoint = sys.argv[1]

#should give something like https://api.porkbun.com/api/json/v3/dns/editByNameType/kkpj.pro/A/www
urichange = endpoint+modifyendpoint

#endpoint to make a ping and get current public IP.
uriget = "https://api.porkbun.com/api/json/v3/ping"

#endpoint to get current ip setted:
currentipendpoint = "https://api.porkbun.com/api/json/v3/dns/retrieveByNameType/"
uricurrentip = currentipendpoint+modifyendpoint

#If you regenerate the api keys you need to change this.
secretapikey = ""
apikey = ""

#Json pingcommand to get public IP
keycommand = {
"secretapikey": "{}".format(secretapikey),
"apikey": "{}".format(apikey),
}

#Post to get public IP.
def getpublicip():
    logging("Current public Ip on Device.")
    x = requests.post(uriget,headers="",json=keycommand)
    logging(str(x.status_code))
    logging(str(x.json()))
    response = x.json()
    return response["yourIp"]

#New ip to set in the record.
ip = getpublicip()

#It compares the actual IP on the record vs the actual public IP on the host.
def compareip():
    y = requests.post(uricurrentip,headers="",json=keycommand)
    yj = y.json()
    currentip = yj["records"][0]["content"]
    logging("Current IP on the PorkBun Host.")
    logging(currentip)
    logging(str(y.status_code))
    if currentip == ip:
        return 0
    else:
        return 1

#Json modifycommand to change IP record.
modifycommand = {
"secretapikey": "{}".format(secretapikey),
"apikey": "{}".format(apikey),
"content": "{}".format(ip),
"ttl": "600"
}

#Post agains the api of Porkbun only if the IP is not the same.
def pushchange():
    if compareip() == 1:
        logging("IP will be renewed")
        r = requests.post(urichange,headers="",json=modifycommand)
        logging(str(r.status_code))
        logging(str(r.json()))
        return r
    else:
        logging("No change needed.")

pushchange()

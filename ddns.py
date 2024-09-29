
import sys
import requests
from datetime import datetime

#DNS Edit Record by Domain, Subdomain and Type. Endpoint
endpoint = "https://api.porkbun.com/api/json/v3/dns/editByNameType/"

#Pass the last part of the endpoint /DOMAIN/TYPE/[SUBDOMAIN] like kkpj.pro/A/www
modifyendpoint = sys.argv[1]

#should give something like https://api.porkbun.com/api/json/v3/dns/editByNameType/kkpj.pro/A/www
urichange = endpoint+modifyendpoint

#endpoint to make a ping and get current public IP.
uriget = "https://api.porkbun.com/api/json/v3/ping"

#If you regenerate the api keys you need to change this.
secretapikey = "sk1_1ca1ee10a7168db48014783471c2dbe7012b380a2d7382f280420b7f0a7616fa"
apikey = "pk1_fffc32ec09dce83cc6778b716bbd66d3a5d915d4a5f2e1a9ce75ab6f0eb97ef5"

#Json pingcommand to get public IP
pingcommand = {
"secretapikey": "{}".format(secretapikey),
"apikey": "{}".format(apikey),
}

#Loggin
logfile = "./log.txt"
def logging(mensaje):
    with open(logfile,"a") as log:
        hora = datetime.now()
        logeo = str(hora) + " " + mensaje + "\n"
        log.write(logeo)

#Post to get public IP.
def getpublicip():
    x = requests.post(uriget,headers="",json=pingcommand)
    logging(str(x.status_code))
    logging(str(x.json()))
    response = x.json()
    return response["yourIp"]

#New ip to set in the record.
ip = getpublicip()

#Json modifycommand to change IP record.
modifycommand = {
"secretapikey": "{}".format(secretapikey),
"apikey": "{}".format(apikey),
"content": "{}".format(ip),
"ttl": "600"
}

#Post agains the api of Porkbun.
def pushchange():
    r = requests.post(urichange,headers="",json=modifycommand)
    logging(str(r.status_code))
    logging(str(r.json()))
    return r

pushchange()
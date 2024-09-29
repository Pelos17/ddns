
import sys
import requests
from datetime import datetime

#DNS Edit Record by Domain, Subdomain and Type. Endpoint
endpoint = "https://api.porkbun.com/api/json/v3/dns/editByNameType/"

#Pass the last part of the endpoint /DOMAIN/TYPE/[SUBDOMAIN] like kkpj.pro/A/www
endpointrecord = sys.argv[1]
#endpointrecord = "kkpj.pro/A/satisfactory"


#should give something like https://api.porkbun.com/api/json/v3/dns/editByNameType/kkpj.pro/A/www
uri = endpoint+endpointrecord
#print (uri)


#If you regenerate the api keys you need to change this.
secretapikey = "sk1_1ca1ee10a7168db48014783471c2dbe7012b380a2d7382f280420b7f0a7616fa"
apikey = "pk1_fffc32ec09dce83cc6778b716bbd66d3a5d915d4a5f2e1a9ce75ab6f0eb97ef5"

#New ip to set in the record.
ip = sys.argv[2]
#content = "3.3.3.3"

#Json command.
command = {
"secretapikey": "{}".format(secretapikey),
"apikey": "{}".format(apikey),
"content": "{}".format(ip),
"ttl": "600"
}

#Loggin
logfile = "./log.txt"
def logging(mensaje):
    with open(logfile,"a") as log:
        hora = datetime.now()
        logeo = str(hora) + " " + mensaje + "\n"
        log.write(logeo)

#Post agains the api of Porkbun.
def request():
    r = requests.post(uri,headers="",json=command)
    logging(str(r.status_code))
    logging(str(r.json()))
    return r

request()
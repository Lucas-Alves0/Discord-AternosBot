from python_aternos import *
from time import *

atclient = Client()

user = {
    'username':'SrLks7162',
    'password':'L6070al#'
}
atclient.login(user['username'],user['password'])
aternos = atclient.account

servs = aternos.list_servers()
myserv = servs[1]


try:
    myserv.fetch()
    print(myserv.status)
    myserv.start(headstart=True)
    myserv.fetch()
    print(myserv.status)
except:
    while myserv.status != 'online':
        myserv.fetch()
        print(myserv.status)

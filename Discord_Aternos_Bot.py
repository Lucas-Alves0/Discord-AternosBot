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
    myserv.start(headstart=True)
    myserv.fetch()
    print(myserv.status)
    while myserv.status == 'waiting':
        sleep(10)
        try:
            myserv.confirm()
        except:
            myserv.fetch()
            print('The server still', myserv.status)
    else:
        while myserv.status != 'online':
            sleep(10)
            myserv.fetch()
            print('The server is', myserv.status)
        else:
            myserv.fetch()
            print('The server is', myserv.status)
except:
    while myserv.status == 'waiting':
        sleep(10)
        try:
            myserv.confirm()
        except:
            myserv.fetch()
            print('The server is ', myserv.status)
    else:
        while myserv.status != 'online':
            sleep(10)
            myserv.fetch()
            print('The server is ', myserv.status)
        else:
            myserv.fetch()
            print('The server is ', myserv.status)

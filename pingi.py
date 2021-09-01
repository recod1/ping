from ping3 import ping, verbose_ping
from datetime import datetime
import plyer
import time

ip = '10.44.54.167'


lastTime = 0
status = True
preStatus = True
def log(status, add):
    date = status + ' ' + add + ' ' + str(t.strftime("%d-%m-%Y %H:%M:%S"))
    f = open('log.txt', 'a')
    f.write(date + '\n')
    f.close()

def alert(var, add):
    if var:

        plyer.notification.notify(message='Узел ' + add + ' доступен',
                        app_name='Ping',
                        app_icon='codingbrowser_102152.ico',
                        title='Соединение восстановленно', )

    else:
        plyer.notification.notify(message='Узел ' + add + ' не доступен',
                        app_name='Ping',
                        app_icon='codingbrowser_102152.ico',
                        title='Соединение разорвано', )


while True:

    t = datetime.now()
    date = ip + ' ' + str(t.strftime("%d-%m-%Y %H:%M:%S"))


    if ping(ip) != None:
        status = True
        print("Successful " + date)
        log('Successful', ip)
        if preStatus == False and status == True:
                alert(True, ip)

    else:
        print('Not found ' + date)
        log('Not found', ip)
        alert(False, ip)
        status = False


    preStatus = status
    time.sleep(1)

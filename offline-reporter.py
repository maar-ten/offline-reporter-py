#!/usr/bin/python3

import logging
import time

from http.client import HTTPSConnection
from datetime import date
from string import Template

CONNECTION_TIMEOUT = 5
THREAD_SLEEP = 10

def main():
    startLogger()

    while True:
        if True == isOffline():
            logConnectionError()
            threadSleep = THREAD_SLEEP - CONNECTION_TIMEOUT
        else:
            threadSleep = THREAD_SLEEP
        
        time.sleep(threadSleep)

def startLogger():
    today = date.today().isoformat()
    datedFilename = 'errors_{when}.log'.format(when = today)

    logging.basicConfig(
        filename = datedFilename, 
        format = '%(asctime)s %(message)s', 
        level = logging.ERROR
    )

def isOffline():
    try:
        client = http.client.HTTPSConnection('canihazip.com', timeout = CONNECTION_TIMEOUT)
        client.request('GET', '/s')
        client.getresponse().read()
        client.close()
        return False
    except:
        return True

def logConnectionError():
    logging.error('cannot reach the internet')

if __name__ == '__main__':
    main()
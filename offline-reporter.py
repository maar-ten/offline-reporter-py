#!/usr/bin/python3

from http.client import HTTPSConnection
import logging
import time
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
    filenameTpl = Template('errors_$when.log')
    datedFilename = filenameTpl.substitute(when=today)

    logging.basicConfig(
        filename=datedFilename, 
        format='%(asctime)s %(message)s', 
        level=logging.ERROR
    )


def isOffline():
    try:
        client = http.client.HTTPSConnection('canihazip.com', timeout=CONNECTION_TIMEOUT)
        client.request('GET', '/s')
        client.getresponse().read()
        client.close()
        return False
    except Exception as e:
        return True

def logConnectionError():
    logging.error('cannot reach the internet')

if __name__ == '__main__':
    main()
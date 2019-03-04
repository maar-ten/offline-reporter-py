#!/usr/bin/python3

import time
import http.client
import logging

CONNECTION_TIMEOUT = 5
THREAD_SLEEP = 10

logging.basicConfig(filename='errors.log', format='%(asctime)s %(message)s', level=logging.ERROR)

def main():
    while True:
        if True == isOffline():
            logConnectionError()
            threadSleep = THREAD_SLEEP - CONNECTION_TIMEOUT
        else
            threadSleep = THREAD_SLEEP
        
        time.sleep(threadSleep)

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
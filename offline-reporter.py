#!/usr/bin/python3

import logging
import time
import socket

from datetime import datetime

CONNECTION_TIMEOUT = 5
THREAD_SLEEP = 10

def main():
    startLogger()

    while True:
        if True == isOffline():
            logConnectionError()
        
        time.sleep(THREAD_SLEEP)

def startLogger():
    today = datetime.now().date().isoformat()
    datedFilename = 'errors_{when}.log'.format(when = today)

    logging.basicConfig(
        filename = datedFilename, 
        format = '%(asctime)s %(message)s', 
        level = logging.ERROR
    )

def isOffline(host = '8.8.8.8', port = 53):
    try:
        socket.setdefaulttimeout(CONNECTION_TIMEOUT)
        socket.socket().connect((host, port))
        return False
    except Exception as e:
        return True

def logConnectionError():
    logging.error('cannot reach the internet')

if __name__ == '__main__':
    main()
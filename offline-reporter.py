#!/usr/bin/python3

import time

import logging
import socket
from datetime import datetime

CONNECTION_TIMEOUT = 5
THREAD_SLEEP = 10


def main():
    start_logger()

    while True:
        if is_offline():
            log_connection_error()

        time.sleep(THREAD_SLEEP)


def start_logger():
    today = datetime.now().date().isoformat()
    dated_filename = 'errors_{when}.log'.format(when=today)

    logging.basicConfig(
        filename=dated_filename,
        format='%(asctime)s %(message)s',
        level=logging.ERROR
    )


def is_offline():
    try:
        socket.setdefaulttimeout(CONNECTION_TIMEOUT)
        socket.socket().connect(('8.8.8.8', 53))
        return False
    except Exception:
        return True


def log_connection_error():
    logging.error('cannot reach the internet')


if __name__ == '__main__':
    main()

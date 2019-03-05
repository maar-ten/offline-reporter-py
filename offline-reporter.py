#!/usr/bin/python3

import logging
import socket
from datetime import datetime, timedelta

from rx import Observable

CONNECTION_TIMEOUT_SEC = 5
INTERVAL_TIME_MS = 2000


def main():
    start_logger()

    connectivity = Observable.interval(INTERVAL_TIME_MS) \
        .map(lambda i: is_online())

    is_offline = connectivity.filter(lambda online: online is False)
    is_offline.subscribe(lambda i: logging.error('cannot reach the internet'))

    how_long_was_the_internet_down = connectivity \
        .distinct_until_changed(lambda online: online is False) \
        .skip(1) \
        .time_interval() \
        .filter(lambda connectivity_changed: connectivity_changed.value is True) \
        .map(lambda connectivity_changed: connectivity_changed.interval) \
        .map(lambda interval: interval + timedelta(milliseconds=INTERVAL_TIME_MS)) \
        .map(lambda timedelta: timedelta.total_seconds()) \
        .map(lambda seconds: int(seconds)) \
        .map(lambda seconds: '{sec} seconds'.format(sec=seconds)) \
        .map(lambda seconds_str: 'Internet was down for {sec_str}'.format(sec_str=seconds_str))

    how_long_was_the_internet_down.subscribe(lambda interval: print(interval))

    input('Program is running. Press enter to exit\n')


def start_logger():
    today = datetime.now().date().isoformat()
    dated_filename = 'errors_{when}.log'.format(when=today)

    logging.basicConfig(
        filename=dated_filename,
        format='%(asctime)s %(message)s',
        level=logging.ERROR
    )


def is_online():
    try:
        socket.setdefaulttimeout(CONNECTION_TIMEOUT_SEC)
        socket.socket().connect(('8.8.8.8', 53))
        return True
    except Exception:
        return False


def log_connection_error():
    logging.error('cannot reach the internet')


if __name__ == '__main__':
    main()

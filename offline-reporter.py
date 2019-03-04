#!/usr/bin/python3

import logging
import socket
from datetime import datetime

from rx import Observable

CONNECTION_TIMEOUT = 5
THREAD_SLEEP = 10
INTERVAL_TIME = 10000


def main():
    start_logger()

    numbers = [1, 2, 3, 4, 5]
    all = Observable.from_(numbers)
    all.subscribe(lambda number: print('The number is {}'.format(number)))

    Observable.interval(INTERVAL_TIME).time_interval().take(5).subscribe(lambda i: print('we are here!'))

    # connectivity = Observable.interval(INTERVAL_TIME) \
    #     .flat_map(lambda i: is_online())
    #
    # is_offline = connectivity.filter(lambda online: online is False)
    # is_offline.subscribe(lambda i: logging.error('cannot reach the internet'))
    #
    # how_long_was_the_internet_down = connectivity \
    #     .distinct_until_changed(lambda online: online is False) \
    #     .skip(1) \
    #     .time_interval() \
    #     .filter(lambda connectivity_changed: connectivity_changed.value is True) \
    #     .map(lambda connectivity_changed: connectivity_changed.interval)
    #
    # how_long_was_the_internet_down.subscribe(lambda interval: print(interval))

    # .filter(connectivityChanged => connectivityChanged.value === true)
    # .map(connectivityChanged => connectivityChanged.interval)
    # .map(interval => moment.duration(interval))
    # .map(duration => duration.add(connectivityTimeout, 'ms'))
    # .map(duration => duration.as('seconds'))
    # .map(duration => Math.round(duration) + ' seconds')
    # .map(txtDuration => 'Internet was down for ' + txtDuration + ' :unamused:');


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
        socket.setdefaulttimeout(CONNECTION_TIMEOUT)
        socket.socket().connect(('8.8.8.8', 53))
        return True
    except Exception:
        return False


def log_connection_error():
    logging.error('cannot reach the internet')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import argparse
import configparser
import logging
import os
import sys

import stomp
from tg import Tg


def setup_logging(level):
    if level == logging.DEBUG:
        urllib_level = logging.INFO
    else:
        urllib_level = logging.WARNING
    logging.getLogger('urllib3').setLevel(urllib_level)
    logging.basicConfig(stream=sys.stderr, level=level)


def main(args):
    config_file = args.config_file or "/etc/pa.conf"

    config = configparser.ConfigParser()
    config.read(config_file)

    if args.debug or config.getboolean('pa', 'debug', fallback=False):
        setup_logging(logging.DEBUG)
    else:
        setup_logging(logging.INFO)

    token_file = args.token_file or config.get('pa', 'token_file')
    with open(token_file) as tok:
        TOKEN = tok.read().strip()

    stomp_host = config.get('stomp', 'host', fallback='localhost')
    stomp_port = config.getint('stomp', 'port', fallback=61613)
    heartbeat_in = config.get('stomp', 'heartbeat_in', fallback=0)
    heartbeat_out = config.get('stomp', 'heartbeat_out', fallback=0)
    stomp_connection = stomp.Connection([(stomp_host, stomp_port)],
                                        heartbeats=(heartbeat_in,heartbeat_out))
    tg = Tg(TOKEN, stomp_connection)

    tg.run_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action='store_true')
    parser.add_argument("-c", "--config-file")
    parser.add_argument("-t", "--token-file")
    main(parser.parse_args())

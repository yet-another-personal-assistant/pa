#!/usr/bin/env python3
import logging
import os
import sys

import stomp
from tg import Tg


def main():
    token_file = os.environ.get('TOKEN_FILE', 'token.txt')
    with open(token_file) as tok:
        TOKEN = tok.read().strip()

    stomp_connection = stomp.Connection([('localhost', 61613)])
    tg = Tg(TOKEN, stomp_connection)

    tg.run_forever()


if __name__ == '__main__':
    logging.getLogger('urllib3').setLevel(logging.INFO)
    logging.basicConfig(stream=sys.stderr,
                        level=logging.DEBUG)
    main()

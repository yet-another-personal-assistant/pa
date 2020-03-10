#!/usr/bin/env python3
from tg import Tg


def main():
    with open('token.txt') as tok:
        TOKEN = tok.read().strip()

    tg = Tg(TOKEN)
    tg.run_forever()


if __name__ == '__main__':
    main()

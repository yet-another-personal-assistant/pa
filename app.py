#!/usr/bin/env python3
import os


from tg import Tg


def main():
    token_file = os.environ.get('TOKEN_FILE', 'token.txt')
    with open(token_file) as tok:
        TOKEN = tok.read().strip()

    tg = Tg(TOKEN)
    tg.run_forever()


if __name__ == '__main__':
    main()

# Yet another personal assistant

Currently this is just a Telegram bot that doesn't understand anything
(and says so).

### Configuration

The application requires a file containing the telegram bot token. If
`TOKEN_FILE` environment variable is defined it should be the path to
token file. Otherwise use a `token.txt` file in the current working
directory.

### Communication

PA-TG communication protocol is based on [PA infrastructure protocol].

Currently the PA instance name is hardcoded to be "niege".

PA-TG connects to STOMP server using the following connection
parameters:

- host: localhost
- port: 61613
- username: N/A
- password: N/A
- queue: "tg"


[PA infactructure protocol]: https://gitlab.com/personal-assistant-bot/infrastructure/protocol

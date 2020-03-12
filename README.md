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

#### `from-tg` messages

For each private text message received from Telegram PA-TG sends to
brain a message using the following format:

- `to`: `{"media": "brain", "name": "niege"}`
- `from`: `{"media": "tg", "user_id": "<user_id>"}`
- `text`: `"<message text>"`

Non-private or non-text messages are silently discarded.

#### `from-brain` messages

PA-TG accepts messages from brain in the following format:

- `to`: `{"media": "tg", "chat_id": "<chat_id>"}`
- `from`: `{"media": "brain", "name": "niege"}`
- `text`: one message or a list of messages to be sent


[PA infactructure protocol]: https://gitlab.com/personal-assistant-bot/infrastructure/protocol

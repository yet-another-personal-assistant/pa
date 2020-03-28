# Yet another personal assistant

Currently this is just a Telegram bot that doesn't understand anything
(and says so).

### Communication

PA-TG communication protocol is based on [PA infrastructure protocol].

Currently the PA instance name is hardcoded to be "niege".

PA-TG connects to STOMP server using the following connection
parameters:

- username: N/A
- password: N/A
- queue: "tg"

### Command-line arguments

- `-d`, `--debug`: use DEBUG logging level (default INFO)
- `-c`, `--config-file`: path to configuration file (default "/etc/pa.conf")
- `-t`, `--token-file`: path to telegram token file (if not specifed
  here it is expected to be set in config file)

### Configuration

Configuration file uses ini-file format with the following sections:

- `pa`
- `stomp`

#### PA

- `debug`: if set to true enables debug output (same as `-d` command-line argument)
- `token_file`: path to telegram token file

#### STOMP

- `host`: STOMP server address (default "localhost")
- `port`: STOMP server port (default 61613)
- `heartbeat_in` and `heartbeat_out`: heartbeat settings (default 0 -- disabled)

[PA infactructure protocol]: https://gitlab.com/personal-assistant-bot/infrastructure/protocol

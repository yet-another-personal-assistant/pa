# Yet another personal assistant

Currently this is just a Telegram bot that doesn't understand anything (and says so).

The code is ready to be deployed on heroku and might not work properly anywhere else.

### Heroku configuration

The following config variables have to be set:

- `BOT_TOKEN` -- telegram bot token
- `HEROKU_URL` -- set it to the application domain so that webhook could be set
- `BOT_SET_WEBHOOK` -- should be defined

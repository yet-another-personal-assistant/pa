import telepot
import telepot.loop


class Tg:

    def __init__(self, token):
        self.bot = telepot.Bot(token)

    def handle(self, msg):
        sender = msg['from']['id']
        chat = msg['chat']['id']
        if msg['chat']['type'] == 'private':
            self.bot.sendMessage(chat, "Я не поняла")
            self.bot.sendMessage(chat, f"А что значит \"{msg['text']}\"?")

    def run_forever(self):
        self.bot.deleteWebhook()
        telepot.loop.MessageLoop(self.bot, self.handle).run_forever()

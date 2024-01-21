import mrcs

class PingBot(mrcs.Client):
    def __init__(self) -> None:
        super().__init__("pb#ping | PingBot")

    def on_text_message(self, user: mrcs.User, content: str):
        if content == "pb#ping":
            self.send_text_message("Pong!")

pingbot = PingBot()
pingbot.run()
try:
    while True:
        pass
finally:
    pingbot.stop()

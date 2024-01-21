import mrcs

mrcs.constants.WS_URL = "put your websocket URL here"

class PrefixBotTest(mrcs.PrefixBot):
    def __init__(self) -> None:
        super().__init__("TestBot | e!help", "e!")
        self.add_command("help", self.help_command)
    
    def help_command(self, user: mrcs.User, arguments: list[str]) -> None:
        self.send_text_message(f"Hello, {user.username}! This is a bot made with [MRCS.py](https://github.com/GEOEGII555/mrcs.py).\nThis help command is from an example (3-prefix-bot.py). Arguments that you've passed to this command: {arguments}")

prefixBot = PrefixBotTest()
prefixBot.run()
try:
    while True:
        pass
finally:
    prefixBot.stop()

# Getting started.
Making a bot with mrcs.py is very simple:
```py
import mrcs

bot = mrcs.Client("bot name") # if you need a login key, mrcs.Client("bot name", "put your login key here")
bot.run()
# do something else, avoid the program from getting stopped.
try:
    while True:
        pass
finally:
    bot.stop()
```
The `Client().run()` function returns after the bot connects, which allows you to do other things.
If you aren't doing anything else, you can create a simple loop that does... nothing.
Another function (I'll probably name it `run_until_stopped()`) will be added, so that you won't have to make an infinite loop.

## Subclassing Client and PrefixBot.
You might need to subclass Client in order to add functionality to your bot. For example:
```py
class Bot(mrcs.Client):
    def __init__(self) -> None:
        super().__init__("CoolTestBot")

    def on_text_message(self, user: mrcs.User, content: str) -> None:
        print(user.username, "->", content)
```
To make adding commands easier, I've also implemented PrefixBot. Subclassing it looks like this:
```py
class MyPrefixBot(mrcs.PrefixBot):
    def __init__(self) -> None:
        super().__init__("TestBot | e!help", "e!")
        self.add_command("help", self.help_command)
    
    def help_command(self, user: mrcs.User, arguments: list[str]) -> None:
        # ...
        pass
```
We also have a built in help command in PrefixBot. See `PrefixBot().add_builtin_help()` for more info. (call it in the constructor)
You can see more info on events and functions in the documentation.

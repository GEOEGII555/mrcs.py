import mrcs

mrcs.constants.WS_URL = "put your websocket URL here"

client = mrcs.Client("doNothingBot")
client.run()
try:
    while True:
        pass
finally:
    client.stop()

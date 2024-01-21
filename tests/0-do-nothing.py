import mrcs

client = mrcs.Client("doNothingBot")
client.run()
try:
    while True:
        pass
finally:
    client.stop()
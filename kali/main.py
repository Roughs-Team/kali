from bot import bot
from handlers import labelers


for labeler in labelers:
    bot.labeler.load(labeler)


bot.run_forever()

def start():
    bot.run_forever()
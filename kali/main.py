from bot import bot
from handlers import labelers
from loguru import logger
from confug_loguru import config_loguru

for labeler in labelers:
    bot.labeler.load(labeler)

config_loguru()
logger.info("Starting the bot...")
bot.run_forever()


from vkbottle.bot import BotLabeler, Message

from rules.text import TextRule

labeler = BotLabeler()
used_commands = ['пинг']

@labeler.message(TextRule('пинг'))
async def bye_handler(message: Message):
    await message.answer("ПОНГ")
from rules.text import TextRule
from vkbottle.bot import BotLabeler, Message

labeler = BotLabeler()
used_commands = ["пинг"]


@labeler.message(TextRule("пинг"))
async def bye_handler(message: Message):
    await message.answer("ПОНГ")

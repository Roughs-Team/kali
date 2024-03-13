import re

from bot import bot
from rules.text import TextRule, CommandRule

from vkbottle.bot import BotLabeler, Message
from vkbottle.dispatch.rules.base import PeerRule

labeler = BotLabeler()
used_commands = ['бан', 'кик']

@labeler.message(TextRule(['бан', 'кик']), PeerRule(from_chat=True))
async def ban_handler(message: Message):
    if not message.reply_message:
        await message.answer("Перешлите сообщение пользователя, которого хотите забанить или отметьте его в сообщении.")
        return
    await bot.api.messages.remove_chat_user(
        chat_id=message.peer_id - 2000000000,
        member_id=message.reply_message.from_id
    )
    await message.answer("Пользователь забанен")


@labeler.message(CommandRule(['бан', 'кик']), PeerRule(from_chat=True))
async def ban_handler(message: Message):
    match = re.search(r'\[(id|club|group)(\d+)\|', message.text)
    if not match:
        await message.answer("Перешлите сообщение пользователя, которого хотите забанить или отметьте его в сообщении.")
        return
    user_id = int(match.group(2))
    await bot.api.messages.remove_chat_user(
        chat_id=message.peer_id - 2000000000,
        member_id=user_id
    )
    await message.answer("Пользователь забанен")


import re
import aiohttp
import random
from vkbottle.bot import BotLabeler, Message

import config
from bot import bot
from data.stickers import stickers
from rules.text import ChitChatRule

labeler = BotLabeler()

sber_url = 'https://api.aicloud.sbercloud.ru/public/v2/boltalka/predict'
context = {}

EMOJI_PATTERN = re.compile(
    r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+"
)

def remove_emoji(text) -> str:
    text = EMOJI_PATTERN.sub(". ", text)
    text = text.replace(" .", ".")
    while text.endswith(".") or text.endswith(" "):
        text = text[:-1]
    return text


def format_response(text: str) -> str:
    text = text.replace("%bot_name", config.BOT_NAME)
    text = remove_emoji(text)
    return text


def find_emoji(text) -> str | None:
    match = EMOJI_PATTERN.search(text)
    if match:
        return match.group(0)
    return None


def get_sticker(word) -> int | None:
    for sticker in stickers["response"]["dictionary"]:
        if word in sticker["words"]:
            return random.choice(sticker["stickers"])["sticker_id"]
    return None


async def get_answer(text: str, peer_id: int):
    try:
        context[str(peer_id)].append(text)
    except KeyError:
        context[str(peer_id)] = [text]

    data = {"instances": [{"contexts": [context[str(peer_id)]]}]}
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        async with session.post(sber_url, json=data, headers=headers) as resp:
            response = await resp.json()
            answer = response['responses'].split("['")[1].split("']")[0]
    
    context[str(peer_id)].append(answer)
    context[str(peer_id)] = context[str(peer_id)][-10:]
    return answer

def generate_reply(message: Message):
    return '{' + f'"peer_id": {message.peer_id}, "conversation_message_ids": [{message.conversation_message_id}], \
        "is_reply": 1' + '}'

@labeler.message(ChitChatRule())
async def chitchat_handler(message: Message):

    await bot.api.messages.set_activity(peer_id=message.peer_id, type="typing")

    answer = await get_answer(message.text, message.peer_id)
    if message.from_id == message.peer_id:
        await message.answer(format_response(answer))
    else:
        await message.answer(format_response(answer), forward=generate_reply(message))

    emoji = find_emoji(answer)
    if emoji:
        sticker = get_sticker(emoji)
        if sticker:
            await message.answer("", sticker_id=sticker)
    else:
        for word in answer.lower().split():
            sticker = get_sticker(word)
            if sticker:
                await message.answer("", sticker_id=sticker)
                break
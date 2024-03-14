import re
from vkbottle.dispatch.rules.abc import ABCRule
from vkbottle.tools.dev.mini_types.base import BaseMessageMin

import config


class TextRule(ABCRule[BaseMessageMin]):
    def __init__(self, text: str | tuple[str]):
        if isinstance(text, str):
            text = [text]
        self.text = [i.lower() for i in text]

    async def check(self, message: BaseMessageMin) -> bool:
        return message.text.lower() in self.text


class CommandRule(ABCRule[BaseMessageMin]):
    def __init__(self, command: str | tuple[str]):
        if isinstance(command, str):
            command = [command]
        self.command = [i.lower() for i in command]

    async def check(self, message: BaseMessageMin) -> bool:
        return message.text.lower().split(" ")[0] in self.command


class ChitChatRule(ABCRule[BaseMessageMin]):
    async def check(self, message: BaseMessageMin) -> bool:
        id_match = re.search(r"\[(id|club|group)(\d+)\|", message.text)
        id_from_message = int(id_match.group(2)) if id_match else None

        return (
            message.from_id == message.peer_id
            or message.text.lower().startswith(config.BOT_NAME.lower() + ",")
            or message.text.lower().startswith(config.BOT_NAME.lower() + " ")
            or message.reply_message.from_id == -config.VK_GROUP_ID
            or id_from_message == config.VK_GROUP_ID
        )

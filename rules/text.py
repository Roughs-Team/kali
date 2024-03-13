import config

from typing import Tuple, Union

from vkbottle.dispatch.rules.abc import ABCRule
from vkbottle.tools.dev.mini_types.base import BaseMessageMin


class TextRule(ABCRule[BaseMessageMin]):
    def __init__(self, text: Union[str, Tuple[str]]):
        if isinstance(text, str):
            text = [text]
        self.text = [i.lower() for i in text]

    async def check(self, message: BaseMessageMin) -> bool:
        return message.text.lower() in self.text
    

class CommandRule(ABCRule[BaseMessageMin]):
    def __init__(self, command: Union[str, Tuple[str]]):
        if isinstance(command, str):
            command = [command]
        self.command = [i.lower() for i in command]

    async def check(self, message: BaseMessageMin) -> bool:
        return message.text.lower().split(' ')[0] in self.command
    

class ChitChatRule(ABCRule[BaseMessageMin]):
    async def check(self, message: BaseMessageMin) -> bool:

        if message.from_id == message.peer_id:
            print('True'*100)
            return True

        elif message.text.lower().startswith(config.BOT_NAME.lower()+',') or message.text.lower().startswith(config.BOT_NAME.lower()+' '):
            return True
        elif message.reply_message.from_id == -config.VK_GROUP_ID:
            return True
        
        return False
from . import (
        ping,
        ban,
        chitchat
    )

labelers = [
        ping.labeler,
        ban.labeler,
        chitchat.labeler
    ]

__all__ = ["labelers"]
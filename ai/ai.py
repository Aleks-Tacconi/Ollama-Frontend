from typing import List
from typing import Iterator

import ollama

from .message import Message


class AI:
    def __init__(self, model: str) -> None:
        self.__model = model

    def query(self, messages: List[Message]) -> Iterator:
        formatted_messages = [
            {
                "role": message.role,
                "content": message.content + "\n\nanswer as if you are helping someone.", 
            }
            for message in messages
        ]

        response = ollama.chat(
            model=self.__model,
            messages=formatted_messages,
            stream=True,
        )

        return response

from typing import Iterator

import streamlit as st

from ai import AI
from ai import Message


class Website:
    def __init__(self, model_name: str) -> None:
        if "messages" not in st.session_state:
            st.session_state.messages = []

        self.__ai = AI(model_name)

    def __render_message(self, message: Message) -> None:
        with st.chat_message(message.role):
            st.markdown(message.content, unsafe_allow_html=True)

    def __render_previous_messages(self) -> None:
        for message in st.session_state.messages:
            self.__render_message(message)

    def __stream(self, stream: Iterator):
        for message in stream:
            msg = message.message.content
            msg = msg.replace("<think>", "")
            msg = msg.replace("</think>", "")

            yield msg

    def __handle_prompt(self, prompt: str) -> None:
        message = Message(prompt, "user")
        st.session_state.messages.append(message)
        self.__render_message(message)

        stream = self.__ai.query(st.session_state.messages)

        with st.chat_message("assistant"):
            response = st.write_stream(self.__stream(stream))

        message = Message(response, "assistant")
        st.session_state.messages.append(message)

    def __listen(self) -> None:
        if prompt := st.chat_input("Type your message..."):
            self.__handle_prompt(prompt)

    def main(self) -> None:
        self.__render_previous_messages()
        self.__listen()

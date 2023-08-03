import reflex as rx
import asyncio

class State(rx.State):
    question: str

    chat_history: list[tuple[str,str]]

    async def answer(self):
        answer = "I don't know bud 😵"
        self.chat_history.append((self.question,answer))
        for i in range(len(answer)):
            await asyncio.sleep(0.1)
            self.chat_history[-1] = (self.question,answer[:i])
            yield
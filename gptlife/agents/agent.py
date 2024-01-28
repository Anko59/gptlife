import abc
from typing import List, Tuple, Any, Type
from gptlife.games.mystery_mansion.constants import Role
from gptlife.games.map import Room

from gptlife.games.action import Action
from gptlife.agents.personality import Personality
from gptlife.utils import parse_output, get_current_time
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import time
import os
import random


class AbstractAgent(abc.ABC):
    def __init__(self, role: Role, current_room: Room, personality_type: Type[Personality]) -> None:
        self.personality = personality_type.generate_random_personality()
        self.name = self.personality.name
        self.role = role
        self.is_alive = True
        self.current_room = current_room
        self.memory: list[str] = []
        self.inventory: list[str] = []

    def __str__(self):
        return f"Agent(name={self.name}, role={self.role}, is_alive={self.is_alive}, current_room={self.current_room.name}, memory={self.memory})"

    def listen(self, sentence: str) -> None:
        self.memory.append(get_current_time() + ': ' + sentence[0:180])

    @abc.abstractmethod
    def get_action(self, legal_actions: List[Tuple[Action, Any]], prompts: list[dict[str, str]]) -> Tuple[Action, Any]:
        pass

    def __str__(self):
        return f"Agent(name={self.name}, role={self.role}, is_alive={self.is_alive}, current_room={self.current_room.name}, memory={self.memory})"


class MistraltAgent(AbstractAgent):

    api_key = os.environ["MISTRAL_API_KEY"]
    client = MistralClient(api_key=api_key)

    def __init__(self, role: Role, current_room: Room, personality_type: Type[Personality]) -> None:
        super().__init__(role, current_room, personality_type)
        self.model = "mistral-medium"
        self.response_memory = []

    def get_action(self, legal_actions: List[Tuple[Action, Any]], prompts: list[dict[str, str]]) -> Tuple[Action, Any]:
        messages = [
            ChatMessage(role=prompt['role'], content=prompt['content'])
            for prompt in prompts
        ]
        chat_response = self.client.chat(
            model=self.model,
            messages=messages,
            max_tokens=50,
            temperature=random.random()
        )
        self.response_memory.append(chat_response.choices[0].message.content)
        action, target = parse_output(
            chat_response.choices[0].message.content, legal_actions)
        return action, target

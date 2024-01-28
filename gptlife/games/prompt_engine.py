from abc import ABC
from gptlife.agents.agent import AbstractAgent
from gptlife.games.action import Action
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gptlife.games.game import AbstractGame


class PromptEngine(ABC):
    personality_prompt_template: str
    rules_prompt_template: str
    memory_prompt_template: str
    legal_actions_prompt_template: str

    @classmethod
    def get_personality_prompt(cls, game: 'AbstractGame', agent: AbstractAgent, legal_actions: list[Action]):
        return cls.personality_prompt_template

    @classmethod
    def get_rules_prompt(cls, game: 'AbstractGame', agent: AbstractAgent, legal_actions: list[Action]):
        return cls.rules_prompt_template

    @classmethod
    def get_memory_prompt(cls, game: 'AbstractGame', agent: AbstractAgent, legal_actions: list[Action]):
        return cls.memory_prompt_template

    @classmethod
    def get_legal_actions_prompt(cls, game: 'AbstractGame', agent: AbstractAgent, legal_actions: list[Action]):
        return cls.legal_actions_prompt_template

    @classmethod
    def get_prompts(cls, game: 'AbstractGame', agent: AbstractAgent, legal_actions: list[Action]) -> list[dict[str: str]]:
        return [
            {
                "role": "system",
                "content": cls.get_personality_prompt(game, agent, legal_actions)
            },
            {
                "role": "system",
                "content": cls.get_rules_prompt(game, agent, legal_actions)
            },
            {
                "role": "system",
                "content": cls.get_memory_prompt(game, agent, legal_actions)
            },
            {
                "role": "user",
                "content": cls.get_legal_actions_prompt(game, agent, legal_actions)
            }
        ]

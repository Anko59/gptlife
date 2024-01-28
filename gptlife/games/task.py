from typing import Optional
from gptlife.agents.agent import AbstractAgent
from gptlife.games.game import AbstractGame


class Task:
    def __init__(
        self,
        name: str,
        condition_function: callable,
        success_message_template: Optional[str] = None,
        failure_message_template: Optional[str] = None
    ) -> None:

        self.name = name
        self.condition_function = condition_function
        self.completed = False

        if success_message_template is None:
            success_message_template = "{agent.name} has completed the task {task.name}"
        self.success_message_template = success_message_template

        if failure_message_template is None:
            failure_message_template = "{agent.name} cannot currently complete the task {task.name}."
        self.failure_message_template = failure_message_template

    def failure_message(self, game: AbstractGame, agent: AbstractAgent) -> str:
        return self.failure_message_template.format(agent=agent, task=self)

    def success_message(self, game: AbstractGame, agent: AbstractAgent) -> str:
        return self.success_message_template.format(agent=agent, task=self)

    def perform(self, game: AbstractGame, agent: AbstractAgent) -> None:
        if self.condition_function(game, agent):
            self.completed = True
            game.broadcast_message(agent, self.success_message(game, agent))
        else:
            game.broadcast_message(agent, self.failure_message(game, agent))

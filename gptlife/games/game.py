import random
from typing import List, Tuple, Type
from gptlife.games.mystery_mansion.constants import Role, ROLE_COLORS
from gptlife.agents.personality import Personality
from gptlife.games.map import Map
from gptlife.games.prompt_engine import PromptEngine
from gptlife.agents.agent import AbstractAgent
from gptlife.games.action import Action
from gptlife.games.map import Room
from abc import ABC, abstractmethod
import networkx as nx
import pickle


class AbstractGame(ABC):
    def __init__(
        self,
        AgentClass: Type[AbstractAgent],
        roles: dict[Role, int],
        map: Map,
        prompt_engine: PromptEngine,
        role_personality_map: dict[Role, Type[Personality]] = None
    ) -> None:
        self.map = map
        self.role_personality_map = role_personality_map
        self.agents = self._genrate_agents(AgentClass, roles)
        self.turn_number: int = 0
        self.prompt_engine = prompt_engine
        self.graphs = []

    @property
    def alive_agents(self):
        return [x for x in self.agents if x.is_alive]

    def _genrate_agents(self, AgentClass: Type[AbstractAgent], roles: dict[Role, int]) -> list[AbstractAgent]:
        agents = []
        for role, role_nr in roles.items():
            for _ in range(role_nr):
                agents.append(AgentClass(
                    role=role,
                    current_room=self.map.get_random_room(),
                    personality_type=self.role_personality_map[role]
                ))
        return agents

    @abstractmethod
    def get_legal_actions(self, agent: AbstractAgent) -> List[Tuple[Action, str]]:
        pass

    @abstractmethod
    def check_win(self) -> bool:
        pass

    def turn(self):
        self.turn_number += 1

        for agent in self.alive_agents:
            if not agent.is_alive:
                continue
            legal_actions = self.get_legal_actions(agent)
            prompts = self.prompt_engine.get_prompts(
                self, agent, legal_actions)
            action, target = agent.get_action(legal_actions, prompts)
            action.perform(self, agent, target)
            # Generate the graph of the mansion
            mansion_graph = self.map.generate_turn_map_graph(self)
            # Store the graph in memory or any data structure of your choice
            # For example, you can create a list to store all the graphs
            self.graphs.append(mansion_graph)
            random.shuffle(self.agents)
            if self.check_win():
                break
        print(f'End of turn {self.turn_number}.')

    def run(self):
        while not self.check_win():
            self.turn()
        with open("game_graphs.pkl", "wb") as file:
            pickle.dump(self.graphs, file)
        
    def broadcast_message(self, agent: AbstractAgent, message: str, room: Room = None, verbose: bool = True) -> int:
        room = room if room else agent.current_room
        witnesses = 0
        for other_agent in self.alive_agents:
            if other_agent.current_room == room:
                other_agent.listen(message)
                witnesses += 1
        if verbose:
            role_color = ROLE_COLORS.get(agent.role, "white")
            print(f"\033[1;{role_color}m{message}\033[0m",
                  f' --- Heard by {witnesses} agents in {room.name}')
        return witnesses

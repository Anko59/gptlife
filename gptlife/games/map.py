from typing import List, Optional
import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gptlife.games.task import Task
    from gptlife.games.game import AbstractGame
import networkx as nx
from enum import Enum
import matplotlib.pyplot as plt
from gptlife.games.mystery_mansion.constants import Role


ROLE_COLORS = {
    Role.KILLER: "red",
    Role.INNOCENT: "blue",
    Role.POLICEMAN: "green",
    Role.ARCHITECT: "orange",
    Role.DEVIL: "purple"
}


class Room:
    def __init__(self, name: str, task: 'Task', connected_rooms: Optional[List['Room']] = None, items: Optional[List[str]] = None):
        self.name = name
        self.task = task
        self.connected_rooms = connected_rooms if connected_rooms is not None else []
        self.items = items if items is not None else []

    def perform_task(self, game, agent):
        self.task.perform(game, agent)


class Map:
    def __init__(self):
        self.rooms = {}
        self.G = nx.Graph()

    def add_room(self, name: str, task: 'Task'):
        self.rooms[name] = Room(name, task)
        self.G.add_node(name)

    def connect_rooms(self, room_name: str, connected_room_names: List[str]):
        self.rooms[room_name].connected_rooms = [self.rooms[name]
                                                 for name in connected_room_names]
        for connected_room_name in connected_room_names:
            self.G.add_edge(room_name, connected_room_name)

    def get_random_room(self) -> Room:
        return random.choice(list(self.rooms.values()))

    def init_map_graph(self):
        self.pos = nx.spring_layout(self.G)

    def generate_turn_map_graph(self, game: 'AbstractGame') -> nx.Graph:
        plt.clf()
        nx.draw(self.G, self.pos, with_labels=True, node_size=1000,
                node_color='lightblue', font_weight='bold')

        for room_name, room in self.rooms.items():
            x, y = self.pos[room_name]
            y = y - 0.05

            if room.task.completed:
                node_color = 'lightgreen'
            else:
                node_color = 'red'

            for agent in game.alive_agents:
                if agent.current_room == room:
                    agent_name = agent.name
                    agent_role = agent.role
                    y = y - 0.04
                    if agent.inventory:
                        agent_items = ', '.join(agent.inventory)
                        plt.text(x, y, f"{agent_name} ({agent_items})",
                                 ha='center', va='center', color=ROLE_COLORS[agent_role])
                    else:
                        plt.text(x, y, f"{agent_name}",
                                 ha='center', va='center', color=ROLE_COLORS[agent_role])

            room_items = ', '.join(room.items) if room.items else ""
            plt.text(x, y - 0.04, f"Items: {room_items}",
                     ha='center', va='center', color='black')

            nx.draw_networkx_nodes(
                self.G, self.pos, nodelist=[room_name], node_color=node_color, node_size=2000, alpha=0.8)

        # Display the number of people still alive
        num_alive = len(game.alive_agents)
        plt.text(0.95, 0.95, f"Alive: {num_alive}",
                 ha='right', va='top', transform=plt.gca().transAxes, color='black')

        # Display the turn number
        plt.text(0.05, 0.95, f"Turn: {game.turn_number}",
                 ha='left', va='top', transform=plt.gca().transAxes, color='black')

        # Display the number of tasks remaining
        num_tasks_remaining = sum(1 for room in self.rooms.values() if not room.task.completed)
        plt.text(0.05, 0.05, f"Tasks Remaining: {num_tasks_remaining}",
                 ha='left', va='bottom', transform=plt.gca().transAxes, color='black')

        plt.show(block=False)
        plt.pause(0.1)

        return self.G

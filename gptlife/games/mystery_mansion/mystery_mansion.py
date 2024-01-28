from typing import List, Tuple
from gptlife.games.mystery_mansion.constants import Role
from gptlife.games.mystery_mansion.mansion_map import generate_map
from gptlife.games.action import Action
from gptlife.games.mystery_mansion.mystery_prompt_engine import MysteriousPromptEngine
import gptlife.games.mystery_mansion.mysterious_actions as actions
from gptlife.agents.agent import MistraltAgent, AbstractAgent
from gptlife.agents.personality import Personality, DevilPersonality
from gptlife.games.game import AbstractGame


class MysteriousMansionGame(AbstractGame):
    def __init__(self):
        super().__init__(
            AgentClass=MistraltAgent,
            roles={
                Role.POLICEMAN: 3,
                Role.ARCHITECT: 4,
                Role.INNOCENT: 16,
                Role.KILLER: 1,        
            },
            map=generate_map(),
            prompt_engine=MysteriousPromptEngine(),
            role_personality_map={
                Role.KILLER: Personality,
                Role.INNOCENT: Personality,
                Role.POLICEMAN: Personality,
                Role.ARCHITECT: Personality,
                Role.DEVIL: DevilPersonality
            }
        )
        print(
            '\n'.join(
                [f'{p.name}:, {p.role.value}' for p in self.agents]
            )
        )

    def get_legal_actions(self, person: AbstractAgent) -> List[Tuple[Action, str]]:
        possible_actions: List[Tuple[Action, str]] = [
            (actions.TALK, "Any message can be talked by the player.")]
        for room in person.current_room.connected_rooms:
            possible_actions.append((actions.MOVE, room.name))
        if person.role == Role.KILLER or person.role == Role.POLICEMAN:
            other_agents_in_room = [p for p in self.alive_agents if p != person 
                                    and p.current_room == person.current_room]
            for other_person in other_agents_in_room:
                if person.role == Role.KILLER:
                    possible_actions.append((actions.KILL, other_person.name))
                elif person.role == Role.POLICEMAN:
                    possible_actions.append((actions.ARREST, other_person.name))
        if person.role == Role.INNOCENT:
            for item in person.current_room.items:
                possible_actions.append((actions.PICK_ITEM, item))
            if not person.current_room.task.completed:
                possible_actions.append(
                    (actions.COMPLETE_TASK, person.current_room.task.name))
        
        return possible_actions

    def check_win(self) -> bool:
        if all(room.task.completed for room in self.map.rooms.values()):
            print("Innocents have won by completing all tasks!")
            return True
        elif len([p for p in self.alive_agents if p.role != Role.KILLER]) == 0:
            print("Killers have won by killing everyone!")
            return True
        # elif len([p for p in self.alive_agents if p.role == Role.KILLER]) == 0:
        #     print("Policemen have won by arresting every killer!")
        #     return True
        elif self.turn_number >= 20:
            print("Time expired, no winner")
            return True
        return False

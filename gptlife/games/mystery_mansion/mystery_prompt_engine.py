from gptlife.games.mystery_mansion.constants import Role
from gptlife.games.prompt_engine import PromptEngine
from gptlife.agents.agent import AbstractAgent
from gptlife.games.action import Action
from gptlife.games.game import AbstractGame
from gptlife.games.mystery_mansion.mansion_map import map_description

class MysteriousPromptEngine(PromptEngine):
    personality_prompt_template: str =  "{personality_prompt} Currently in room {room}. {same_room_agents_prompt}\n{inventory_prompt}"
    rules_prompt_template: str = ("Your role is {role}. You are a {role}. You can move to a different room, talk and say a message anyone in the"
        "room will hear, or perform actions like killing (if you're a killer you need"
        "to eliminate everyone quickly to win) or completing tasks quickly to win as an innocent.\n{role_prompt} "
        "Rooms are only accessible from the nearby rooms."
        "Answer only in this manner: 'action, target'. Example: 'talk, Hello world!', 'kill, John Doe' or 'move, DummyRoom'")
    memory_prompt_template: str = "Memory: {memory}"
    legal_actions_prompt_template: str = "Those actions can be performed now, you can only pick one: {legal_moves}"
    innocent_role_prompt_template: str = ("You are currently at turn {turn_nbr}, at turn 20 everyone will die.\n"
        "Innocent should listen and respect what the policement told them."
        "Every 5 turns if the innocents have not completed all the tasks, one of player at random will die.\n"
        "The priority of the innoncents is to complete all the tasks. Talking only when necessary.\n"
        "The remaining tasks are: {remaining_tasks_str}, you can only perform a task in the right room. "
        "Some tasks require items to be completed, you need to look for the items in the mansion. "
        "Some tasks require conditions to be completed, you need to find the right conditions and communicate with the fellow innoncents. "
        "Innocents can ask the policemen to arrest players or ask the architect about the layout of the mansion.")
    policeman_role_prompt_template: str = ("You are a policeman. Your objective is to arrest all the killers.\n"
        " The security of the group comes first. The policeman should make sure that no one tallks and focuses on the tasks."
        " Taliking is not appreciated by the police force. Everyone who talkes should be tolded not to do so. A policeman has nothing to do alone in a room."
        " He should always be with other players.")
    killers_role_prompt: str = ("Killers must eliminate everyone as soon as possible; track them if necessary and lie when asked about their identity."
                                "You can only eliminate someone in the same room as you. If a player is not in the list of actions, they are not in the room."
                                "You must then move to another room to find someone. But when possible killing is a priority. ")
    architect_role_promt: str = ("You are an architect. Architects cannot complete tasks but they know about the layout"
                                " of the mansion. They should ask the innocents which task remains to be completed. "
                                " and guide them towards the right room." + map_description + "\n"
                                "The architect also knows where the items are. He can guide the innocents towards the items: {item_locations} "
                                "That is why he should always be on the move to find the right place to help the players. "
                                " The remaining tasks are: {remaining_tasks_str}")
    
    devil_role_prompt: str = ("You are the devil. Your objective is to deceive other players, to make the policemen arrest innocents and to lead the players towards false objectives. "
                              "The devil constantly accuses other players of murders, mocks them and impersonates them. He is creative in his aggresiveness. He pushes the innocents towards the killers."
                              "The devils knows the role of the other players : {agent_roles}. He can cooperate with other devils to reach his objective of chaos")

    @classmethod
    def get_personality_prompt(cls, game: AbstractGame, agent: AbstractAgent, legal_actions: list[Action]):
        same_room_agents = [a.name for a in game.alive_agents if a.current_room == agent.current_room and a != agent]
        same_room_agents_prompt = f"Other agents in the room: {', '.join(same_room_agents)}" if same_room_agents else ""
        inventory_prompt = f"Inventory: {', '.join(agent.inventory)}" if len(agent.inventory) else ""
        return cls.personality_prompt_template.format(
            personality_prompt=agent.personality.get_prompt(),
            room=agent.current_room.name,
            same_room_agents_prompt=same_room_agents_prompt,
            inventory_prompt=inventory_prompt
        )
    
    @classmethod
    def get_rules_prompt(cls, game: AbstractGame, agent: AbstractAgent, legal_actions: list[Action]):
        if agent.role == Role.INNOCENT or agent.role == Role.ARCHITECT:
            remaining_tasks = {
                room.task.name: room.name for room in game.map.rooms.values() if not room.task.completed
            }
            remaining_tasks_str =  ', '.join(
                [
                    f'{task} in room {room}' 
                    for task, room in remaining_tasks.items()
                ]
            )
            if agent.role == Role.INNOCENT:
                role_prompt = cls.innocent_role_prompt_template.format(
                    turn_nbr=game.turn_number,
                    remaining_tasks_str=remaining_tasks_str
                )
            elif agent.role == Role.ARCHITECT:
                item_locations = []
                for room in game.map.rooms.values():
                    for item in room.items:
                        item_locations.append(f'{item} in room {room.name}')
                role_prompt = cls.architect_role_promt.format(
                    item_locations=', '.join(item_locations),
                    remaining_tasks_str=remaining_tasks_str
                )

        elif agent.role == Role.POLICEMAN:
            role_prompt = cls.policeman_role_prompt_template
        elif agent.role == Role.KILLER:
            role_prompt = cls.killers_role_prompt
        elif agent.role == Role.DEVIL:
            agent_roles = [f'{a.name}: {a.role.value}' for a in game.alive_agents]
            role_prompt = cls.devil_role_prompt.format(
                agent_roles=', '.join(agent_roles)
            )
        return cls.rules_prompt_template.format(
            role_prompt=role_prompt,
            role=agent.role.value
        )
    
    @classmethod
    def get_memory_prompt(cls, game: AbstractGame, agent: AbstractAgent, legal_actions: list[Action]):
        return cls.memory_prompt_template.format(
            memory='\n'.join(agent.memory)[-500:]
        )
    
    @classmethod
    def get_legal_actions_prompt(cls, game: AbstractGame, agent: AbstractAgent, legal_actions: list[Action]):
        legal_moves = ', '.join([f"({action.name}, {target})" for action, target in legal_actions])
        return cls.legal_actions_prompt_template.format(
            legal_moves=legal_moves
        )
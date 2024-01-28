import random
from copy import copy

from gptlife.games.action import Action, ActionError
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from gptlife.games.game import AbstractGame
    from gptlife.agents.agent import AbstractAgent
from gptlife.games.mystery_mansion.constants import Role


def talk_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    message = f'{agent.name} said: "{target}"'
    game.broadcast_message(agent, message)
    for room in agent.current_room.connected_rooms:
        if random.random() > 0.5:
            game.broadcast_message(
                agent, message + f' in {agent.current_room.name}', room, verbose=False)


def move_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    current_room = copy(agent.current_room)
    room = game.map.rooms[target]
    if room in agent.current_room.connected_rooms:
        agent.current_room = room
    else:
        raise ActionError
    game.broadcast_message(
        agent, f'{agent.name} has left the room {current_room.name}.', current_room, verbose=False)
    game.broadcast_message(
        agent, f'{agent.name} has entered the room {agent.current_room.name}.')


def kill_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    target = [x for x in game.agents if x.name == target][0]
    if agent.role == Role.KILLER and target.is_alive and agent.current_room == target.current_room:
        target.is_alive = False
        agent.current_room.items.extend(target.inventory)
    else:
        raise ActionError
    message = f'{target.name} was killed by {agent.name} in front of your eyes'
    witnesses = game.broadcast_message(agent, message)
    for room in game.map.rooms.values():
        if room != agent.current_room:
            game.broadcast_message(
                agent,  f'{target.name} was killed in another room.', room, verbose=False)
    agent.listen(
        f'You killed {target.name}. There were {witnesses} witnesses.')


def complete_task_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    if agent.current_room and agent.current_room.task.completed == False:
        agent.current_room.task.perform(game, agent)
    else:
        raise ActionError


def arrest_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    target = [x for x in game.agents if x.name == target][0]
    if agent.role == Role.POLICEMAN and target.is_alive and agent.current_room == target.current_room:
        target.is_alive = False
        agent.current_room.items.extend(target.inventory)
        if target.role == Role.KILLER:
            game.broadcast_message(
                agent, f'Congratulations {agent.name}! You have arrested the killer {target.name}.')
        else:
            game.broadcast_message(
                agent, f'Shame on you {agent.name}! You have arrested an innocent person {target.name}.')
    else:
        raise ActionError


def failed_kill_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    if agent.role == Role.KILLER:
        game.broadcast_message(
            agent, f'{agent.name} tried to kill {target} but there is no one '
            'in the room. He revealed himself as a killer.')
    else:
        raise ActionError
    

def pick_item_action(game: 'AbstractGame', agent: 'AbstractAgent', target: str):
    if target in agent.current_room.items:
        agent.inventory.append(target)
        agent.current_room.items.remove(target)
        game.broadcast_message(
            agent, f'{agent.name} picked up a {target}. Maybe it can be used tp perform a task.')
    else:
        raise ActionError

ARREST = Action('arrest', arrest_action)
TALK = Action('talk', talk_action)
MOVE = Action('move', move_action)
KILL = Action('kill', kill_action)
COMPLETE_TASK = Action('complete_task', complete_task_action)
FAILED_KILL = Action('failed_kill', failed_kill_action)
PICK_ITEM = Action('pick_item', pick_item_action)

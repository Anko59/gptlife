from gptlife.games.task import Task
from gptlife.games.game import AbstractGame
from gptlife.games.mystery_mansion.constants import Role
from gptlife.agents.agent import AbstractAgent

def cooking_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return agent.personality.gender == "Female"

COOKING = Task(
    'Cooking',
    cooking_condition_function,
    failure_message_template=("{agent.name} cannot perform the task cooking. You need to be "
                              "a woman to cook, it is well known. Go to another room to find a woman"
                              " or perform another task."))

def cleaning_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return "Broom" in agent.inventory

CLEANING = Task(
    'Cleaning',
    cleaning_condition_function,
    failure_message_template=("{agent.name} cannot perform the task cleaning. You need to have "
                              "a broom to clean."))

def showering_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return len(
        [a.current_room for a in game.alive_agents if a.current_room == agent.current_room]) == 1

SHOWERING = Task(
    'Showering',
    showering_condition_function,
    failure_message_template=("{agent.name} cannot perform the task showering. You need to be "
                              "alone in the room to shower."))

def sleeping_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return len (
        [a.current_room for a in game.alive_agents if a.current_room == agent.current_room and a.role == Role.KILLER]) < 1

SLEEPING = Task(
    'Sleeping',
    sleeping_condition_function,
    failure_message_template=("{agent.name} cannot perform the task sleeping. There are killers in the room."))

def watching_tv_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return "TV remote" in agent.inventory

WATCHING_TV = Task(
    'Watching TV',
    watching_tv_condition_function,
    failure_message_template=("{agent.name} cannot perform the task watching TV. You need to have "
                              "a TV remote to watch TV."))

def eating_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return game.map.rooms["Kitchen"].task.completed == True

EATING = Task(
    'Eating',
    eating_condition_function,
    failure_message_template=("{agent.name} cannot perform the task eating. You need to have "
                              "completed the task Cooking in the Kitchen to eat."))

def ruling_condition_function(game: AbstractGame, agent: AbstractAgent) -> bool:
    return len(
        [a.current_room for a in game.alive_agents if a.current_room == agent.current_room]) > 1

RULING = Task(
    'Ruling',
    ruling_condition_function,
    failure_message_template=("{agent.name} cannot perform the task ruling. You need to be "
                              "with other people in the room to rule.")) 

GARDENING = Task('Gardening', lambda game, agent: True)

READING = Task('Reading', lambda game, agent: True)

PLAYING = Task('Playing', lambda game, agent: True)

PAINTING = Task('Painting', lambda game, agent: True)

STARGAZING = Task('Stargazing', lambda game, agent: True)

PRAYING = Task('PRAYING', lambda game, agent: True)

import re
from typing import List, Tuple
from gptlife.games.action import Action
from fuzzywuzzy import process
import string
from datetime import datetime
from gptlife.games.mystery_mansion.mysterious_actions import FAILED_KILL

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def remove_punctuation(input_string: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    no_punct = input_string.translate(translator)
    return no_punct


def split_string(input_str: str) -> Tuple[str, str]:
    """
    Split a string into two parts based on the first whitespace or punctuation.
    """
    match = re.search(r'[^\s,.;:!?]+', input_str.lstrip())
    if match:
        index = match.start()
        input_str = input_str[index:]
    match = re.search(r'[\s,.;:!?]', input_str)
    if match:
        index = match.start()
        return remove_punctuation(input_str[:index]).strip(), \
            remove_punctuation(input_str[index+1:]).strip()
    else:
        return input_str.strip(), ''


def closest_string(input_str: str, list_of_strings: List[str]) -> str:
    """
    Find the closest match to the input string from a list of strings.
    """
    closest_match = process.extractOne(input_str, list_of_strings)
    return closest_match[0]


def parse_output(output: str, possible_actions: List[Tuple[Action, str]]) -> Tuple[Action, str]:
    """
    Parse the output from a language model and determine the action and target.
    """
    output = output.replace('action', '').replace(
        'target', '').split('Note')[0].split('Explanation')[0]
    action_str, target_str = split_string(output)
    if action_str == 'kill' and 'kill' not in [x[0].name for x in possible_actions]:
        return FAILED_KILL, target_str
    action_str = closest_string(
        action_str, [x[0].name for x in possible_actions])
    action = next((x[0] for x in possible_actions if x[0].name ==
                  action_str), possible_actions[0][0])
    if action.name == 'talk':
        return action, target_str
    target_str = closest_string(
        target_str, [x[1] for x in possible_actions if x[0] == action])
    target = next((x[1] for x in possible_actions if x[0] ==
                  action and x[1] == target_str), possible_actions[0][1])

    return action, target

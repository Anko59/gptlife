from enum import Enum

PLAYERS_PER_GAME = 12

KILLERS_PER_GAME = 5


class Role(Enum):
    KILLER = "killer"
    INNOCENT = "innocent"
    POLICEMAN = "policeman"
    ARCHITECT = "architect"
    DEVIL = "devil"


ROLE_COLORS = {
    Role.KILLER: "31",  # red
    Role.INNOCENT: "34",  # blue
    Role.POLICEMAN: "32",  # green
    Role.ARCHITECT: "33",  # yellow
    Role.DEVIL: "30"  # black
}


class Items:
    BROOM = "Broom"
    TV_REMOTE = "TV remote"


class RoomName:
    KITCHEN = "Kitchen"
    CELLAR = "Cellar"
    BATHROOM = "Bathroom"
    BEDROOM = "Bedroom"
    LIVING_ROOM = "Living Room"
    DINING_ROOM = "Dining Room"
    GARDEN = "Garden"
    LIBRARY = "Library"
    THRONE_ROOM = "Throne Room"
    PLAYROOM = "Playroom"
    ART_ROOM = "Art Room"
    OBSERVATORY = "Observatory"
    CHAPEL = "Chapel"

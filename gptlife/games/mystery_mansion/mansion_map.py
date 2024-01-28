from gptlife.games.map import Map, Room
import gptlife.games.mystery_mansion.mysterious_tasks as task
from gptlife.games.mystery_mansion.constants import RoomName, Items


map_description = """The mansion has a central Throne Room connected to the Living Room, Playroom, 
and Chapel. The Living Room connects to the Bathroom, Bedroom, Garden, and Library. The Playroom 
leads to the Observatory and Art Room. The Bathroom and Bedroom are interconnected and both 
lead back to the Living Room, with the Bedroom also connected to the Dining Room and Cellar. 
The Garden is accessible from the Living Room and Library and leads to the Observatory. 
The Cellar is connected to the Bedroom, Kitchen, and Art Room.
The Art Room can also be reached from the Playroom. The Observatory has passages to the Playroom, 
Garden, and Throne Room. The Dining Room is connected to the Kitchen, Bedroom, Library, and Living 
Room. The Kitchen leads to the Dining Room and Cellar. The Library is connected to the 
Dining Room, Garden, Chapel, and Living Room. Finally, the Chapel is connected to the 
Library and Throne Room.
"""


def generate_map() -> Map:
    map = Map()
    rooms = [RoomName.THRONE_ROOM, RoomName.LIVING_ROOM, RoomName.PLAYROOM, RoomName.BATHROOM, RoomName.BEDROOM, RoomName.GARDEN,
             RoomName.CELLAR, RoomName.ART_ROOM, RoomName.OBSERVATORY, RoomName.DINING_ROOM, RoomName.KITCHEN, RoomName.LIBRARY, RoomName.CHAPEL]
    tasks = [task.RULING, task.WATCHING_TV, task.PLAYING, task.SHOWERING, task.SLEEPING, task.GARDENING,
             task.CLEANING, task.PAINTING, task.STARGAZING, task.EATING, task.COOKING, task.READING, task.PRAYING]

    for room, t in zip(rooms, tasks):
        map.add_room(room, t)

    connections = {
        RoomName.THRONE_ROOM: [RoomName.LIVING_ROOM, RoomName.PLAYROOM, RoomName.CHAPEL],
        RoomName.LIVING_ROOM: [RoomName.THRONE_ROOM, RoomName.BATHROOM, RoomName.BEDROOM, RoomName.GARDEN, RoomName.LIBRARY],
        RoomName.PLAYROOM: [RoomName.THRONE_ROOM, RoomName.OBSERVATORY, RoomName.ART_ROOM],
        RoomName.BATHROOM: [RoomName.LIVING_ROOM, RoomName.BEDROOM],
        RoomName.BEDROOM: [RoomName.BATHROOM, RoomName.LIVING_ROOM, RoomName.DINING_ROOM, RoomName.CELLAR],
        RoomName.GARDEN: [RoomName.LIVING_ROOM, RoomName.LIBRARY, RoomName.OBSERVATORY],
        RoomName.CELLAR: [RoomName.BEDROOM, RoomName.KITCHEN, RoomName.ART_ROOM],
        RoomName.ART_ROOM: [RoomName.CELLAR, RoomName.PLAYROOM],
        RoomName.OBSERVATORY: [RoomName.PLAYROOM, RoomName.GARDEN, RoomName.THRONE_ROOM],
        RoomName.DINING_ROOM: [RoomName.KITCHEN, RoomName.BEDROOM, RoomName.LIBRARY, RoomName.LIVING_ROOM],
        RoomName.KITCHEN: [RoomName.DINING_ROOM, RoomName.CELLAR],
        RoomName.LIBRARY: [RoomName.DINING_ROOM, RoomName.GARDEN, RoomName.CHAPEL, RoomName.LIVING_ROOM],
        RoomName.CHAPEL: [RoomName.LIBRARY, RoomName.THRONE_ROOM]
    }

    for room, connected_rooms in connections.items():
        map.connect_rooms(room, connected_rooms)

    map.rooms[RoomName.KITCHEN].items.append(Items.BROOM)
    map.rooms[RoomName.LIVING_ROOM].items.append(Items.TV_REMOTE)

    map.init_map_graph()

    return map

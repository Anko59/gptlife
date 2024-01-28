
from typing import List, Union

import random
from typing import List, Union
from faker import Faker

fake = Faker()


def generate_blood_type() -> str:
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    return random.choice(blood_types)


def generate_zodiac_sign() -> str:
    zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    return random.choice(zodiac_signs)


def generate_personality_type() -> str:
    personality_types = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP',
                         'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']
    return random.choice(personality_types)


def generate_allergies() -> List[str]:
    allergies = ['Pollen', 'Dust mites', 'Mold', 'Pet dander',
                 'Food', 'Insect stings', 'Medications', 'Latex']
    return random.sample(allergies, k=random.randint(1, 3))


def generate_health_conditions() -> List[str]:
    health_conditions = ['Diabetes', 'Asthma', 'Heart Disease',
                         'Cancer', 'Stroke', 'Alzheimer', 'Kidney Disease', 'Liver Disease']
    return random.sample(health_conditions, k=random.randint(1, 2))


def generate_fitness_level() -> str:
    fitness_levels = ['Poor', 'Below average', 'Average', 'Good', 'Excellent']
    return random.choice(fitness_levels)


def generate_age() -> int:
    return random.randint(18, 80)


def generate_num_of_children() -> int:
    return random.randint(0, 5)


def generate_nationality() -> str:
    return fake.country()


def generate_gender() -> str:
    return random.choice(['Male', 'Female'])


def generate_pet() -> str:
    return random.choice(['Dog', 'Cat', 'Bird', 'Fish', 'None'])


def generate_occupation() -> str:
    return fake.job()


def generate_income() -> Union[int, float]:
    return round(random.uniform(10000, 100000), 2)


def generate_marital_status() -> str:
    return random.choice(['Single', 'Married', 'Divorced', 'Widowed'])


def generate_education_level() -> str:
    return random.choice(['No High School', 'High School', 'Bachelor', 'Master', 'PhD'])


def generate_favorite_color() -> str:
    return fake.color_name()


def generate_favorite_food() -> str:
    food_list = ['Pizza', 'Burger', 'Pasta', 'Sushi', 'Steak',
                 'Salad', 'Ice Cream', 'Chocolate', 'Fries', 'Tacos']
    return random.choice(food_list)


def get_favorite_music_genre() -> str:
    genres = ["Pop", "Rock", "Country", "Rap", "Classical",
              "Jazz", "Blues", "Reggae", "Folk", "Electronic"]
    return random.choice(genres)


def get_hobbies() -> List[str]:
    hobbies = ["Reading", "Traveling", "Fishing", "Gardening", "Cooking",
               "Dancing", "Hiking", "Painting", "Photography", "Writing"]
    return random.sample(hobbies, k=random.randint(1, len(hobbies)))


def get_political_view() -> str:
    views = ["Conservative", "Liberal", "Libertarian",
             "Green", "Socialist", "Independent", "Moderate"]
    return random.choice(views)


def get_religious_belief() -> str:
    beliefs = ["Christianity", "Islam", "Secular/Agnostic/Atheist", "Hinduism",
               "Buddhism", "Sikhism", "Judaism", "Baháʼí", "Confucianism", "Jainism"]
    return random.choice(beliefs)


def get_height() -> Union[int, float]:
    return round(random.uniform(150.0, 200.0), 2)


def get_weight() -> Union[int, float]:
    return round(random.uniform(50.0, 100.0), 2)


def get_eye_color() -> str:
    colors = ["Blue", "Green", "Brown", "Hazel",
              "Grey", "Amber", "Red", "Violet"]
    return random.choice(colors)


def get_hair_color() -> str:
    colors = ["Black", "Brown", "Blond", "Auburn",
              "Chestnut", "Red", "Gray", "White"]
    return random.choice(colors)


given_names = []


def generate_random_name(gender: str) -> str:
    """
    Generate a random name of a historical figure or a soccer player.

    :param gender: 'male' or 'female'
    """

    first_names = {
        'Male': ["Alexander", "Julius", "Napoleon", "Socrates", "Galileo", "Marco",
                 "Christopher", "Wolfgang", "Ludwig", "Albert", "Martin", "Mahatma",
                 "Nelson", "Winston", "Abraham", "George", "Thomas", "Benjamin",
                 "Theodore", "Franklin", "William", "Charles", "Henry", "Lionel",
                 "Cristiano", "Diego", "Pele", "Zinedine", "David", "Ronaldinho",
                 "Roberto", "Franz", "Johan"],
        'Female': ["Cleopatra", "Joan", "Leonarda", "Marie", "Rosa", "Elizabeth",
                   "Victoria", "Margaret", "Florence", "Harriet", "Amelia", "Helen",
                   "Anne", "Emily", "Louisa", "Jane", "Mary", "Susan", "Diana",
                   "Eleanor", "Ruth", "Ellen", "Marilyn", "Rosa", "Audrey", "Mae",
                   "Simone", "Oprah", "Indira", "Theresa", "Angela", "Hillary",
                   "Michelle", "Melinda"]
    }

    last_names = ["the Great", "Caesar", "Bonaparte", "of Egypt", "of Arc",
                  "da Vinci", "of Athens", "Galilei", "Polo", "Columbus",
                  "Mozart", "Beethoven", "Einstein", "Curie", "Parks",
                  "Luther King Jr.", "Gandhi", "Mandela", "Churchill", "Lincoln",
                  "Washington", "Jefferson", "Franklin", "Roosevelt", "D. Roosevelt",
                  "I", "II", "the Conqueror", "I", "VIII",
                  "Messi", "Ronaldo", "Maradona", "de Lima", "Zidane",
                  "Beckham", "Gaucho", "Carlos", "Beckenbauer", "Cruyff"]

    name = None

    while name is None or name in given_names:
        name = f"{random.choice(first_names[gender])} {random.choice(last_names)}"
    given_names.append(name)

    return name


class Personality:
    def __init__(
        self,
        name: str,
        age: int,
        num_of_children: int,
        nationality: str,
        gender: str,
        pet: str,
        occupation: str,
        income: Union[int, float],
        marital_status: str,
        education_level: str,
        favorite_color: str,
        favorite_food: str,
        favorite_music_genre: str,
        hobbies: List[str],
        political_view: str,
        religious_belief: str,
        height: Union[int, float],
        weight: Union[int, float],
        eye_color: str,
        hair_color: str,
        blood_type: str,
        zodiac_sign: str,
        personality_type: str,
        allergies: List[str],
        health_conditions: List[str],
        fitness_level: str
    ):
        self.name = name
        self.age = age
        self.num_of_children = num_of_children
        self.nationality = nationality
        self.gender = gender
        self.pet = pet
        self.occupation = occupation
        self.income = income
        self.marital_status = marital_status
        self.education_level = education_level
        self.favorite_color = favorite_color
        self.favorite_food = favorite_food
        self.favorite_music_genre = favorite_music_genre
        self.hobbies = hobbies
        self.political_view = political_view
        self.religious_belief = religious_belief
        self.height = height
        self.weight = weight
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.blood_type = blood_type
        self.zodiac_sign = zodiac_sign
        self.personality_type = personality_type
        self.allergies = allergies
        self.health_conditions = health_conditions
        self.fitness_level = fitness_level

    def get_prompt(self):
        attributes = [
            f"You are a {self.age} year old {self.gender} from {self.nationality}.",
            f"You are {self.marital_status} with {self.num_of_children} children.",
            f"You work as a {self.occupation} and earn {self.income}.",
            f"You have a pet {self.pet}.",
            f"Your favorite color is {self.favorite_color} and you enjoy {self.favorite_food}.",
            f"You listen to {self.favorite_music_genre} and enjoy these hobbies: {', '.join(self.hobbies)}.",
            f"You are of {self.religious_belief} religion and your political view is {self.political_view}.",
            f"You are {self.height} tall and weigh {self.weight}.",
            f"You have {self.eye_color} eyes and {self.hair_color} hair.",
            f"Your blood type is {self.blood_type} and your Zodiac sign is {self.zodiac_sign}.",
            f"You are a {self.personality_type}.",
            f"You are allergic to {', '.join(self.allergies)} and have these health conditions: {', '.join(self.health_conditions)}.",
            f"Your fitness level is {self.fitness_level}."
        ]

        random.shuffle(attributes)
        prompt = f"Your name is {self.name}."
        prompt += " ".join(attributes[:random.randint(2, len(attributes))])

        return prompt

    @classmethod
    def generate_random_personality(
        cls,
        **kwargs
    ):
        args = {
            "age": generate_age(),
            "num_of_children": generate_num_of_children(),
            "nationality": generate_nationality(),
            "gender": generate_gender(),
            "pet": generate_pet(),
            "occupation": generate_occupation(),
            "income": generate_income(),
            "marital_status": generate_marital_status(),
            "education_level": generate_education_level(),
            "favorite_color": generate_favorite_color(),
            "favorite_food": generate_favorite_food(),
            "favorite_music_genre": get_favorite_music_genre(),
            "hobbies": get_hobbies(),
            "political_view": get_political_view(),
            "religious_belief": get_religious_belief(),
            "height": get_height(),
            "weight": get_height(),
            "eye_color": get_eye_color(),
            "hair_color": get_hair_color(),
            "blood_type": generate_blood_type(),
            "zodiac_sign": generate_zodiac_sign(),
            "personality_type": generate_personality_type(),
            "allergies": generate_allergies(),
            "health_conditions": generate_health_conditions(),
            "fitness_level": generate_fitness_level()
        }
        args["name"] = generate_random_name(args["gender"])
        args.update(kwargs)
        return cls(**args)


def generate_devil_job() -> str:
    jobs = ["Fire Starter", "Soul Collector", "Tempter",
            "Underworld Gatekeeper", "Hell's Accountant"]
    return random.choice(jobs)


def generate_devil_pet() -> str:
    pets = ["Hellhound", "Demon Cat", "Infernal Bat",
            "Cursed Snake", "Possessed Raven"]
    return random.choice(pets)


def generate_devil_power() -> str:
    powers = ["Fire Manipulation", "Invisibility",
              "Teleportation", "Mind Control", "Immortality"]
    return random.choice(powers)


def generate_devil_weapon() -> str:
    weapons = ["Hellfire Trident", "Demon Sword",
               "Cursed Scythe", "Infernal Whip", "Soul Eater Dagger"]
    return random.choice(weapons)


def generate_devil_language() -> str:
    languages = ["Infernal", "Abyssal",
                 "Demonic", "Undercommon", "Shadowtongue"]
    return random.choice(languages)


def generate_devil_talent() -> str:
    talents = ["Deception", "Manipulation", "Shape-shifting", "Invisibility", "Telekinesis",
               "Mind control", "Fire control", "Flight", "Immortality", "Super strength"]
    return random.choice(talents)


def generate_devil_skill() -> str:
    skills = ["Deception", "Manipulation", "Stealth", "Intelligence", "Charm",
              "Cunning", "Power", "Invisibility", "Teleportation", "Immortality"]
    return skills


def generate_devil_appearance() -> str:
    appearances = ["Horns", "Wings", "Tail", "Hooves", "Fangs",
                   "Claws", "Red skin", "Black eyes", "Black hair", "Red eyes"]
    return random.choice(appearances)


def generate_devil_origin() -> str:
    origins = ["Hell", "Underworld", "Abyss", "Pandemonium", "Netherworld"]
    return random.choice(origins)


def generate_devil_motto() -> str:
    mottos = [
        "One man's sin is another man's freedom.",
        "Rules are made to be broken.",
        "Why be a saint when you can reign in hell?",
        "Sometimes, the darkest path leads to the brightest future.",
        "Chaos is not a pit, it's a ladder.",
        "Power is never given, it's taken.",
        "When you stare into the abyss, the abyss stares back.",
        "The only thing necessary for the triumph of evil is for good men to do nothing.",
        "Evil is just a matter of perspective.",
        "In the end, we all become the monsters we fear the most."
    ]
    return random.choice(mottos)


class DevilPersonality(Personality):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.personality_type = "Evil"
        self.favorite_color = "Black"
        self.favorite_music_genre = "Heavy Metal"
        self.hobbies.append("Torturing souls")

    @classmethod
    def generate_random_personality(cls):
        personality = super().generate_random_personality()
        personality.personality_type = "Evil"
        personality.favorite_color = "Black"
        personality.favorite_music_genre = "Heavy Metal"
        personality.hobbies.append("Torturing souls")
        personality.job = generate_devil_job()
        personality.devil_pet = generate_devil_pet()
        personality.devil_power = generate_devil_power()
        personality.devil_weapon = generate_devil_weapon()
        personality.devil_language = generate_devil_language()
        personality.devil_talent = generate_devil_talent()
        personality.devil_skill = generate_devil_skill()
        personality.devil_appearance = generate_devil_appearance()
        personality.devil_origin = generate_devil_origin()
        personality.devil_motto = generate_devil_motto()
        return personality

    def get_prompt(self):
        attributes = [
            f"You are a {self.age} year old {self.gender} from {self.nationality}.",
            f"Your devil job is {self.job}.",
            f"Your devil pet is {self.devil_pet}.",
            f"Your devil power is {self.devil_power}.",
            f"Your devil weapon is {self.devil_weapon}.",
            f"Your devil language is {self.devil_language}.",
            f"Your devil talent is {self.devil_talent}.",
            f"Your devil skill is {', '.join(self.devil_skill)}.",
            f"Your devil appearance includes {', '.join(self.devil_appearance)}.",
            f"Your devil origin is {self.devil_origin}.",
            f"Your devil motto is {self.devil_motto}."
        ]

        random.shuffle(attributes)
        prompt = f"Your name is {self.name}."
        prompt += " ".join(attributes[:random.randint(2, len(attributes))])

        return prompt

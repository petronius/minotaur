"""
left/right
up/down

floor

day



color

pitch
mood
name


Warp items:

Stairs up/down - change floor

Calendar (the days pass swiftly) - "day" forward
A mirror (do I already look so old?) - "day" backward



"""

MSGS=[
    {# x
        1: "You will soon see how the cellar branches out",
        -1: "I knew you would like that drain.",
    },
    {# y
        1: "Now we shall return to the first intersection",
        -1:  "Now we shall come out into another courtyard",
    },
    {#z/height
        1: "Above, the intricate sun.",
        -1: "Below, Asterion.",
    },
    {#a/time
        1: "... the nights and days are long.",
        -1: "One afternoon I did step into the street.",
    },
    {# color
        1: "The morning sun reverberated from the bronze sword.",
        -1: "There was no longer even a vestige of blood.",
    },
    {# pitch
        1: "I run through the stone galleries until I fall dizzy to the floor.",
        -1: "There are roofs from which I let myself fall until I am bloody.",
    },
    {# mood
        1: "Bothersome and trivial details have no place in my spirit ...",
        -1: "... which is prepared for all that is vast and grand",
    },
    {# name
        1: "And the queen gave birth to a child who was called Asterion.",
        -1: "The Minotaur scarcely defended himself.",
    },
]

# color = [
#     "red",
#     "blue",
#     "green",
#     "yellow",
#     "white",
#     "silver",
#     "gold",
#     "black",
# ]

color = [
    ("or",
        (255, 210, 0)),
    ("argent",
        (192, 192, 192)),
    ("azure",
        (0, 0, 139)),
    ("gules",
        (139, 0, 0)),
    ("purpure",
        (75, 0, 130)),
    ("sable",
        (30, 30, 10)),
    ("vert",
        (0, 139, 0)),
]

def get_msg(dim, delta):
    return MSGS[dim].get(delta)

def get_color(idx):
    return color[idx][1]

mood = [

]

names = [
    "asterion",
    "minotaur",
    "son of minos",
    "theseus",
    "did you see, ariadne?",
    "scarcely defended himself",
]
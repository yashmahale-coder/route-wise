# Illustrative demo network inspired by Navi Mumbai. Distances are simulated (km).
LOCATIONS = {
    "uran": "Uran",
    "panvel": "Panvel",
    "kharghar": "Kharghar",
    "belapur": "CBD Belapur",
    "nerul": "Nerul",
    "vashi": "Vashi",
    "koparkhairane": "Kopar Khairane",
    "airoli": "Airoli"
}

# Abstract map coordinates used only to draw the graph and estimate A* heuristic.
COORDS = {
    "uran": (80, 330),
    "panvel": (270, 300),
    "kharghar": (390, 250),
    "belapur": (500, 260),
    "nerul": (610, 210),
    "vashi": (740, 150),
    "koparkhairane": (850, 190),
    "airoli": (940, 100)
}

# Every edge cost is at least the straight-line distance in this abstract coordinate
# space scaled to km, keeping the Euclidean A* heuristic admissible.
GRAPH = {
    "uran": {"panvel": 22},
    "panvel": {"uran": 22, "kharghar": 12, "belapur": 19},
    "kharghar": {"panvel": 12, "belapur": 9, "nerul": 17},
    "belapur": {"panvel": 19, "kharghar": 9, "nerul": 8},
    "nerul": {"kharghar": 17, "belapur": 8, "vashi": 11},
    "vashi": {"nerul": 11, "koparkhairane": 7},
    "koparkhairane": {"vashi": 7, "airoli": 10},
    "airoli": {"koparkhairane": 10}
}

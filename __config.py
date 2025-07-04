# All image files should be the same size as the width and height specified below.
# If not, an error will be raised
WIDTH = 10
HEIGHT = 10

# The JSON file name/path to save the map data to
MAP_JSON_FILE = "map.json"

# Images denoting which cells have certain environmental conditions
# The order of which these environmental conditions are inputted should not be changed.
ENVIRONMENT_FLAG_IMAGES = [
    "images/nebula.png", # Nebula
    "images/asteroids.png", # Asteroids
    "images/spacedust.png", # Space dust
    "images/ice.png", # Ice fields
]

# Images denoting which faction cells belong to
# The keys of the FACTION_IMAGES should be identical to the enum values of the Faction enum in the Java source code.
FACTION_IMAGES = {

}

# Images denoting landmarks that appear in certain places
# The keys of the LANDMARK_IMAGES should be identical to the enum values of the LandmarkType enum in the Java source code.
LANDMARK_IMAGES = {
    "PLANET": "images/planets.png",
}
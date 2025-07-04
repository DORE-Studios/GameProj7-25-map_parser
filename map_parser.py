from PIL import Image
import json
import os
from __config import ENVIRONMENT_FLAG_IMAGES, FACTION_IMAGES, LANDMARK_IMAGES, WIDTH, HEIGHT, MAP_JSON_FILE

# Change to current working directory
script_path = os.path.abspath(__file__)
script_directory = os.path.dirname(script_path)
os.chdir(script_directory)

def parse_image(image_path: str) -> set:
    """
    Loads a black and white image from a file path. Returns the coordinate locations of black pixels as a set of (x, y) tuples.
    
    If the image fails to load or is of an incorrect size (i.e. its width and height are not the same as the WIDTH and HEIGHT config)
    then the function will return an empty set.
    """

    image: Image.Image = None
    try: 
        image = Image.open(image_path).convert("L")
        if image.width != WIDTH or image.height != HEIGHT:
            print(f"Error parsing image '{image_path}': Incorrect size")
            return set()
    except IOError as e:
        print(f"Error parsing image '{image_path}': {e}")
        return set()
    
    coordinates: set = set()
    
    for x in range(image.width):
        for y in range(image.height):
            if image.getpixel((x, y)) == 0:
                coordinates.add((x, y))

    return coordinates


def parse_images_to_json() -> None:
    """
    Parses the images from the config file and creates a json file.
    You can modify the name/path of the json file in the config file.
    """

    coordinate_features: list = []
    for y in range(HEIGHT):
        l: list = []
        for x in range(WIDTH):
            l.append({"environmentFlags": 0, "faction": None, "landmark": None})
        coordinate_features.append(l)

    # Add environment flags
    for bit, image_path in enumerate(ENVIRONMENT_FLAG_IMAGES):
        for coordinate in parse_image(image_path):
            coordinate_features[coordinate[1]][coordinate[0]]["environmentFlags"] += (2 ** bit)

    # Add factions
    for faction, image_path in FACTION_IMAGES.items():
        for coordinate in parse_image(image_path):
            coordinate_features[coordinate[1]][coordinate[0]]["faction"] = faction

    # Add landmarks
    for landmark_type, image_path in LANDMARK_IMAGES.items():
        for coordinate in parse_image(image_path):
            coordinate_features[coordinate[1]][coordinate[0]]["landmark"] = {"type": landmark_type, "name": "", "description": ""}

    # Write to json file    
    with open('map.json', 'w', encoding='utf-8') as f:
        json.dump(coordinate_features, f, ensure_ascii=False, indent=4)

    


    
if __name__ == "__main__":
    parse_images_to_json()
    print(f"Parsed images to the map json file: {MAP_JSON_FILE}")

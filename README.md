This is a small utility for the 2025 July Game Jam project that helps generate a JSON file that stores game map data.
This turns multiple black and white images into a JSON file that the game can read and parse as a map.

# Steps for Use

## 1. Install the pillow library
`pip install pillow`

## 2. Modify __config.py
All of the images can be saved into the images folder (the ones in the repository are there for testing) and 
To change the images, change the paths in `__config.py`. **Ensure that you read all the comments in `__config.py`!**

## 3. Run the file
`python map_parser.py`
This should generate the JSON file that can be parsed by the game. Yay!

*Written by Euan Monteclaro in the span of 30 minutes*
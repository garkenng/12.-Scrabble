"""
Creating a Scrabble like game, program will output the points based on the words used in the word
Two lists below, one with letters and the other with the corresponding points
"""

# Two lists containing letters and its value
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Combining the lists together to match A with 1 for example
letter_to_points = {key: value for key, value in zip(letters, points)}

# Add an empty string with value of 0 points to the newly created dictionary
letter_to_points[" "] = 0

# Creates a function that calcualtes the points of a given word
def score_word(word):
    point_total = 0
    # Loops through the word, pulls the value from the key, 'i' and adds it to the point total
    for i in word:
        point_total += letter_to_points.get(i, 0)
        
    return point_total

# Test the function by creating a varaible brownie points and calculating its value
brownie_points = score_word("BROWNIE")
# Expected result is 15
# print(brownie_points)

# Creates map of words that each fictional player has created
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Creating an empty dictionary to store the scores of words from the players
player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word)
    player_to_points[player] = player_points

# print the result of the game
print(player_to_points)
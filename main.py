import random
from words import words
from hangman_visual import lives_visual_dict
import string


print("H A N G M A N")
def get_valid_word(words):
    word = random.choice(words)  # randomly choose something from the list
    

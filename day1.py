# assignment:
# write a function that traverses a list and returns a random name from said list
# bonus if you write in nested loops for transversal, concatenation of results, etc.

import random # need for choosing a random player

Bengles_list = ['Burrow', 'Chase', 'Higgins', 'Mixon', 'Boyd'] # player list

def select_bengles_player(): # selects a random player from the list and saves it
    selected_player = random.choice(Bengles_list)
    print(selected_player)
    return selected_player

select_bengles_player()
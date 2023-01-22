import random

def item_randomizer():
    item = []

    with open("item_randomizer/item_list.txt") as file:
        for line in file: 
                item.append(line.rstrip())

    random_number = random.randint(0, 21)

    chosen_items = random.sample(item, random_number) 

    return chosen_items

"""Restaurant rating lister."""

import random

def read_ratings():
    """Reads text file and creates dictionary in the format of restuarant:rating"""
    ratings = {}

    file = open('./scores.txt', 'r')

    for line in file:
        line = line.strip('\n')
        key, value = line.split(':')
        ratings[key] = int(value)

    file.close()
    return ratings
    

def add_rating(d):
    """Prompts the user for a new restaurant/rating and adds it to the dictionary"""
    
    new_rest = input('Enter a restaurant name: ')
    while True:
        new_rating = int(input('Enter rating of ' + new_rest + ': '))
        if new_rating >= 1 and new_rating <= 5:
            break
        else:
            print('Please enter a rating between 1 and 5')
            continue

    d[new_rest] = int(new_rating)


def update_rating(d):
    """Allows user to update a random rating from a dictionary"""
    choice = random.choice(list(d.keys()))
    print('\nThe randomly chosen restaurant is', choice)
    new_rating = int(input('Enter a new rating for ' + choice + ': '))
    d[choice] = new_rating


def print_ratings(d):
    """Prints the restaurants/ratings in alphabetical order"""

    for restaurant, rating in sorted(d.items()):
        print(f'{restaurant} is rated at {rating}.')


# Read text file and create dictionary of restuarant: rating
ratings = read_ratings()

# Prompt the user for action choice
while True:
    print('\nWhat action would you like to perform?')
    print('\'add\' a new restaurant and rating, \'see\' all ratings, \'update\' a random rating, or \'quit\'.')
    choice = input('Your choice: ').lower()

    if choice == 'add':
        add_rating(ratings)
        continue
    elif choice == 'see':
        print_ratings(ratings)
        continue
    elif choice == 'update':
        update_rating(ratings)
        continue
    else:
        print('Thanks for your time! Have a nice day :)')
        break


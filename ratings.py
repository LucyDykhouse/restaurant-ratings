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
    
    new_rest = input('\nEnter a restaurant name: ')
    while True:
        new_rating = int(input('Enter rating of ' + new_rest + ': '))
        if new_rating >= 1 and new_rating <= 5:
            break
        else:
            print('Please enter a rating between 1 and 5')
            continue

    d[new_rest] = int(new_rating)


def update_random_rating(d):
    """Allows user to update a random rating from a dictionary"""

    # Pick a random restaurant key
    choice = random.choice(list(d.keys()))

    # Allow users to change rating
    print('\nThe randomly chosen restaurant is', choice)
    print('It currently has a rating of', d[choice])
    new_rating = int(input('What is your rating for ' + choice + ': '))

    # Update rating in dictionary
    d[choice] = new_rating


def update_chosen_rating(d):
    """Allows user to choose a restaurant then update its rating"""

    # Show the user the current restaurants
    print('\nHere are the current restaurants available for update:')
    print_ratings(d)

    # Prompt the user to choose a restaurant
    while True:
        choice = input('\nEnter a restaurant as it\'s written above:\n')

        # Verify choice and get new rating
        if d.get(choice) != None:
            print('The current rating for', choice, 'is', d[choice])
            new_rating = int(input('Enter your rating: '))
            d[choice] = new_rating
            break
        else:
            print('Sorry, I didn\'t get that. Please try again')
            continue


def print_ratings(d):
    """Prints the restaurants/ratings in alphabetical order"""

    for restaurant, rating in sorted(d.items()):
        print(f'{restaurant} is rated at {rating}.')


def display_choices():
    """Prints the user\'s choices to console and allows user to input choice"""

    print('\nWhat action would you like to perform?')

    # User choices
    print('\t1: See all restaurants and their ratings')
    print('\t2: Add a new restaurant and rating')
    print('\t3: Update the rating of a random restaurant')
    print('\t4: Update the rating of a chosen restaurant')
    print('\t5: Quit')

    # Prompt user for a choice
    choice = input('Your choice: ').strip()

    return choice


# Read text file and create dictionary of restuarant: rating
ratings = read_ratings()

# Prompt the user for action choice
while True:
    choice = display_choices()    

    if choice == '1':
        print('\n')
        print_ratings(ratings)
    elif choice == '2':
        add_rating(ratings)
    elif choice == '3':
        update_random_rating(ratings)
    elif choice == '4':
        update_chosen_rating(ratings)
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('I didn\'t get that. Please try again!')


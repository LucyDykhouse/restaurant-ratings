"""Restaurant rating lister."""

# Create dictionary to store restaurants/ratings
ratings = {}

# Open the text file
file = open('./scores.txt', 'r')

# Read in the text file contents and add to dictionary
for line in file:
    line = line.strip('\n')
    key, value = line.split(':')
    ratings[key] = int(value)

# Prompt the user for a new restaurant/rating
new_rest = input('Enter a restaurant name: ')
new_rating = input('Enter rating of ' + new_rest + ': ')

# Insert new restaurant/rating into dictionary
ratings[new_rest] = new_rating

# Print the ratings in alphabetical order
for restaurant, rating in sorted(ratings.items()):
    print(f'{restaurant} is rated at {rating}.')

# Close the file
file.close()
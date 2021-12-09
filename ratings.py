"""Restaurant rating lister."""

ratings = {}

file = open('./scores.txt', 'r')

for line in file:
    line = line.strip('\n')
    (key, value) = line.split(':')
    ratings[key] = value

sorted_ratings = sorted(ratings.items())

for tuple in sorted_ratings:
    print(f'{tuple[0]} is rated at {tuple[1]}.')


file.close()
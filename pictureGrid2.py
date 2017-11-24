### Character Picture Grid ###

grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]

#read up on 'zip'
transposed_grid = zip(*grid)
#this iterates over all 'lines' in the transposed_grid
#and uses ''.join on these lines, basically concatenating
#the characters
joined_characters = [''.join(line) for line in transposed_grid]
#now join the lines, putting a newline between each line
joined_lines = '\n'.join(joined_characters)
#print the thing
print(joined_lines)

# streamlined: print('\n'.join(''.join(line) for line in zip(*grid)))

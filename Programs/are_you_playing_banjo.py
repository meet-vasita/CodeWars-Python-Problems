#Are You Playing Banjo?

# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

# Names given are always valid strings.


def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        print(f'{name} is playing banjo')
    else:
        print(f'{name} is not playing a banjo')

are_you_playing_banjo('Meet')
are_you_playing_banjo('Rikkie')
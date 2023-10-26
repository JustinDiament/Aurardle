
import fileinput
import sys
import global_vars as g

# Returns the player at the argument index in the set order
def todays_player(index):
# Open the list of players, in order by who will be the correct answer each day
    with open('./static/player_files/player_of_the_day_2023_24.txt', 'r') as file:
        # Put them in a list
        players_order = file.readlines()

    # Remove white space and newlines
    players_order = [line.strip() for line in players_order]

    # Return the player of the day
    return players_order[index]

# Overwrites the daily player in all necessary places
# Run automatically daily by a cron job
def change_player():
    # Get old player and day index
    old_day_index = str(g.day_index)
    old_player = todays_player(g.day_index)
    
    # Increase index
    g.day_index= g.day_index + 1

    # Get new player and day index
    new_player = todays_player(g.day_index)
    new_day_index = str(g.day_index)

    # Overwrite js constsnts
    for line in fileinput.input("./static/global_vars.js", inplace=1):
        if "game_number" in line:
            line = line.replace(old_day_index, new_day_index)
        elif "correct_player" in line:
            line = line.replace(old_player, new_player)
        sys.stdout.write(line)

    # Overwrite python constants
    for line in fileinput.input("./global_vars.py", inplace=1):
        if "day_index" in line:
            line = line.replace(old_day_index, new_day_index)
        elif "correct_player" in line:
            line = line.replace(old_player, new_player)
        sys.stdout.write(line)

# Directs a command line call to this python file to run the player overwriting function above
if __name__ == "__main__":
    change_player()
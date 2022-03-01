# Creation date: February 27, 2022
# Author: Daniel Soto Corochué

from urllib.request import urlopen
import json

url = "https://mach-eight.uc.r.appspot.com/"                                        # URL where the json is
response = urlopen(url)                                                             # Open the url and save it in response variable

# Save all players in a list of dicts sorted by height desc
players = sorted(json.loads(response.read()) ['values'], key=lambda i:i['h_in'], reverse=True)
max_number = int(players[0]['h_in']) + int(players[1]['h_in'])                     # Assign to max_number the sum of the two tallest players
min_number = int(players[-1]['h_in']) + int(players[-2]['h_in'])                   # Assign to min_number the sum of the two smaller players

# Ask to user for a number
number = int(input(f'Enter a number between {min_number} and {max_number}: '))
while (number > max_number) or (number < min_number):                               # Validate if the number is between min and max
    number = int(input(f'Wrong number. Enter a number between {min_number} and {max_number}: '))

# Save in list players1 all players who have a height mayor of the diff between the input number and the highest height
players1 = [one for one, find_player in enumerate(players) if int(find_player['h_in']) > number - int(players[0]['h_in'])]

for player in players1:
    player1 = f"{players[player]['first_name']} {players[player]['last_name']}"     # Save on player1 the first and last name of the player
    height_player_1 = int(players[player]['h_in'])                                  # Save the height of player1
    
    # Save in players2 all players who have the height of the input number minus the height of player1
    players2 = [one for one, find_player in enumerate(players) if int(find_player['h_in']) == (number - height_player_1)]
    for player2 in players2:
        if players[player] != players[player2]:
            # Print player1 with all players who their height add up the input number
            print(f"{player1}\n{players[player2]['first_name']} {players[player2]['last_name']}\n")
            try:
                del players1[players1.index(player2)]
                break
            except ValueError:
                pass

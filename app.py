from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import player_data.all_players_with_data_2023_24 as players
import global_vars as g

# All players currently avalible to be guessed and their attributes
# currently includes all NU basketball and hockey players from 2022-23
# plus, all NU baseball players from 2021-22.
# Also Tyson Walker because I said so
all_players = players.players

# Gets the player object with player properties for a player guessed by the user
def player_properties(player_typed):
    user_player = None

    for plyr in all_players:
        if plyr.name == player_typed:
            user_player = plyr
            break

    return user_player

# Gets the height of a guessed player and formats it into feet and inches
@app.route("/determine/height")
def determine_height():
    height_inches = player_properties(**request.args).height
    feet = height_inches//12
    inches = height_inches - (feet*12)

    height_overall = str(feet) + '′' + " " + str(inches) + "″"

    return jsonify(result=height_overall)

# Gets the sport of a guessed player
@app.route("/determine/sport")
def determine_sport():
    return jsonify(result=player_properties(**request.args).sport)

# Gets the position of a guessed player
@app.route("/determine/position")
def determine_postition():
    return jsonify(result=player_properties(**request.args).position)

# Gets the year of a guessed player
@app.route("/determine/year")
def determine_year():
    return jsonify(result=player_properties(**request.args).year)

# Gets the number of a guessed player
@app.route("/determine/number")
def determine_number():
    return jsonify(result=player_properties(**request.args).number)

# Determines green/yellow/red result for sport of player guessed
# Perfect match = green
# Same sport, opposite gender = yellow
# Wrong sport = red
@app.route("/check/sport")
def checksport():
    sport_guessed = player_properties(**request.args).sport
    sport_correct = player_properties(g.correct_player).sport
    if (sport_guessed==sport_correct):
        final = "correct"
    elif ((sport_guessed=="MBB" and sport_correct=="WBB") or (sport_guessed=="WBB" and sport_correct=="MBB")):
        final = "partially_correct"
    elif ((sport_guessed=="MHKY" and sport_correct=="WHKY") or (sport_guessed=="WHKY" and sport_correct=="MHKY")):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# Determines green/yellow/red result for position of player guessed
# Perfect match = green
# In baseball only, hitter/pitch match = yellow
# Wrong position otherwise = red
@app.route("/check/position")
def check_position():
    position_guessed = player_properties(**request.args).position
    position_correct = player_properties(g.correct_player).position

    if (position_guessed==position_correct):
        final = "correct"
    elif (position_guessed=="Catcher" and (position_correct=="UTL" or position_guessed=="OF" and position_correct=="INF")):
        final = "partially_correct"
    elif (position_guessed=="UTL" and (position_correct=="Catcher" or position_guessed=="OF" and position_correct=="INF")):
        final = "partially_correct"
    elif (position_guessed=="OF" and (position_correct=="Catcher" or position_guessed=="UTL" and position_correct=="INF")):
        final = "partially_correct"
    elif (position_guessed=="INF" and (position_correct=="Catcher" or position_guessed=="UTL" and position_correct=="OF")):
        final = "partially_correct"
    elif (position_guessed=="LHP" and position_correct=="RHP"):
        final = "partially_correct"
    elif (position_guessed=="RHP" and position_correct=="LHP"):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# Determines green/red result for sport of player guessed
@app.route("/check/year")
def check_year():
    return jsonify(result=player_properties(**request.args).year==player_properties(g.correct_player).year)

# Determines green/yellow/red result for height of player guessed
# Perfect match = green
# Within 2 inches = yellow
# More wrong than that = red
@app.route("/check/height")
def check_height():
    height_guessed = player_properties(**request.args).height
    height_correct = player_properties(g.correct_player).height
    if (height_guessed==height_correct):
        final = "correct"
    elif (abs(int(height_guessed) - int(height_correct)) <= 2):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# Determines green/yellow/red result for number of player guessed
# Perfect match = green
# Within 2 = yellow
# More wrong than that = red
@app.route("/check/number")
def check_number():
    number_guessed = player_properties(**request.args).number
    number_correct = player_properties(g.correct_player).number
    if (number_guessed==number_correct):
        final = "correct"
    elif (abs(int(number_guessed) - int(number_correct)) <= 2):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# Determines if the game has been won or not (correct player guessed)
@app.route("/check/winner")
def determine_winner():
    if (player_properties(g.correct_player).name == player_properties(**request.args).name):
        return jsonify(result="winner")
    else:
        return jsonify(result="not_yet")

# Renders the main screen of the game
@app.route("/", methods=["GET"])
def home():
    return render_template('main_page.html')
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import fileinput
import sys
import all_players_with_data_2023_24 as players

# overwritten daily
# daily correct player that must be guessed
correctplayer = "Matt Downing"

# increased by one daily automatically
# the index in the set player order of the current correct player
dayindex = 125

# all players currently avalible to be guessed and their attributes
# currently includes all NU basketball and hockey players from 2022-23
# plus, all NU baseball players from 2021-22
# also Tyson Walker because I said so
allplayers = players.players

# gets the player object with player properties for a player guessed by the user
def playerproperties(playertyped):
    userplayer = None

    for player1 in allplayers:
        if player1.name == playertyped:
            userplayer = player1
            break

    return userplayer

# gets the height of a guessed player and formats it into feet and inches
@app.route("/determine/height")
def determineheight():
    heightinches = playerproperties(**request.args).height
    feet = heightinches//12
    inches = heightinches - (feet*12)

    heightoverall = str(feet) + '′' + " " + str(inches) + "″"

    return jsonify(result=heightoverall)

# gets the sport of a guessed player
@app.route("/determine/sport")
def determinesport():
    return jsonify(result=playerproperties(**request.args).sport)

# gets the position of a guessed player
@app.route("/determine/position")
def determinepostition():
    return jsonify(result=playerproperties(**request.args).position)

# gets the year of a guessed player
@app.route("/determine/year")
def determineyear():
    return jsonify(result=playerproperties(**request.args).year)

# gets the number of a guessed player
@app.route("/determine/number")
def determinenumber():
    return jsonify(result=playerproperties(**request.args).number)

# determines green/yellow/red result for sport of player guessed
# perfect match = green
# same sport, opposite gender = yellow
# wrong sport = red
@app.route("/check/sport")
def checksport():
    sportguessed = playerproperties(**request.args).sport
    sportcorrect = playerproperties(correctplayer).sport
    if (sportguessed==sportcorrect):
        final = "correct"
    elif ((sportguessed=="MBB" and sportcorrect=="WBB") or (sportguessed=="WBB" and sportcorrect=="MBB")):
        final = "partially_correct"
    elif ((sportguessed=="MHKY" and sportcorrect=="WHKY") or (sportguessed=="WHKY" and sportcorrect=="MHKY")):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# determines green/yellow/red result for position of player guessed
# perfect match = green
# in baseball only, hitter/pitch match = yellow
# wrong position otherwise = red
@app.route("/check/position")
def checkposition():
    positionguessed = playerproperties(**request.args).position
    positioncorrect = playerproperties(correctplayer).position

    if (positionguessed==positioncorrect):
        final = "correct"
    elif (positionguessed=="Catcher" and (positioncorrect=="UTL" or positionguessed=="OF" and positioncorrect=="INF")):
        final = "partially_correct"
    elif (positionguessed=="UTL" and (positioncorrect=="Catcher" or positionguessed=="OF" and positioncorrect=="INF")):
        final = "partially_correct"
    elif (positionguessed=="OF" and (positioncorrect=="Catcher" or positionguessed=="UTL" and positioncorrect=="INF")):
        final = "partially_correct"
    elif (positionguessed=="INF" and (positioncorrect=="Catcher" or positionguessed=="UTL" and positioncorrect=="OF")):
        final = "partially_correct"
    elif (positionguessed=="LHP" and positioncorrect=="RHP"):
        final = "partially_correct"
    elif (positionguessed=="RHP" and positioncorrect=="LHP"):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# determines green/red result for sport of player guessed
@app.route("/check/year")
def checkyear():
    return jsonify(result=playerproperties(**request.args).year==playerproperties(correctplayer).year)

# determines green/yellow/red result for height of player guessed
# perfect match = green
# within 2 inches = yellow
# more wrong than that = red
@app.route("/check/height")
def checkheight():
    heightguessed = playerproperties(**request.args).height
    heightcorrect = playerproperties(correctplayer).height
    if (heightguessed==heightcorrect):
        final = "correct"
    elif (abs(int(heightguessed) - int(heightcorrect)) <= 2):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# determines green/yellow/red result for number of player guessed
# perfect match = green
# within 2 = yellow
# more wrong than that = red
@app.route("/check/number")
def checknumber():
    numberguessed = playerproperties(**request.args).number
    numbercorrect = playerproperties(correctplayer).number
    if (numberguessed==numbercorrect):
        final = "correct"
    elif (abs(int(numberguessed) - int(numbercorrect)) <= 2):
        final = "partially_correct"
    else:
        final = "incorrect"

    return jsonify(result=final)

# determines if the game has been won or not (correct player guessed)
@app.route("/check/winner")
def determinewinner():
    if (playerproperties(correctplayer).name == playerproperties(**request.args).name):
        return jsonify(result="winner")
    else:
        return jsonify(result="not_yet")

# returns the player at the argument index in the set order
# automatically run daily to set the new daily player
def todaysplayer(index):

# Open the text file for reading
    with open('your-text-file.txt', 'r') as file:
        # Read all lines from the file and store them in a list
        playersorder = file.readlines()

    # Each line is now a separate list entry
    # You may want to remove any trailing newline characters
    playersorder = [line.strip() for line in playersorder]

    # Now, 'lines' is a list where each entry represents a line from the text file

    

    return playersorder[index]

# overwrites the daily player in all necessary places
# run automatically daily
def changeplayer():
    global dayindex
    oldline2 = str(dayindex)
    dayindex= dayindex + 1
    newline = todaysplayer(dayindex)
    oldline = todaysplayer(dayindex - 1)
    newline2 = str(dayindex)

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/templates/main_page.html", inplace=1):
        if "Sorry, the correct answer was" in line:
            line = line.replace(oldline, newline)
        sys.stdout.write(line)

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/app.py", inplace=1):
        if "correctplayer = " in line:
            line = line.replace(oldline, newline)
        sys.stdout.write(line)

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/templates/main_page.html", inplace=1):
        if "Aurardle #" in line:
            line = line.replace(oldline2, newline2)
        sys.stdout.write(line)

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/app.py", inplace=1):
        if "dayindex = " in line:
            line = line.replace(oldline2, newline2)
        sys.stdout.write(line)

# directs a command line call to this python file to run the player overwriting function above
if __name__ == "__main__":
    changeplayer()

# renders the main screen of the game
@app.route("/", methods=["GET"])
def home():
    return render_template('main_page.html')
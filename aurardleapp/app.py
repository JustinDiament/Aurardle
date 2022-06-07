from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import fileinput
import sys

# overwritten daily
# #daily correct player that must be guessed
correctplayer = "Brooke Hobson"

# increased by one daily automatically
# the index in the set player order of the current correct player
dayindex = 62

# defines a player and their attributes that are shown to the user
class player:
    def __init__(self, name, height, sport, position, year, number):
        self.name = name
        self.height = height
        self.sport = sport
        self.position = position
        self.year = year
        self.number = number

# all players currently avalible to be guessed and their attributes
# currently includes all NU basketball, hockey, and baseball players from 2021-22
# also Tyson Walker because I said so
allplayers = [
    player("Jason Strong", 80, "MBB", "Forward", "Sr", 0),
    player("Vito Cubrilo", 76, "MBB", "Guard", "Jr", 1),
    player("Glen McClintock", 74, "MBB", "Guard", "So", 2),
    player("Tyreek Scott-Grayson", 77, "MBB", "Guard", "Sr", 10),
    player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
    player("Alex Nwagha", 80, "MBB", "Forward", "So", 12),
    player("Nikola Djogo", 80, "MBB", "Guard", "Sr", 13),
    player("Coleman Stucke", 79, "MBB", "Forward", "So", 15),
    player("Quirin Emanga", 77, "MBB", "Guard", "Jr", 22),
    player("Joe Pridgen", 77, "MBB", "Guard", "Jr", 23),
    player("Shaquille Walters", 78, "MBB", "Guard", "Sr", 24),
    player("Connor Braun", 81, "MBB", "Forward", "So", 32),
    player("Chris Doherty", 79, "MBB", "Forward", "Jr", 33),
    player("To Randriasalama", 75, "MBB", "Guard", "Fr", 55),

    player("Kendall Currence", 68, "WBB", "Guard", "Sr", 1),
    player("Izzy Larsen", 73, "WBB", "Forward", "So", 2),
    player("Donna Ntambue", 69, "WBB", "Guard", "So", 3),
    player("Century McCartney", 71, "WBB", "Guard", "Jr", 5),
    player("Camille Clement", 68, "WBB", "Guard", "Fr", 12),
    player("Katie May", 71, "WBB", "Guard", "Sr", 13),
    player("Amyrah Sapenter", 68, "WBB", "Guard", "So", 14),
    player("Anna Boruta", 70, "WBB", "Guard", "Jr", 15),
    player("Leyla Ozturk", 73, "WBB", "Forward", "So", 21),
    player("Maddie Vizza", 66, "WBB", "Guard", "So", 22),
    player("Gemima Motema", 69, "WBB", "Guard", "Fr", 23),
    player("Asha Parker", 74, "WBB", "Guard", "Fr", 24),
    player("Claudia Soriano", 67, "WBB", "Guard", "Fr", 25),
    player("Sammie Martin", 73, "WBB", "Forward", "Jr", 30),
    player("Emily Calabrese", 72, "WBB", "Forward", "Sr", 32),

    player("Alexa Matses", 68, "WHKY", "Goaltender", "Jr", 1),
    player("Lauren Macinnis", 68, "WHKY", "Defense", "Sr", 2),
    player("Gillian Foote", 72, "WHKY", "Defense", "Sr", 3),
    player("Molly Griffin", 64, "WHKY", "Wing", "So", 4),
    player("Miceala Sindoris", 65, "WHKY", "Wing", "Sr", 5),
    player("Katy Knoll", 67, "WHKY", "Center", "Jr", 6),
    player("Brooke Tucker", 68, "WHKY", "Defense", "Sr", 7),
    player("Andrea Renner", 64, "WHKY", "Wing", "Sr", 8),
    player("Emma Jurusik", 63, "WHKY", "Wing", "Sr", 9),
    player("Brooke Hobson", 66, "WHKY", "Defense", "Sr", 10),
    player("Alina Mueller", 65, "WHKY", "Center", "Sr", 11),
    player("Chloe Aurard", 66, "WHKY", "Wing", "Sr", 12),
    player("Katie Cipra", 65, "WHKY", "Wing", "Sr", 13),
    player("Mia Brown", 69, "WHKY", "Wing", "Sr", 15),
    player("Lily Yovetich", 64, "WHKY", "Defense", "So", 16),
    player("Maddie Mills", 64, "WHKY", "Wing", "Sr", 17),
    player("Abbey Marohn", 67, "WHKY", "Defense", "So", 19),
    player("Maureen Murphy", 64, "WHKY", "Wing", "Sr", 21),
    player("Skylar Fontaine", 64, "WHKY", "Defense", "Sr", 22),
    player("Kate Holmes", 62, "WHKY", "Center", "Jr", 24),
    player("Peyton Cullaton", 67, "WHKY", "Wing", "Jr", 26),
    player("Megan Carter", 68, "WHKY", "Defense", "Jr", 27),
    player("Taylor Guarino", 65, "WHKY", "Defense", "Fr", 28),
    player("Aerin Frankel", 65, "WHKY", "Goaltender", "Sr", 33),
    player("Paige Taborski", 67, "WHKY", "Goaltender", "Fr", 35),
    player("Gwyneth Philips", 67, "WHKY", "Goaltender", "Jr", 37),
    player("Tessa Ward", 69, "WHKY", "Center", "Sr", 42),
    player("Tory Mariano", 69, "WHKY", "Defense", "Fr", 44),
    player("Skylar Irving", 68, "WHKY", "Wing", "Fr", 88),
    player("Peyton Anderson", 65, "WHKY", "Wing", "Jr", 91),

    player("Devon Levi", 72, "MHKY", "Goaltender", "So", 1),
    player("Jordan Harris", 71, "MHKY", "Defense", "Sr", 2),
    player("Jayden Struble", 73, "MHKY", "Defense", "Jr", 3),
    player("Jeremie Bucheler", 76, "MHKY", "Defense", "Jr", 4),
    player("Matt Choupani", 71, "MHKY", "Wing", "Fr", 5),
    player("Chase Mcinnis", 71, "MHKY", "Wing", "Fr", 6),
    player("Michael Outzen", 72, "MHKY", "Center", "So", 7),
    player("Julian Kislin", 73, "MHKY", "Defense", "Sr", 8),
    player("Jakov Novak", 75, "MHKY", "Wing", "Sr", 10),
    player("Gunnarwolfe Fontaine", 70, "MHKY", "Wing", "So", 11),
    player("Tommy Miller", 74, "MHKY", "Defense", "Sr", 12),
    player("Ryan St. Louis", 70, "MHKY", "Wing", "Fr", 13),
    player("Ty Jackson", 68, "MHKY", "Center", "So", 14),
    player("Dylan Jackson", 70, "MHKY", "Wing", "So", 15),
    player("Sam Colangelo", 75, "MHKY", "Wing", "So", 16),
    player("Marco Bozzo", 71, "MHKY", "Wing", "Sr", 17),
    player("Tyler Spott", 71, "MHKY", "Defense", "Jr", 18),
    player("Riley Hughes", 74, "MHKY", "Wing", "Jr", 19),
    player("Alex Mella", 72, "MHKY", "Wing", "Jr", 20),
    player("Matt DeMelis", 73, "MHKY", "Wing", "Jr", 21),
    player("Cam Gaudette", 73, "MHKY", "Defense", "Fr", 23),
    player("Steven Agriogianis", 69, "MHKY", "Center", "So", 24),
    player("Aidan McDonough", 74, "MHKY", "Wing", "Jr", 25),
    player("James Davenport", 71, "MHKY", "Defense", "So", 26),
    player("Jack Hughes", 72, "MHKY", "Center", "Fr", 27),
    player("Justin Hryckowian", 70, "MHKY", "Center", "Fr", 29),
    player("TJ Semptimphelter", 73, "MHKY", "Goaltender", "Fr", 33),
    player("Evan Fear", 74, "MHKY", "Goaltender", "Jr", 35),

    player("Danny Crossen", 72, "Baseball", "UTL", "Jr", 1),
    player("Hayden Smith", 75, "Baseball", "RHP", "Fr", 2),
    player("Max Viera", 70, "Baseball", "INF", "So", 3),
    player("Dennis Colleran", 75, "Baseball", "RHP", "Fr", 4),
    player("Jeff Costello", 71, "Baseball", "OF", "Sr", 5),
    player("Cam Schlittler", 78, "Baseball", "RHP", "So", 6),
    player("Kyle Hoog", 74, "Baseball", "OF", "So", 7),
    player("Mike Sirota", 74, "Baseball", "OF", "Fr", 8),
    player("Owen Langan", 72, "Baseball", "RHP", "Jr", 9),
    player("Corey Diloreto", 76, "Baseball", "INF", "Jr", 10),
    player("Eric Yost", 73, "Baseball", "RHP", "So", 11),
    player("Sebastian Keane", 75, "Baseball", "RHP", "So", 13),
    player("Thomas Balboni", 76, "Baseball", "RHP", "So", 14),
    player("Matt Downing", 74, "Baseball", "LHP", "So", 15),
    player("Mark Darakjy", 75, "Baseball", "OF", "So", 16),
    player("Brett Dunham", 74, "Baseball", "RHP", "Fr", 17),
    player("JP Olson", 73, "Baseball", "Catcher", "So", 18),
    player("Luke Beckstein", 67, "Baseball", "INF", "So", 19),
    player("Jordy Allard", 69, "Baseball", "RHP", "Sr", 20),
    player("Justin Bosland", 77, "Baseball", "UTL", "Fr", 21),
    player("Spenser Smith", 74, "Baseball", "INF", "Jr", 22),
    player("Ed Jarvis", 71, "Baseball", "Catcher", "So", 24),
    player("Jack Doyle", 72, "Baseball", "INF", "Fr", 27),
    player("Buddy Mrowka", 71, "Baseball", "INF", "Sr", 28),
    player("Michael Gemma", 77, "Baseball", "RHP", "So", 31),
    player("James Quinlivan", 78, "Baseball", "LHP", "So", 32),
    player("Teddy Beaudet", 71, "Baseball", "Cat", "Sr", 33),
    player("Luke Masiuk", 73, "Baseball", "OF", "Fr", 34),
    player("Jack Beauchesne", 74, "Baseball", "RHP", "Fr", 35),
    player("Nick Davis", 77, "Baseball", "RHP", "Jr", 36),
    player("Jake Gigliotti", 73, "Baseball", "RHP", "So", 37),
    player("Sean Quinlivan", 73, "Baseball", "RHP", "Fr", 39),
    player("Ryan Cervone", 70, "Baseball", "OF", "So", 42),
    player("Jack Thorbahn", 75, "Baseball", "INF", "So", 43),
    player("Will Jones", 77, "Baseball", "LHP", "So", 45),
    player("Wyatt Scotti", 75, "Baseball", "RHP", "So", 46),
    player("Matt Devlin", 75, "Baseball", "LHP", "Sr", 47),
    player("Luke Bottger", 76, "Baseball", "LHP", "So", 48),
    player("Gregory Bozzo", 72, "Baseball", "Catcher", "So", 49),

    player("Tyson Walker", 72, "MBB", "Guard", "Jr", 2)
]

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
        final = "true"
    elif ((sportguessed=="MBB" and sportcorrect=="WBB") or (sportguessed=="WBB" and sportcorrect=="MBB")):
        final = "middle"
    elif ((sportguessed=="MHKY" and sportcorrect=="WHKY") or (sportguessed=="WHKY" and sportcorrect=="MHKY")):
        final = "middle"
    else:
        final = "false"

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
        final = "true"
    elif (positionguessed=="Catcher" and (positioncorrect=="UTL" or positionguessed=="OF" and positioncorrect=="INF")):
        final = "middle"
    elif (positionguessed=="UTL" and (positioncorrect=="Catcher" or positionguessed=="OF" and positioncorrect=="INF")):
        final = "middle"
    elif (positionguessed=="OF" and (positioncorrect=="Catcher" or positionguessed=="UTL" and positioncorrect=="INF")):
        final = "middle"
    elif (positionguessed=="INF" and (positioncorrect=="Catcher" or positionguessed=="UTL" and positioncorrect=="OF")):
        final = "middle"
    elif (positionguessed=="LHP" and positioncorrect=="RHP"):
        final = "middle"
    elif (positionguessed=="RHP" and positioncorrect=="LHP"):
        final = "middle"
    else:
        final = "false"

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
        final = "true"
    elif (abs(int(heightguessed) - int(heightcorrect)) <= 2):
        final = "middle"
    else:
        final = "false"

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
        final = "true"
    elif (abs(int(numberguessed) - int(numbercorrect)) <= 2):
        final = "middle"
    else:
        final = "false"

    return jsonify(result=final)

# determines if the game has been won or not (correct player guessed)
# two functions seems unneccessary, but when I try to reduce it to one, the winning check breaks :(
# so, two functions will remain!
@app.route("/check/winner")
def determinewinner():
    if determinewinner2(**request.args):
        return jsonify(result="winner")
    else:
        return jsonify(result="notyet")

# helps out with the winner check in mysterious ways. see above
def determinewinner2(playertyped):
    return (playertyped==correctplayer)

# returns the player at the argument index in the set order
# automatically run daily to set the new daily player
def todaysplayer(index):
    playersorder=[
    "Fake Player",
    "Sam Colangelo",
    "Coleman Stucke",
    "Skylar Fontaine",
    "Cam Schlittler",
    "Katie May",
    "Tessa Ward",
    "Alex Nwagha",
    "Jayden Struble",
    "Matt DeMelis",
    "Katy Knoll",
    "Mike Sirota",
    "Emma Jurusik",
    "Thomas Balboni",
    "TJ Semptimphelter",
    "Maddie Vizza",
    "Teddy Beaudet",
    "Gunnarwolfe Fontaine",
    "Nikola Djogo",
    "Andrea Renner",
    "Danny Crossen",
    "Jason Strong",
    "Devon Levi",
    "Izzy Larsen",
    "Molly Griffin",
    "Chris Doherty",
    "Tyreek Scott-Grayson",
    "Tyler Spott",
    "Katie Cipra",
    "Chloe Aurard",
    "Steven Agriogianis",
    "Alex Mella",
    "Abbey Marohn",
    "Brett Dunham",
    "Michael Outzen",
    "Anna Boruta",
    "Peyton Cullaton",
    "Jeremie Bucheler",
    "Mia Brown",
    "Skylar Irving",
    "Jordy Allard",
    "Kendall Currence",
    "Ryan St. Louis",
    "Will Jones",
    "Luke Beckstein",
    "Jack Hughes",
    "Lauren Macinnis",
    "Dylan Jackson",
    "Max Viera",
    "Ryan Cervone",
    "Luke Bottger",
    "Nick Davis",
    "Amyrah Sapenter",
    "Paige Taborski",
    "Jeff Costello",
    "Jack Beauchesne",
    "Jahmyl Telfort",
    "Cam Gaudette",
    "Gwyneth Philips",
    "Jake Gigliotti",
    "Connor Braun",
    "Tory Mariano",
    "Brooke Hobson",
    "Matt Downing",
    "Sebastian Keane",
    "Jordan Harris",
    "Ed Jarvis",
    "Gemima Motema",
    "Riley Hughes",
    "Joe Pridgen",
    "Vito Cubrilo",
    "Kate Holmes",
    "Jakov Novak",
    "Ty Jackson",
    "Camille Clement",
    "Spenser Smith",
    "To Randriasalama",
    "Kyle Hoog",
    "Century McCartney",
    "Leyla Ozturk",
    "Dennis Colleran",
    "Justin Hryckowian",
    "Wyatt Scotti",
    "Brooke Tucker",
    "Miceala Sindoris",
    "Gregory Bozzo",
    "Justin Bosland",
    "Luke Masiuk",
    "Gillian Foote",
    "Maureen Murphy",
    "Asha Parker",
    "Julian Kislin",
    "Lily Yovetich",
    "Mark Darakjy",
    "Hayden Smith",
    "Evan Fear",
    "Jack Thorbahn",
    "Eric Yost",
    "Sammie Martin",
    "James Quinlivan",
    "Alexa Matses",
    "Aidan McDonough",
    "Shaquille Walters",
    "James Davenport",
    "Aerin Frankel",
    "Maddie Mills",
    "Jack Doyle",
    "Buddy Mrowka",
    "Jack Doyle",
    "Matt Devlin",
    "Sean Quinlivan",
    "Emily Calabrese",
    "Alina Mueller",
    "Taylor Guarino",
    "Michael Gemma",
    "Owen Langan",
    "Donna Ntambue",
    "Marco Bozzo",
    "Glen McClintock",
    "Matt Choupani",
    "Claudia Soriano",
    "Quirin Emanga",
    "Peyton Anderson",
    "Megan Carter",
    "Corey Diloreto",
    "JP Olson",
    "Tommy Miller",
    "Chase Mcinnis"]

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

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/templates/my-form.html", inplace=1):
        if "Sorry, the correct answer was" in line:
            line = line.replace(oldline, newline)
        sys.stdout.write(line)

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/app.py", inplace=1):
        if "correctplayer = " in line:
            line = line.replace(oldline, newline)
        sys.stdout.write(line)

    for line in fileinput.input("/home/Aurardle/aurardle/aurardleapp/templates/my-form.html", inplace=1):
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
    return render_template('my-form.html')
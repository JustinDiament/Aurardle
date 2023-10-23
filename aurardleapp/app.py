from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import fileinput
import sys

# overwritten daily
# #daily correct player that must be guessed
correctplayer = "Matt Downing"

# increased by one daily automatically
# the index in the set player order of the current correct player
dayindex = 125

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
# currently includes all NU basketball and hockey players from 2022-23
# plus, all NU baseball players from 2021-22
# also Tyson Walker because I said so
allplayers = [
    player("Masai Troutman", 78, "MBB", "Guard", "Fr", 1),
    player("Glen McClintock", 74, "MBB", "Guard", "Jr", 2),
    player("Chase Cormier", 74, "MBB", "Guard", "Fr", 3),
    player("Rashad King", 78, "MBB", "Guard", "Fr", 4),
    player("Harold Woods", 77, "MBB", "Guard", "Fr", 10),
    player("Jahmyl Telfort", 79, "MBB", "Guard", "Jr", 11),
    player("Alex Nwagha", 80, "MBB", "Forward", "Jr", 12),
    player("Jared Turner", 80, "MBB", "Guard", "Fr", 13),
    player("Coleman Stucke", 79, "MBB", "Forward", "Jr", 15),
    player("Joe Pridgen", 77, "MBB", "Guard", "Jr", 23),
    player("Chris Doherty", 79, "MBB", "Forward", "Sr", 33),
    player("Collin Metcalf", 81, "MBB", "Forward", "Fr", 45),
    player("To Randriasalama", 75, "MBB", "Guard", "So", 55),

    player("Jaelyn Batts", 72, "WBB", "Guard", "Sr", 0),
    player("Derin Erdogan", 66, "WBB", "Guard", "Jr", 1),
    player("Izzy Larsen", 73, "WBB", "Forward", "Jr", 2),
    player("Jamiya Braxton", 77, "WBB", "Guard", "Sr", 3),
    player("Oralye Kiefer", 75, "WBB", "Forward", "Fr", 11),
    player("Camille Clement", 68, "WBB", "Guard", "So", 12),
    player("Deja Bristol", 73, "WBB", "Forward", "Jr", 13),
    player("Amyrah Sapenter", 68, "WBB", "Guard", "Jr", 14),
    player("Anna Boruta", 70, "WBB", "Guard", "Sr", 15),
    player("Ariana Webb", 69, "WBB", "Guard", "Fr", 21),
    player("Maddie Vizza", 66, "WBB", "Guard", "Jr", 22),
    player("Gemima Motema", 69, "WBB", "Guard", "So", 23),
    player("Asha Parker", 74, "WBB", "Guard", "So", 24),
    player("Marian Turnbull", 57, "WBB", "Guard", "Fr", 32),
    player("Halle Idowu", 71, "WBB", "Guard", "Jr", 35),

    player("Alexa Matses", 68, "WHKY", "Goaltender", "Sr", 1),
    player("Lily Shannon", 70, "WHKY", "Wing", "Sr", 2),
    player("Tory Mariano", 69, "WHKY", "Defense", "So", 4),
    player("Katy Knoll", 67, "WHKY", "Center", "Sr", 6),
    player("Molly Griffin", 64, "WHKY", "Wing", "Jr", 8),
    player("Kristina Allard", 64, "WHKY", "Defense", "Fr", 9),
    player("Holly Abela", 65, "WHKY", "Wing", "Fr", 10),
    player("Alina Mueller", 65, "WHKY", "Center", "Sr", 11),
    player("Chloe Aurard", 66, "WHKY", "Wing", "Sr", 12),
    player("Mia Brown", 69, "WHKY", "Wing", "Sr", 15),
    player("Lily Yovetich", 64, "WHKY", "Defense", "Jr", 16),
    player("Mia Langolis", 67, "WHKY", "Wing", "Fr", 17),
    player("Abbey Marohn", 67, "WHKY", "Defense", "Jr", 19),
    player("Maureen Murphy", 64, "WHKY", "Wing", "Sr", 21),
    player("Peyton Cullaton", 67, "WHKY", "Wing", "Sr", 23),
    player("Kate Holmes", 62, "WHKY", "Center", "Sr", 24),
    player("Megan Carter", 68, "WHKY", "Defense", "Sr", 27),
    player("Taylor Guarino", 65, "WHKY", "Defense", "So", 28),
    player("Paige Taborski", 67, "WHKY", "Goaltender", "So", 35),
    player("Gwyneth Philips", 67, "WHKY", "Goaltender", "Sr", 37),
    player("Jules Constantinople", 65, "WHKY", "Defense", "Fr", 41),
    player("Taze Thompson", 66, "WHKY", "Wing", "So", 44),
    player("Lily Brazis", 65, "WHKY", "Wing", "Fr", 61),
    player("Maude Poulin-Labelle", 66, "WHKY", "Defense", "Sr", 76),
    player("Skylar Irving", 68, "WHKY", "Wing", "So", 88),
    player("Peyton Anderson", 65, "WHKY", "Wing", "Sr", 91),
    player("Avery Anderson", 66, "WHKY", "Wing", "Fr", 92),
    player("Alyssa Antonakis", 66, "WHKY", "Wing", "Fr", 94),

    player("Devon Levi", 72, "MHKY", "Goaltender", "Jr", 1),
    player("Jayden Struble", 73, "MHKY", "Defense", "Sr", 3),
    player("Jeremie Bucheler", 76, "MHKY", "Defense", "Sr", 4),
    player("Hunter McDonald", 76, "MHKY", "Defense", "Fr", 5),
    player("Chase Mcinnis", 71, "MHKY", "Wing", "So", 6),
    player("Michael Outzen", 72, "MHKY", "Center", "Jr", 7),
    player("Jackson Dorrington", 74, "MHKY", "Defense", "Fr", 8),
    player("Matt Choupani", 71, "MHKY", "Wing", "So", 9),
    player("Jakov Novak", 75, "MHKY", "Wing", "Sr", 10),
    player("Gunnarwolfe Fontaine", 70, "MHKY", "Wing", "Jr", 11),
    player("Cam Lund", 74, "MHKY", "Wing", "Fr", 12),
    player("Liam Walsh", 73, "MHKY", "Center", "Sr", 14),
    player("Jack Williams", 71, "MHKY", "Wing", "Fr", 15),
    player("Sam Colangelo", 75, "MHKY", "Wing", "Jr", 16),
    player("Braden Doyle", 72, "MHKY", "Defense", "So", 17),
    player("Tyler Spott", 71, "MHKY", "Defense", "Sr", 18),
    player("Riley Hughes", 74, "MHKY", "Wing", "Sr", 19),
    player("Alex Mella", 72, "MHKY", "Wing", "Sr", 20),
    player("Matt DeMelis", 73, "MHKY", "Center", "Sr", 21),
    player("Vinny Borgesi", 68, "MHKY", "Defense", "Fr", 22),
    player("Cam Gaudette", 73, "MHKY", "Defense", "So", 23),
    player("Kyle Furey", 72, "MHKY", "Defense", "Fr", 24),
    player("Aidan McDonough", 74, "MHKY", "Wing", "Sr", 25),
    player("James Davenport", 71, "MHKY", "Defense", "Jr", 26),
    player("Jack Hughes", 72, "MHKY", "Center", "So", 27),
    player("Anthony Messuri", 68, "MHKY", "Wing", "Fr", 28),
    player("Justin Hryckowian", 70, "MHKY", "Center", "So", 29),
    player("Harrison Chesney", 75, "MHKY", "Goaltender", "Fr", 35),
    player("Grant Riley", 76, "MHKY", "Goaltender", "Fr", 37),

    player("Danny Crossen", 72, "Baseball", "UTL", "Sr", 1),
    player("Hayden Smith", 75, "Baseball", "RHP", "So", 2),
    player("Jack Thorbahn", 75, "Baseball", "INF", "Jr", 3),
    player("Dennis Colleran", 75, "Baseball", "RHP", "Jr", 4),
    player("Sean McGee", 73, "Baseball", "INF", "Fr", 5),
    player("Aiven Cabral", 71, "Baseball", "RHP", "Fr", 6),
    player("Cam Maldonado", 75, "Baseball", "OF", "Fr", 7),
    player("Mike Sirota", 74, "Baseball", "OF", "So", 8),
    player("Harrison Feinberg", 73, "Baseball", "OF", "So", 9),
    player("Alex Lane", 77, "Baseball", "OF", "Sr", 10),
    player("Eric Yost", 73, "Baseball", "RHP", "Jr", 11),
    player("Joseph Hauser", 75, "Baseball", "RHP", "Fr", 12),
    player("Matt Brinker", 70, "Baseball", "Catcher", "Fr", 13),
    player("Patrick Harrington", 73, "Baseball", "RHP", "Sr", 14),
    player("Matt Downing", 74, "Baseball", "LHP", "Jr", 15),
    player("Ryan Griffin", 78, "Baseball", "RHP", "Fr", 16),
    player("Brett Dunham", 74, "Baseball", "RHP", "So", 17),
    player("Griffin Young", 76, "Baseball", "RHP", "Sr", 18),
    player("Luke Beckstein", 67, "Baseball", "INF", "Jr", 19),
    player("Jordy Allard", 69, "Baseball", "RHP", "Sr", 20),
    player("Justin Bosland", 77, "Baseball", "UTL", "So", 21),
    player("Spenser Smith", 74, "Baseball", "INF", "Sr", 22),
    player("Ed Jarvis", 71, "Baseball", "Catcher", "Jr", 24),
    player("Craig Ottaviano", 77, "Baseball", "RHP", "Fr", 25),
    player("Jack Doyle", 72, "Baseball", "INF", "So", 27),
    player("Melo Musacchia", 72, "Baseball", "INF", "Fr", 28),
    player("Michael Gemma", 77, "Baseball", "RHP", "Jr", 31),
    player("James Quinlivan", 78, "Baseball", "LHP", "Jr", 32),
    player("Tyler MacGregor", 73, "Baseball", "INF", "Sr", 33),
    player("Luke Masiuk", 73, "Baseball", "OF", "So", 34),
    player("Jack Beauchesne", 74, "Baseball", "RHP", "So", 35),
    player("Nick Davis", 77, "Baseball", "RHP", "Sr", 36),
    player("Jake Gigliotti", 73, "Baseball", "RHP", "Jr", 37),
    player("Sean Quinlivan", 73, "Baseball", "RHP", "So", 39),
    player("Carson Walsh", 72, "Baseball", "RHP", "So", 43),
    player("Jimmy Sullivan", 72, "Baseball", "Catcher", "Fr", 45),
    player("Will Jones", 77, "Baseball", "LHP", "Jr", 45),
    player("Wyatt Scotti", 75, "Baseball", "RHP", "Jr", 46),
    player("James Morice", 77, "Baseball", "RHP", "Fr", 47),
    player("Gregory Bozzo", 72, "Baseball", "Catcher", "Jr", 49),

    player("Tyson Walker", 72, "MBB", "Guard", "Sr", 2)
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
    "Craig Ottaviano",
    "Rashad King",
    "Alex Lane",
    "Gwyneth Philips",
    "Halle Idowu",
    "To Randriasalama",
    "Maude Poulin-Labelle",
    "Asha Parker",
    "Jahmyl Telfort",
    "Jimmy Sullivan",
    "Peyton Cullaton",
    "Cam Lund",
    "Marian Turnbull",
    "Alex Mella",
    "James Davenport",
    "Tyler MacGregor",
    "Gunnarwolfe Fontaine",
    "Kristina Allard",
    "Jamiya Braxton",
    "Danny Crossen",
    "Avery Anderson",
    "Gregory Bozzo",
    "Jack Beauchesne",
    "Lily Brazis",
    "Ryan Griffin",
    "Camille Clement",
    "Masai Troutman",
    "Jakov Novak",
    "Chris Doherty",
    "Aidan McDonough",
    "Amyrah Sapenter",
    "Braden Doyle",
    "Deja Bristol",
    "Collin Metcalf",
    "Patrick Harrington",
    "Griffin Young",
    "Joseph Hauser",
    "Alina Mueller",
    "Brett Dunham",
    "Mike Sirota",
    "Luke Masiuk",
    "Holly Abela",
    "Cam Maldonado",
    "Harold Woods",
    "Sean McGee",
    "Jordy Allard",
    "Wyatt Scotti",
    "Aiven Cabral",
    "Eric Yost",
    "Cam Gaudette",
    "Megan Carter",
    "Liam Walsh",
    "Jake Gigliotti",
    "Jaelyn Batts",
    "Hunter McDonald",
    "Vinny Borgesi",
    "Jack Doyle",
    "Spenser Smith",
    "Jules Constantinople",
    "Ed Jarvis",
    "Jared Turner",
    "Carson Walsh",
    "Katy Knoll",
    "Justin Hryckowian",
    "Maddie Vizza",
    "Joe Pridgen",
    "Alex Nwagha",
    "Grant Riley",
    "Skylar Irving",
    "Michael Gemma",
    "Izzy Larsen",
    "Mia Brown",
    "Oralye Kiefer",
    "Chase Mcinnis",
    "Alyssa Antonakis",
    "James Morice",
    "Anna Boruta",
    "Mia Langolis",
    "Paige Taborski",
    "Nick Davis",
    "Hayden Smith",
    "Peyton Anderson",
    "Taylor Guarino",
    "Molly Griffin",
    "Harrison Feinberg",
    "Jayden Struble",
    "Jack Hughes",
    "Jackson Dorrington",
    "Jack Williams",
    "Dennis Colleran",
    "Taze Thompson",
    "Kyle Furey",
    "Jeremie Bucheler",
    "Connor Braun",
    "Maureen Murphy",
    "Riley Hughes",
    "Derin Erdogan",
    "Sean Quinlivan",
    "Tory Mariano",
    "Glen McClintock",
    "Sam Colangelo",
    "Harrison Chesney",
    "Lily Yovetich",
    "Devon Levi",
    "Chase Cormier",
    "Chloe Aurard",
    "Matt Brinker",
    "Kate Holmes",
    "Tyler Spott",
    "Michael Outzen",
    "Lily Shannon",
    "Jack Thorbahn",
    "Gemima Motema",
    "Alexa Matses",
    "Matt Choupani",
    "Will Jones",
    "Matt DeMelis",
    "Ariana Webb",
    "Melo Musacchia",
    "Coleman Stucke",
    "Abbey Marohn",
    "Justin Bosland",
    "Luke Beckstein",
    "James Quinlivan",
    "Matt Downing"]

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
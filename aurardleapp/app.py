from flask import Flask, render_template, request, make_response
app = Flask(__name__)

global globalnamecolors
globalnamecolors = ["ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"]

global globalheightcolors
globalheightcolors = ["ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"]

global globalsportcolors
globalsportcolors = ["ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"]

global globalpositioncolors
globalpositioncolors = ["ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"]

global globalyearcolors
globalyearcolors = ["ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"]

global globalnumbercolors
globalnumbercolors = ["ffffff", "ffffff", "ffffff", "ffffff", "ffffff", "ffffff"]

global globalguesses 
globalguesses = 0

global guesstext
guesstext = "Guess 1 of 5"

global rows
rows = ["rowinvisible", "rowinvisible", "rowinvisible", "rowinvisible", "rowinvisible"]

class player:
    def __init__(self, name, height, sport, position, year, number):
        self.name = name
        self.height = height
        self.sport = sport
        self.position = position
        self.year = year
        self.number = number

global chosenplayers
chosenplayers = [player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
]

global chosenplayerdisplayheights 
chosenplayerdisplayheights = ["", "", "", "", ""]

@app.route("/", methods=["POST", "GET"])
def home():
    playernames = [player("Jahmyl Telfort", 79, "MBB", "Guard", "So", 11),
        player("Jason Strong", 80, "MBB", "Forward", "Sr", 0),
        player("Vito Cubrilo", 76, "MBB", "Guard", "Jr", 1),
        player("Glen McClintock", 74, "MBB", "Guard", "So", 2),
        player("Tyreek Scott-Grayson", 77, "MBB", "Guard", "Sr", 10),
        player("Alex Nwagha", 80, "MBB", "Forward", "So", 12),
        player("Nikola Djogo", 80, "MBB", "Guard", "Sr", 13),
        player("Coleman Stucke", 79, "MBB", "Forward", "So", 15),
        player("Quirin Emanga", 77, "MBB", "Guard", "Jr", 22),
        player("Joe Pridgen", 77, "MBB", "Guard", "Jr", 23),
        player("Shaquille Walters", 78, "MBB", "Guard", "Sr", 24),
        player("Connor Braun", 81, "MBB", "Forward", "So", 32),
        player("Chris Doherty", 79, "MBB", "Forward", "Jr", 33),
        player("To Randriasalama", 75, "MBB", "Guard", "Fr", 55),

        player("Kendall Currence", 63, "WBB", "Guard", "Sr", 1),
        player("Izzy Larson", 73, "WBB", "Forward", "So", 2),
        player("Donna Ntambue", 69, "WBB", "Guard", "So", 3),
        player("Century McCartney", 71, "WBB", "Guard", "Jr", 5),
        player("Camille Clement", 68, "WBB", "Guard", "Fr", 12),
        player("Katie May", 71, "WBB", "Guard", "Sr", 13),
        player("Amryah Sapenter", 68, "WBB", "Guard", "So", 14),
        player("Anna Boruta", 70, "WBB", "Guard", "Jr", 15),
        player("Leyla Ozturk", 73, "WBB", "Guard", "So", 21),
        player("Maddie Vizza", 66, "WBB", "Guard", "So", 22),
        player("Gemima Motema", 69, "WBB", "Guard", "Fr", 23),
        player("Asha Parker", 74, "WBB", "Guard", "Fr", 24),
        player("Claudia Soriano", 67, "WBB", "Guard", "Fr", 25),
        player("Sammie Martin", 73, "WBB", "Forward", "Jr", 30),
        player("Emily Calabrese", 72, "WBB", "Forward", "Sr", 32),

        player("Alexa Matses", 68, "WHKY", "Gl", "Jr", 1),
        player("Lauren Macinnis", 68, "WHKY", "Def", "Sr", 2),
        player("Gillian Foote", 72, "WHKY", "Def", "Sr", 3),
        player("Molly Griffin", 64, "WHKY", "For", "So", 4),
        player("Miceala Sindoris", 65, "WHKY", "For", "Sr", 5),
        player("Katy Knoll", 67, "WHKY", "For", "Jr", 6),
        player("Brooke Tucker", 68, "WHKY", "Def", "Sr", 7),
        player("Andrea Renner", 64, "WHKY", "For", "Sr", 8),
        player("Emma Jurusik", 63, "WHKY", "For", "Sr", 9),
        player("Brooke Hobson", 66, "WHKY", "Def", "Sr", 10),
        player("Alina Mueller", 65, "WHKY", "For", "Sr", 11),
        player("Chloe Aurard", 66, "WHKY", "For", "Sr", 12),
        player("Katie Cipra", 65, "WHKY", "For", "Sr", 13),
        player("Mia Brown", 69, "WHKY", "For", "Sr", 15),
        player("Lily Yovetich", 64, "WHKY", "Def", "So", 16),
        player("Maddie Mills", 64, "WHKY", "For", "Sr", 17),
        player("Abbey Marohn", 67, "WHKY", "Def", "So", 19),
        player("Maureen Murphy", 64, "WHKY", "For", "Sr", 21),
        player("Skylar Fontaine", 64, "WHKY", "Def", "Sr", 22),
        player("Kate Holmes", 62, "WHKY", "For", "Jr", 24),
        player("Peyton Cullaton", 67, "WHKY", "For", "Jr", 26),
        player("Megan Carter", 68, "WHKY", "Def", "Jr", 27),
        player("Taylor Guarino", 65, "WHKY", "Def", "Fr", 28),
        player("Aerin Frankel", 65, "WHKY", "Gl", "Sr", 33),
        player("Paige Taborski", 67, "WHKY", "Gl", "Fr", 35),
        player("Gwyneth Philips", 67, "WHKY", "Gl", "Jr", 37),
        player("Tessa Ward", 69, "WHKY", "For", "Jr", 42),
        player("Tory Mariano", 69, "WHKY", "For", "Fr", 44),
        player("Skylar Irving", 68, "WHKY", "For", "Fr", 88),
        player("Peyton Anderson", 65, "WHKY", "For", "Jr", 91),

        player("Devon Levi", 72, "MHKY", "Gl", "So", 1),
        player("Jordan Harris", 71, "MHKY", "Def", "Sr", 2),
        player("Jayden Struble", 73, "MHKY", "Def", "Jr", 3),
        player("Jeremie Bucheler", 76, "MHKY", "Def", "Jr", 4),
        player("Matt Choupani", 71, "MHKY", "For", "Fr", 5),
        player("Chase Mcinnis", 71, "MHKY", "For", "Fr", 6),
        player("Michael Outzen", 72, "MHKY", "For", "So", 7),
        player("Julian Kislin", 73, "MHKY", "Def", "Sr", 8),
        player("Jakov Novak", 75, "MHKY", "For", "Sr", 10),
        player("Gunnarwolfe Fontaine", 70, "MHKY", "For", "So", 11),
        player("Tommy Miller", 74, "MHKY", "Def", "Sr", 12),
        player("Ryan St. Louis", 70, "MHKY", "For", "Fr", 13),
        player("Ty Jackson", 68, "MHKY", "For", "So", 14),
        player("Dylan Jackson", 70, "MHKY", "For", "So", 15),
        player("Sam Colangelo", 75, "MHKY", "For", "So", 16),
        player("Marco Bozzo", 71, "MHKY", "For", "Sr", 17),
        player("Tyler Spott", 71, "MHKY", "Def", "Jr", 18),
        player("Riley Hughes", 74, "MHKY", "For", "Jr", 19),
        player("Alex Mella", 72, "MHKY", "For", "Jr", 20),
        player("Matt Demelis", 73, "MHKY", "For", "Jr", 21),
        player("Cam Gaudette", 73, "MHKY", "Def", "Fr", 23),
        player("Steven Agriogianis", 69, "MHKY", "For", "So", 24),
        player("Aidan McDonough", 74, "MHKY", "For", "Jr", 25),
        player("James Davenport", 71, "MHKY", "Def", "So", 26),
        player("Jack Hughes", 72, "MHKY", "For", "Fr", 27),
        player("Justin Hryckowian", 70, "MHKY", "For", "Fr", 29),
        player("TJ Semptimphelter", 73, "MHKY", "Gl", "Fr", 29),
        player("Evan Fear", 74, "MHKY", "Gl", "Jr", 35),

        player("Danny Crossen", 72, "Baseball", "UTL", "Jr", 1),
        player("Hayden Smith", 75, "Baseball", "RHP", "Fr", 2),
        player("Max Viera", 70, "Baseball", "INF", "Fr", 3),
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
        player("JP Olson", 73, "Baseball", "Catcher", "Fr", 18),
        player("Luke Beckstein", 67, "Baseball", "INF", "So", 19),
        player("Jordy Allard", 69, "Baseball", "RHP", "Sr", 20),
        player("Justin Bosland", 77, "Baseball", "UTL", "Fr", 21),
        player("Spenser Smith", 74, "Baseball", "INF", "Jr", 22),
        player("Ed Jarvis", 71, "Baseball", "Catcher", "So", 24),
        player("Buddy Mrowka", 71, "Baseball", "INF", "Sr", 28),
        player("Michael Gemma", 77, "Baseball", "RHP", "Sr", 31),
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

        player("Tyson Walker", 72, "MBB", "Guard", "Jr", 2)]


    playernamessuggest = []
    for player2 in playernames:
        playernamessuggest.append(player2.name)

    if request.method == "GET":
        return render_template('my-form.html', 
                    namecolor1 = globalnamecolors[1],
                    namecolor2 = globalnamecolors[2],
                    namecolor3 = globalnamecolors[3],
                    namecolor4 = globalnamecolors[4],
                    namecolor5 = globalnamecolors[5],   

                    heightcolor1 = globalheightcolors[1],  
                    heightcolor2 = globalheightcolors[2],  
                    heightcolor3 = globalheightcolors[3],  
                    heightcolor4 = globalheightcolors[4],  
                    heightcolor5 = globalheightcolors[5],  
            
                    sportcolor1 = globalsportcolors[1],  
                    sportcolor2 = globalsportcolors[2],  
                    sportcolor3 = globalsportcolors[3],  
                    sportcolor4 = globalsportcolors[4],  
                    sportcolor5 = globalsportcolors[5],  

                    positioncolor1 = globalpositioncolors[1],  
                    positioncolor2 = globalpositioncolors[2],  
                    positioncolor3 = globalpositioncolors[3],  
                    positioncolor4 = globalpositioncolors[4],  
                    positioncolor5 = globalpositioncolors[5],  

                    yearcolor1 = globalpositioncolors[1],  
                    yearcolor2 = globalpositioncolors[2],  
                    yearcolor3 = globalpositioncolors[3],  
                    yearcolor4 = globalpositioncolors[4],  
                    yearcolor5 = globalpositioncolors[5],  

                    numbercolor1 = globalyearcolors[1],  
                    numbercolor2 = globalyearcolors[2],  
                    numbercolor3 = globalyearcolors[3],  
                    numbercolor4 = globalyearcolors[4],  
                    numbercolor5 = globalyearcolors[5],
                    
                    playernames=playernamessuggest, 
                    guessblankofblank=guesstext,
                    
                    row1=rows[0],
                    row2=rows[1],
                    row3=rows[2],
                    row4=rows[3],
                    row5=rows[4],

                    name1=chosenplayers[0].name,
                    name2=chosenplayers[1].name,
                    name3=chosenplayers[2].name,
                    name4=chosenplayers[3].name,
                    name5=chosenplayers[4].name,

                    height1=chosenplayers[0].height,
                    height2=chosenplayers[1].height,
                    height3=chosenplayers[2].height,
                    height4=chosenplayers[3].height,
                    height5=chosenplayers[4].height,

                    sport1=chosenplayers[0].sport,
                    sport2=chosenplayers[1].sport,
                    sport3=chosenplayers[2].sport,
                    sport4=chosenplayers[3].sport,
                    sport5=chosenplayers[4].sport,

                    position1=chosenplayers[0].position,
                    position2=chosenplayers[1].position,
                    position3=chosenplayers[2].position,
                    position4=chosenplayers[3].position,
                    position5=chosenplayers[4].position,

                    year1=chosenplayers[0].year,
                    year2=chosenplayers[1].year,
                    year3=chosenplayers[2].year,
                    year4=chosenplayers[3].year,
                    year5=chosenplayers[4].year,

                    number1=chosenplayers[0].number,
                    number2=chosenplayers[1].number,
                    number3=chosenplayers[2].number,
                    number4=chosenplayers[3].number,
                    number5=chosenplayers[4].number

                    )
    
    if request.method == "POST":

        userplayername = request.form['text']
        userplayer = None

        global globalguesses

        playernum = 19

        todaysname = playernames[playernum].name
        todaysheight = playernames[playernum].height
        todayssport = playernames[playernum].sport
        todaysposition = playernames[playernum].position
        todaysyear = playernames[playernum].year
        todaysnumber = playernames[playernum].number

        for player1 in playernames:
            if player1.name == userplayername:
                userplayer = player1
                break
        
        chosenplayers[globalguesses] = userplayer

        if (userplayer.name.lower() == todaysname.lower()):
            globalnamecolors[globalguesses + 1] = "0f9f6e"
        else:
            globalnamecolors[globalguesses + 1] = "f4f2ec" # red/grey

        if (userplayer.height == todaysheight):
            globalheightcolors[globalguesses + 1] = "0f9f6e" # green
        elif (abs (userplayer.height - todaysheight) <= 2):
            globalheightcolors[globalguesses + 1] = "faca17" # yellow
        else:
            globalheightcolors[globalguesses + 1] = "e2e8f0" # red

        if (userplayer.sport == todayssport):
            globalsportcolors[globalguesses + 1] = "0f9f6e" # green
        elif ((userplayer.sport == "WBB" and todayssport == "MBB") or (userplayer.sport == "MBB" and todayssport == "WBB")):
            globalsportcolors[globalguesses + 1] = "faca17" # yellow
        elif ((userplayer.sport == "WHKY" and todayssport == "MHKY") or (userplayer.sport == "MHKY" and todayssport == "WHKY")):
            globalsportcolors[globalguesses + 1] = "faca17" # yellow
        else:
            globalsportcolors[globalguesses + 1] = "e2e8f0" # red
        
        if (userplayer.position == todaysposition):
            globalpositioncolors[globalguesses + 1] = "0f9f6e" # green
        elif (todayssport == "Baseball" and ((todaysposition == "INF" or todaysposition == "OF" or todaysposition == "UTL" or todaysposition == "C") and (userplayer.position == "INF" or userplayer.position == "OF" or userplayer.position == "UTL" or userplayer.position == "C"))):
            globalpositioncolors[globalguesses + 1] = "faca17" # yellow
        elif (todayssport == "Baseball" and ((todaysposition == "LHP" or todaysposition == "RHP") and (userplayer.position == "LHP" or userplayer.position == "RHP"))):
            globalpositioncolors[globalguesses + 1] = "faca17" # yellow
        else:
            globalpositioncolors[globalguesses + 1] = "e2e8f0" # red

        if (userplayer.number == todaysnumber):
            globalnumbercolors[globalguesses + 1] = "0f9f6e" # green
        elif (abs (userplayer.number - todaysnumber) <= 2):
            globalnumbercolors[globalguesses + 1] = "faca17" # yellow
        else:
            globalnumbercolors[globalguesses + 1] = "e2e8f0" # red

        if (userplayer.year == todaysyear):
            globalyearcolors[globalguesses + 1] = "0f9f6e" # green
        else:
            globalyearcolors[globalguesses + 1] = "e2e8f0" # red

        chosenplayerheightfeet = chosenplayers[globalguesses].height // 12
        chosenplayerheightinches = chosenplayers[globalguesses].height - (chosenplayerheightfeet * 12)
        chosenplayerdisplayheights[globalguesses] = str(chosenplayerheightfeet) + '′' + " " + str(chosenplayerheightinches) + "″"

        globalguesses = globalguesses + 1

        gameover="false"
        lost = "nah"

        if (globalguesses == 5):
            gameover="true"
            lost="loser"

        for i in range (0, globalguesses):
            rows[i] = "rowvisible"

        won="nope"
        shareboard = ["", "", "", "", "", ""]
        if (userplayer.name.lower() == todaysname.lower()):
            won="winner"
            gameover="true"
            lost="nah"
        for i in range (1, globalguesses+1):
            if (globalnamecolors[i]=="0f9f6e"):
                shareboard[i] = shareboard[i] + '\U0001F7E9'
            else: 
                shareboard[i] = shareboard[i] + '\U00002B1B'

            if (globalsportcolors[i]=='0f9f6e'):
                shareboard[i] = shareboard[i] + '\U0001F7E9'
            elif globalsportcolors[i]=='faca17':
                shareboard[i] = shareboard[i] + '\U0001F7E8'
            else: 
                shareboard[i] = shareboard[i] + '\U00002B1B'

            if (globalpositioncolors[i]=='0f9f6e'):
                shareboard[i] = shareboard[i] + '\U0001F7E9'
            elif globalpositioncolors[i]=='faca17':
                shareboard[i] = shareboard[i] + '\U0001F7E8'
            else: 
                shareboard[i] = shareboard[i] + '\U00002B1B'
            
            if (globalyearcolors[i]=='0f9f6e'):
                shareboard[i] = shareboard[i] + '\U0001F7E9'
            else: 
                shareboard[i] = shareboard[i] + '\U00002B1B'

            if (globalheightcolors[i]=='0f9f6e'):
                shareboard[i] = shareboard[i] + '\U0001F7E9'
            elif globalheightcolors[i]=='faca17':
                shareboard[i] = shareboard[i] + '\U0001F7E8'
            else: 
                shareboard[i] = shareboard[i] + '\U00002B1B'

            if (globalnumbercolors[i]=='0f9f6e'):
                shareboard[i] = shareboard[i] + '\U0001F7E9'
            elif globalnumbercolors[i]=='faca17':
                shareboard[i] = shareboard[i] + '\U0001F7E8'
            else: 
                shareboard[i] = shareboard[i] + '\U00002B1B'  

        return render_template('my-form.html', 
            namecolor1 = globalnamecolors[1],
            namecolor2 = globalnamecolors[2],
            namecolor3 = globalnamecolors[3],
            namecolor4 = globalnamecolors[4],
            namecolor5 = globalnamecolors[5],   

            heightcolor1 = globalheightcolors[1],  
            heightcolor2 = globalheightcolors[2],  
            heightcolor3 = globalheightcolors[3],  
            heightcolor4 = globalheightcolors[4],  
            heightcolor5 = globalheightcolors[5],  
    
            sportcolor1 = globalsportcolors[1],  
            sportcolor2 = globalsportcolors[2],  
            sportcolor3 = globalsportcolors[3],  
            sportcolor4 = globalsportcolors[4],  
            sportcolor5 = globalsportcolors[5],  

            positioncolor1 = globalpositioncolors[1],  
            positioncolor2 = globalpositioncolors[2],  
            positioncolor3 = globalpositioncolors[3],  
            positioncolor4 = globalpositioncolors[4],  
            positioncolor5 = globalpositioncolors[5],  

            yearcolor1 = globalyearcolors[1],  
            yearcolor2 = globalyearcolors[2],  
            yearcolor3 = globalyearcolors[3],  
            yearcolor4 = globalyearcolors[4],  
            yearcolor5 = globalyearcolors[5],  

            numbercolor1 = globalnumbercolors[1],  
            numbercolor2 = globalnumbercolors[2],  
            numbercolor3 = globalnumbercolors[3],  
            numbercolor4 = globalnumbercolors[4],  
            numbercolor5 = globalnumbercolors[5],
            
            playernames=playernamessuggest,
            guessblankofblank=guesstext,
            
            row1=rows[0],
            row2=rows[1],
            row3=rows[2],
            row4=rows[3],
            row5=rows[4],

            name1=chosenplayers[0].name,
                    name2=chosenplayers[1].name,
                    name3=chosenplayers[2].name,
                    name4=chosenplayers[3].name,
                    name5=chosenplayers[4].name,

                    height1=chosenplayerdisplayheights[0],
                    height2=chosenplayerdisplayheights[1],
                    height3=chosenplayerdisplayheights[2],
                    height4=chosenplayerdisplayheights[3],
                    height5=chosenplayerdisplayheights[4],

                    sport1=chosenplayers[0].sport,
                    sport2=chosenplayers[1].sport,
                    sport3=chosenplayers[2].sport,
                    sport4=chosenplayers[3].sport,
                    sport5=chosenplayers[4].sport,

                    position1=chosenplayers[0].position,
                    position2=chosenplayers[1].position,
                    position3=chosenplayers[2].position,
                    position4=chosenplayers[3].position,
                    position5=chosenplayers[4].position,

                    year1=chosenplayers[0].year,
                    year2=chosenplayers[1].year,
                    year3=chosenplayers[2].year,
                    year4=chosenplayers[3].year,
                    year5=chosenplayers[4].year,

                    number1=chosenplayers[0].number,
                    number2=chosenplayers[1].number,
                    number3=chosenplayers[2].number,
                    number4=chosenplayers[3].number,
                    number5=chosenplayers[4].number,
                    won=won,
                    shareboard1=shareboard[1],
                    shareboard2=shareboard[2],
                    shareboard3=shareboard[3],
                    shareboard4=shareboard[4],
                    shareboard5=shareboard[5],

                    gameover=gameover,
                    lost=lost,
                    correctplayer=todaysname
            )


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   resp = make_response(render_template("my-form.html"))
   resp.set_cookie('somecookiename', 'I am cookie')
   return resp 
   
@app.route('/get-cookie/')
def get_cookie():
    username = request.cookies.get('somecookiename')
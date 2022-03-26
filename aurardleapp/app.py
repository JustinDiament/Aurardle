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

global row1
row1 = "rowvisible"

global row2
row2 = "rowinvisible"

global row3
row3 = "rowinvisible"

global row4
row4 = "rowinvisible"

global row5
row5 = "rowinvisible"

class player:
    def __init__(self, name, height, sport, position, year, number):
        self.name = name
        self.height = height
        self.sport = sport
        self.position = position
        self.year = year
        self.number = number

@app.route("/", methods=["POST", "GET"])
def home():
    playernames = [player("Jahmyl Telfort", 79, "mbb", "G", "So", 11),
        player("Jason Strong", 80, "mbb", "F", "Sr", 0),
        player("Vito Cubrilo", 76, "mbb", "G", "Jr", 1),
        player("Glen McClintock", 74, "mbb", "G", "So", 2),
        player("Tyreek Scott-Grayson", 77, "mbb", "G", "Sr", 10),
        player("Alex Nwagha", 80, "mbb", "F", "So", 12),
        player("Nikola Djogo", 80, "mbb", "G", "Sr", 13),
        player("Coleman Stucke", 79, "mbb", "F", "So", 15),
        player("Quirin Emanga", 77, "mbb", "G", "Jr", 22),
        player("Joe Pridgen", 77, "mbb", "G", "Jr", 23),
        player("Shaquille Walters", 78, "mbb", "G", "Sr", 24),
        player("Connor Braun", 81, "mbb", "F", "So", 32),
        player("Chris Doherty", 79, "mbb", "F", "Jr", 33),
        player("To Randriasalama", 75, "mbb", "G", "Fr", 55),

        player("Kendall Currence", 63, "wbb", "G", "Sr", 1),
        player("Izzy Larson", 73, "wbb", "F", "So", 2),
        player("Donna Ntambue", 69, "wbb", "G", "So", 3),
        player("Century McCartney", 71, "wbb", "G", "Jr", 5),
        player("Camille Clement", 68, "wbb", "G", "Fr", 12),
        player("Katie May", 71, "wbb", "G", "Sr", 13),
        player("Amryah Sapenter", 68, "wbb", "G", "So", 14),
        player("Anna Boruta", 70, "wbb", "G", "Jr", 15),
        player("Leyla Ozturk", 73, "wbb", "G", "So", 21),
        player("Maddie Vizza", 66, "wbb", "G", "So", 22),
        player("Gemima Motema", 69, "wbb", "G", "Fr", 23),
        player("Asha Parker", 74, "wbb", "G", "Fr", 24),
        player("Claudia Soriano", 67, "wbb", "G", "Fr", 25),
        player("Sammie Martin", 73, "wbb", "F", "Jr", 30),
        player("Emily Calabrese", 72, "wbb", "F", "Sr", 32),

        player("Alexa Matses", 68, "whky", "Gl", "Jr", 1),
        player("Lauren Macinnis", 68, "whky", "Def", "Sr", 2),
        player("Gillian Foote", 72, "whky", "Def", "Sr", 3),
        player("Molly Griffin", 64, "whky", "For", "So", 4),
        player("Miceala Sindoris", 65, "whky", "For", "Sr", 5),
        player("Katy Knoll", 67, "whky", "For", "Jr", 6),
        player("Brooke Tucker", 68, "whky", "Def", "Sr", 7),
        player("Andrea Renner", 64, "whky", "For", "Sr", 8),
        player("Emma Jurusik", 63, "whky", "For", "Sr", 9),
        player("Brooke Hobson", 66, "whky", "Def", "Sr", 10),
        player("Alina Mueller", 65, "whky", "For", "Sr", 11),
        player("Chloe Aurard", 66, "whky", "For", "Sr", 12),
        player("Katie Cipra", 65, "whky", "For", "Sr", 13),
        player("Mia Brown", 69, "whky", "For", "Sr", 15),
        player("Lily Yovetich", 64, "whky", "Def", "So", 16),
        player("Maddie Mills", 64, "whky", "For", "Sr", 17),
        player("Abbey Marohn", 67, "whky", "Def", "So", 19),
        player("Maureen Murphy", 64, "whky", "For", "Sr", 21),
        player("Skylar Fontaine", 64, "whky", "Def", "Sr", 22),
        player("Kate Holmes", 62, "whky", "For", "Jr", 24),
        player("Peyton Cullaton", 67, "whky", "For", "Jr", 26),
        player("Megan Carter", 68, "whky", "Def", "Jr", 27),
        player("Taylor Guarino", 65, "whky", "Def", "Fr", 28),
        player("Aerin Frankel", 65, "whky", "Gl", "Sr", 33),
        player("Paige Taborski", 67, "whky", "Gl", "Fr", 35),
        player("Gwyneth Philips", 67, "whky", "Gl", "Jr", 37),
        player("Tessa Ward", 69, "whky", "For", "Jr", 42),
        player("Tory Mariano", 69, "whky", "For", "Fr", 44),
        player("Skylar Irving", 68, "whky", "For", "Fr", 88),
        player("Peyton Anderson", 65, "whky", "For", "Jr", 91),

        player("Devon Levi", 72, "mhky", "Gl", "So", 1),
        player("Jordan Harris", 71, "mhky", "Def", "Sr", 2),
        player("Jayden Struble", 73, "mhky", "Def", "Jr", 3),
        player("Jeremie Bucheler", 76, "mhky", "Def", "Jr", 4),
        player("Matt Choupani", 71, "mhky", "For", "Fr", 5),
        player("Chase Mcinnis", 71, "mhky", "For", "Fr", 6),
        player("Michael Outzen", 72, "mhky", "For", "So", 7),
        player("Julian Kislin", 73, "mhky", "Def", "Sr", 8),
        player("Jakov Novak", 75, "mhky", "For", "Sr", 10),
        player("Gunnarwolfe Fontaine", 70, "mhky", "For", "So", 11),
        player("Tommy Miller", 74, "mhky", "Def", "Sr", 12),
        player("Ryan St. Louis", 70, "mhky", "For", "Fr", 13),
        player("Ty Jackson", 68, "mhky", "For", "So", 14),
        player("Dylan Jackson", 70, "mhky", "For", "So", 15),
        player("Sam Colangelo", 75, "mhky", "For", "So", 16),
        player("Marco Bozzo", 71, "mhky", "For", "Sr", 17),
        player("Tyler Spott", 71, "mhky", "Def", "Jr", 18),
        player("Riley Hughes", 74, "mhky", "For", "Jr", 19),
        player("Alex Mella", 72, "mhky", "For", "Jr", 20),
        player("Matt Demelis", 73, "mhky", "For", "Jr", 21),
        player("Cam Gaudette", 73, "mhky", "Def", "Fr", 23),
        player("Steven Agriogianis", 69, "mhky", "For", "So", 24),
        player("Aidan McDonough", 74, "mhky", "For", "Jr", 25),
        player("James Davenport", 71, "mhky", "Def", "So", 26),
        player("Jack Hughes", 72, "mhky", "For", "Fr", 27),
        player("Justin Hryckowian", 70, "mhky", "For", "Fr", 29),
        player("TJ Semptimphelter", 73, "mhky", "Gl", "Fr", 29),
        player("Evan Fear", 74, "mhky", "Gl", "Jr", 35),

        player("Danny Crossen", 72, "base", "UTL", "Jr", 1),
        player("Hayden Smith", 75, "base", "RHP", "Fr", 2),
        player("Max Viera", 70, "base", "INF", "Fr", 3),
        player("Dennis Colleran", 75, "base", "RHP", "Fr", 4),
        player("Jeff Costello", 71, "base", "OF", "Sr", 5),
        player("Cam Schlittler", 78, "base", "RHP", "So", 6),
        player("Kyle Hoog", 74, "base", "OF", "So", 7),
        player("Mike Sirota", 74, "base", "OF", "Fr", 8),
        player("Owen Langan", 72, "base", "RHP", "Jr", 9),
        player("Corey Diloreto", 76, "base", "INF", "Jr", 10),
        player("Eric Yost", 73, "base", "RHP", "So", 11),
        player("Sebastian Keane", 75, "base", "RHP", "So", 13),
        player("Thomas Balboni", 76, "base", "RHP", "So", 14),
        player("Matt Downing", 74, "base", "LHP", "So", 15),
        player("Mark Darakjy", 75, "base", "OF", "So", 16),
        player("Brett Dunham", 74, "base", "RHP", "Fr", 17),
        player("JP Olson", 73, "base", "C", "Fr", 18),
        player("Luke Beckstein", 67, "base", "INF", "So", 19),
        player("Jordy Allard", 69, "base", "RHP", "Sr", 20),
        player("Justin Bosland", 77, "base", "UTL", "Fr", 21),
        player("Spenser Smith", 74, "base", "INF", "Jr", 22),
        player("Ed Jarvis", 71, "base", "C", "So", 24),
        player("Buddy Mrowka", 71, "base", "INF", "Sr", 28),
        player("Michael Gemma", 77, "base", "RHP", "Sr", 31),
        player("James Quinlivan", 78, "base", "LHP", "So", 32),
        player("Teddy Beaudet", 71, "base", "Cat", "Sr", 33),
        player("Luke Masiuk", 73, "base", "OF", "Fr", 34),
        player("Jack Beauchesne", 74, "base", "RHP", "Fr", 35),
        player("Nick Davis", 77, "base", "RHP", "Jr", 36),
        player("Jake Gigliotti", 73, "base", "RHP", "So", 37),
        player("Sean Quinlivan", 73, "base", "RHP", "Fr", 39),
        player("Ryan Cervone", 70, "base", "OF", "So", 42),
        player("Jack Thorbahn", 75, "base", "INF", "So", 43),
        player("Will Jones", 77, "base", "LHP", "So", 45),
        player("Wyatt Scotti", 75, "base", "RHP", "So", 46),
        player("Matt Devlin", 75, "base", "LHP", "Sr", 47),
        player("Luke Bottger", 76, "base", "LHP", "So", 48),
        player("Gregory Bozzo", 72, "base", "Cat", "So", 49),

        player("Tyson Walker", 72, "mbb", "G", "Jr", 2)]


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

                    numbercolor1 = globalnumbercolors[1],  
                    numbercolor2 = globalnumbercolors[2],  
                    numbercolor3 = globalnumbercolors[3],  
                    numbercolor4 = globalnumbercolors[4],  
                    numbercolor5 = globalnumbercolors[5],
                    
                    playernames=playernamessuggest, 
                    guessblankofblank=guesstext,
                    
                    row1=row1,
                    row2=row2,
                    row3=row3,
                    row4=row4,
                    row5=row5
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

        gotname: 0
        gotheight: 0
        gotsport: 0
        gotposition: 0
        gotyear: 0
        gotnumber: 0

        for player1 in playernames:
            if player1.name == userplayername:
                userplayer = player1
                break

        if (userplayer.name.lower() == todaysname.lower()):
            globalnamecolors[globalguesses + 1] = "228C22"
        else:
            globalnamecolors[globalguesses + 1] = "ff0000"

        if (userplayer.height == todaysheight):
            globalheightcolors[globalguesses + 1] = "228C22" # green
        elif (abs (userplayer.height - todaysheight) <= 2):
            globalheightcolors[globalguesses + 1] = "FFFF00" # yellow
        else:
            globalheightcolors[globalguesses + 1] = "ff0000" # red

        if (userplayer.sport == todayssport):
            globalsportcolors[globalguesses + 1] = "228C22" # green
        elif ((userplayer.sport == "wbb" and todayssport == "mbb") or (userplayer.sport == "mbb" and todayssport == "wbb")):
            globalsportcolors[globalguesses + 1] = "FFFF00" # yellow
        elif ((userplayer.sport == "whky" and todayssport == "mhky") or (userplayer.sport == "mhky" and todayssport == "whky")):
            globalsportcolors[globalguesses + 1] = "FFFF00" # yellow
        else:
            globalsportcolors[globalguesses + 1] = "ff0000" # red
        
        if (userplayer.position == todaysposition):
            globalpositioncolors[globalguesses + 1] = "228C22" # green
        elif (todayssport == "base" and ((todaysposition == "INF" or todaysposition == "OF" or todaysposition == "UTL" or todaysposition == "C") and (userplayer.position == "INF" or userplayer.position == "OF" or userplayer.position == "UTL" or userplayer.position == "C"))):
            globalpositioncolors[globalguesses + 1] = "FFFF00" # yellow
        elif (todayssport == "base" and ((todaysposition == "LHP" or todaysposition == "RHP") and (userplayer.position == "LHP" or userplayer.position == "RHP"))):
            globalpositioncolors[globalguesses + 1] = "FFFF00" # yellow
        else:
            globalpositioncolors[globalguesses + 1] = "ff0000" # red

        if (userplayer.number == todaysnumber):
            globalnumbercolors[globalguesses + 1] = "228C22" # green
        elif (abs (userplayer.number - todaysnumber) <= 2):
            globalnumbercolors[globalguesses + 1] = "FFFF00" # yellow
        else:
            globalnumbercolors[globalguesses + 1] = "ff0000" # red

        if (userplayer.year == todaysyear):
            globalyearcolors[globalguesses + 1] = "228C22" # green
        else:
            globalyearcolors[globalguesses + 1] = "ff0000" # red


        globalguesses = globalguesses + 1

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

            numbercolor1 = globalnumbercolors[1],  
            numbercolor2 = globalnumbercolors[2],  
            numbercolor3 = globalnumbercolors[3],  
            numbercolor4 = globalnumbercolors[4],  
            numbercolor5 = globalnumbercolors[5],
            
            playernames=playernamessuggest,
            guessblankofblank=guesstext,
            
            row1=row1,
            row2=row2,
            row3=row3,
            row4=row4,
            row5=row5
            )


@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   resp = make_response(render_template("my-form.html"))
   resp.set_cookie('somecookiename', 'I am cookie')
   return resp 
   
@app.route('/get-cookie/')
def get_cookie():
    username = request.cookies.get('somecookiename')
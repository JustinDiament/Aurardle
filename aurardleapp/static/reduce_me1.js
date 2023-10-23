
function shuffle(array) {
let currentIndex = array.length,  randomIndex;

// While there remain elements to shuffle...
while (currentIndex != 0) {

// Pick a remaining element...
randomIndex = Math.floor(Math.random() * currentIndex);
currentIndex--;

// And swap it with the current element.
[array[currentIndex], array[randomIndex]] = [
array[randomIndex], array[currentIndex]];
}

return array;
}



   var availableTags = [
  "Masai Troutman",
  "Glen McClintock",
  "Chase Cormier",
  "Rashad King",
  "Harold Woods",
  "Jahmyl Telfort",
  "Alex Nwagha",
  "Jared Turner",
  "Coleman Stucke",
  "Joe Pridgen",
  "Chris Doherty",
  "Collin Metcalf",
  "To Randriasalama",

  "Jaelyn Batts",
  "Derin Erdogan",
  "Izzy Larsen",
  "Jamiya Braxton",
  "Oralye Kiefer",
  "Camille Clement",
  "Deja Bristol",
  "Amyrah Sapenter",
  "Anna Boruta",
  "Ariana Webb",
  "Maddie Vizza",
  "Gemima Motema",
  "Asha Parker",
  "Marian Turnbull",
  "Halle Idowu",

  "Alexa Matses",
  "Lily Shannon",
  "Tory Mariano",
  "Katy Knoll",
  "Molly Griffin",
  "Kristina Allard",
  "Holly Abela",
  "Alina Mueller",
  "Chloe Aurard",
  "Mia Brown",
  "Lily Yovetich",
  "Mia Langolis",
  "Abbey Marohn",
  "Maureen Murphy",
  "Peyton Cullaton",
  "Kate Holmes",
  "Megan Carter",
  "Taylor Guarino",
  "Paige Taborski",
  "Gwyneth Philips",
  "Jules Constantinople",
  "Taze Thompson",
  "Lily Brazis",
  "Maude Poulin-Labelle",
  "Skylar Irving",
  "Peyton Anderson",
  "Avery Anderson",
  "Alyssa Antonakis",

  "Devon Levi",
  "Jayden Struble",
  "Jeremie Bucheler",
  "Hunter McDonald",
  "Chase Mcinnis",
  "Michael Outzen",
  "Jackson Dorrington",
  "Matt Choupani",
  "Jakov Novak",
  "Gunnarwolfe Fontaine",
  "Cam Lund",
  "Liam Walsh",
  "Jack Williams",
  "Sam Colangelo",
  "Braden Doyle",
  "Tyler Spott",
  "Riley Hughes",
  "Alex Mella",
  "Matt DeMelis",
  "Vinny Borgesi",
  "Cam Gaudette",
  "Kyle Furey",
  "Aidan McDonough",
  "James Davenport",
  "Jack Hughes",
  "Justin Hryckowian",
  "Harrison Chesney",
  "Grant Riley",

  "Danny Crossen",
  "Hayden Smith",
  "Jack Thorbahn",
  "Dennis Colleran",
  "Sean McGee",
  "Aiven Cabral",
  "Cam Maldonado",
  "Mike Sirota",
  "Harrison Feinberg",
  "Alex Lane",
  "Eric Yost",
  "Joseph Hauser",
  "Matt Brinker",
  "Patrick Harrington",
  "Matt Downing",
  "Ryan Griffin",
  "Brett Dunham",
  "Griffin Young",
  "Luke Beckstein",
  "Jordy Allard",
  "Justin Bosland",
  "Spenser Smith",
  "Ed Jarvis",
  "Craig Ottaviano",
  "Jack Doyle",
  "Melo Musacchia",
  "Michael Gemma",
  "James Quinlivan",
  "Tyler MacGregor",
  "Luke Masiuk",
  "Jack Beauchesne",
  "Nick Davis",
  "Jake Gigliotti",
  "Sean Quinlivan",
  "Carson Walsh",
  "Jimmy Sullivan",
  "Will Jones",
  "Wyatt Scotti",
  "James Morice",
  "Gregory Bozzo",

  "Tyson Walker"];
shuffle(availableTags);


    $( "#enter_field_1" ).autocomplete({
source: availableTags,
select: function (event, ui) {
$(this).val(ui.item.value);
localStorage.setItem("guesscount", "0")
document.getElementById("getridofrowsometimes").classList.add('revealrow');
document.getElementById("getridofrowsometimes").classList.remove('getridofrow');
document.getElementById("enterdivsmall2").classList.remove('getridofrow');
// document.getElementById("sub").click();
var urlheight = 'http://127.0.0.1:5000/determine/height?playertyped='
var urlsport = 'http://127.0.0.1:5000/determine/sport?playertyped='
var urlposition = 'http://127.0.0.1:5000/determine/position?playertyped='
var urlyear = 'http://127.0.0.1:5000/determine/year?playertyped='
var urlnumber = 'http://127.0.0.1:5000/determine/number?playertyped='
var urlcheckwinner = 'http://127.0.0.1:5000/check/winner?playertyped='

var checkheight = 'http://127.0.0.1:5000/check/height?playertyped='
var checksport = 'http://127.0.0.1:5000/check/sport?playertyped='
var checkposition = 'http://127.0.0.1:5000/check/position?playertyped='
var checkyear = 'http://127.0.0.1:5000/check/year?playertyped='
var checknumber = 'http://127.0.0.1:5000/check/number?playertyped='



var playertyped = document.getElementById("enter_field_1").value;
var urlheightfull = urlheight + playertyped
var urlsportfull = urlsport + playertyped
var urlpositionfull = urlposition + playertyped
var urlyearfull = urlyear + playertyped
var urlnumberfull = urlnumber + playertyped
var checkwinnerfull = urlcheckwinner + playertyped

var checkheightfull = checkheight + playertyped
var checksportfull = checksport + playertyped
var checkpositionfull = checkposition + playertyped
var checkyearfull = checkyear + playertyped
var checknumberfull = checknumber + playertyped

localStorage.setItem("firstplayername", playertyped);
document.getElementById("nameone").innerHTML = localStorage.getItem("firstplayername");

playertyped = ''
document.getElementById("getridofrowsometimes").classList.add('revealrow');
document.getElementById("getridofrowsometimes").classList.remove('getridofrow');

localStorage.setItem("1nametosport", "stop")
localStorage.setItem("1sporttoposition", "stop")
localStorage.setItem("1positiontoyear", "stop")
localStorage.setItem("1yeartoheight", "stop")
localStorage.setItem("1heighttonumber", "stop")

let el = document.querySelector( ':focus' );
if( el ) el.blur();

$.getJSON(checkwinnerfull,

function(data) {
localStorage.setItem("wonthegame", data.result);
if(localStorage.getItem("wonthegame")==="winner") {
document.getElementById("nameone").classList.add('greensquare');
document.getElementById('winnerbox').click();
localStorage.setItem("namecolor", "green");
}
else {
}
localStorage.setItem("1nametosport", "go")
})

$.getJSON(urlsportfull,
function(data) {
localStorage.setItem("firstplayersport", data.result);
document.getElementById("sportone").innerHTML = data.result;

}
)

$.getJSON(checksportfull,
function(data) {
// while(localStorage.getItem("1nametosport")!="go") {
//    //bah
// }


localStorage.setItem("sport_check_1", data.result);
if (localStorage.getItem("sport_check_1")==="true") {
document.getElementById('sportone').classList.add("greensquare");
}
else if (localStorage.getItem("sport_check_1")==="middle") {
document.getElementById('sportone').classList.add("yellowsquare");
}
else {
document.getElementById('sportone').classList.add("greysquare");
}
localStorage.setItem("1sporttoposition", "go")

}
)

$.getJSON(urlpositionfull,
function(data) {
localStorage.setItem("firstplayerposition", data.result);
document.getElementById("positionone").innerHTML = data.result;
}
)

$.getJSON(checkpositionfull,
function(data) {
// while(localStorage.getItem("1sporttoposition")!="go") {
//    //bah
// }
localStorage.setItem("position_check_1", data.result);

if (localStorage.getItem("position_check_1")==="true") {
document.getElementById('positionone').classList.add("greensquare");
}
else if (localStorage.getItem("position_check_1")==="middle") {
document.getElementById('positionone').classList.add("yellowsquare");
}
else {
document.getElementById('positionone').classList.add("greysquare");
}
localStorage.setItem("1positiontoyear", "go")

}
)

$.getJSON(urlyearfull,
function(data) {
localStorage.setItem("firstplayeryear", data.result);
document.getElementById("yearone").innerHTML = data.result;
}
)

$.getJSON(checkyearfull,
function(data) {
// while(localStorage.getItem("1positiontoyear")!="go") {
//    //bah
// }

localStorage.setItem("year_check_1", data.result);
if (localStorage.getItem("year_check_1")==="true") {
document.getElementById('yearone').classList.add("greensquare");
}
else {
document.getElementById('yearone').classList.add("greysquare");
}
localStorage.setItem("1yeartoheight", "go")
}
)

$.getJSON(urlheightfull,
function(data) {
localStorage.setItem("firstplayerheight", data.result);
document.getElementById("heightone").innerHTML = data.result;

}
)

$.getJSON(checkheightfull,
function(data) {
// while(localStorage.getItem("1yeartoheight")!="go") {
//    //bah
// }

localStorage.setItem("height_check_1", data.result);
if (localStorage.getItem("height_check_1")==="true") {
document.getElementById('heightone').classList.add("greensquare");
}
else if (localStorage.getItem("height_check_1")==="middle") {
document.getElementById('heightone').classList.add("yellowsquare");
}
else {
document.getElementById('heightone').classList.add("greysquare");

}
localStorage.setItem("1heighttonumber", "go")
}
)

$.getJSON(urlnumberfull,
function(data) {

localStorage.setItem("firstplayernumber", data.result);
document.getElementById("numberone").innerHTML = data.result;

}
)

$.getJSON(checknumberfull,
function(data) {

localStorage.setItem("number_check_1", data.result);

if (localStorage.getItem("number_check_1")==="true") {
document.getElementById('numberone').classList.add("greensquare");

if(localStorage.getItem("wonthegame")==="winner") {
fixstatsonwin();
document.getElementById("enterdivsmall2").classList.add('getridofrow');
}
}
else if (localStorage.getItem("number_check_1")==="middle") {
document.getElementById('numberone').classList.add("yellowsquare");
}


else {
document.getElementById('numberone').classList.add("greysquare");
}
}
)

if (!localStorage.getItem("guesscount")) {
localStorage.setItem("guesscount", 1);
}
else {
localStorage.setItem("guesscount", (parseInt(localStorage.getItem("guesscount")) + 1));
}

$('#submitaplayer')[0].reset();



$('#enter_field_1').val('');
document.getElementById("submitaplayer").classList.add('getridofinput');

}
});

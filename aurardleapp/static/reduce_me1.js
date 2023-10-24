// URL of the site
var url_prefix = "http://127.0.0.1:5000/";

// Players text file
var players_txt = "all_players_2023_24.txt";

// Endpoints to get the values for the player's attributes
var urlheight = url_prefix + "determine/height?playertyped=";
var urlsport = url_prefix + "determine/sport?playertyped=";
var urlposition = url_prefix + "determine/position?playertyped=";
var urlyear = url_prefix + "determine/year?playertyped=";
var urlnumber = url_prefix + "determine/number?playertyped=";

// Endpoints to check for partial and full matches with the correct player
var urlcheckwinner = url_prefix + "check/winner?playertyped=";
var checkheight = url_prefix + "check/height?playertyped=";
var checksport = url_prefix + "check/sport?playertyped=";
var checkposition = url_prefix + "check/position?playertyped=";
var checkyear = url_prefix + "check/year?playertyped=";
var checknumber = url_prefix + "check/number?playertyped=";

// The current guess turn and next turn
var turn_number = "1";
var next_turn = "2";

// Shuffle the list of players into a random order
function shuffle(players) {
  // Start the index as the length of the players list
  let current_index = players.length;
  let random_index;

  // While there are still elements left to randomly order
  while (current_index != 0) {
    // Pick a one of them
    random_index = Math.floor(Math.random() * current_index);
    current_index--;

    // And swap it with the current element
    [players[current_index], players[random_index]] = [
      players[random_index],
      players[current_index],
    ];
  }

  // Return the shuffled players lsit
  return players;
}

// The shuffled list of players to offer autocomplete suggestions
let players_list_shuffled = [];

// Get the players from a text file
fetch("/static/" + players_txt)
  .then((response) => response.text())
  .then((data) => {
    players_list_shuffled = data.split("\n");

    // Shuffle the players
    shuffle(players_list_shuffled);

    // After setting up the autocomplete field
    $("#enter_field_" + turn_number).autocomplete({
      source: players_list_shuffled,

      // Once a player is selected
      select: function (event, ui) {
        $(this).val(ui.item.value);

        // Increase the guess count by 1
        localStorage.setItem(
          "guess_count",
          parseInt(localStorage.getItem("guess_count")) + 1
        );

        // Hide the input box, reveal the next one, and reveal the next row of the
        // clues table
        document
          .getElementById("hide_row_sometimes_" + turn_number)
          .classList.add("revealrow");
        document
          .getElementById("hide_row_sometimes_" + turn_number)
          .classList.remove("getridofrow");
        document
          .getElementById("enter_div_" + next_turn)
          .classList.remove("getridofrow");
        document
          .getElementById("submit_player_" + turn_number)
          .classList.add("getridofinput");

        // Get the player name the player chose
        var playertyped = document.getElementById(
          "enter_field_" + turn_number
        ).value;

        // Add the player name to the endpoints to get the values for
        // the player's attributes
        var urlheightfull = urlheight + playertyped;
        var urlsportfull = urlsport + playertyped;
        var urlpositionfull = urlposition + playertyped;
        var urlyearfull = urlyear + playertyped;
        var urlnumberfull = urlnumber + playertyped;
        var checkwinnerfull = urlcheckwinner + playertyped;

        // Add the player name to the endpoints to check for partial and
        // full matches with the correct player
        var checkheightfull = checkheight + playertyped;
        var checksportfull = checksport + playertyped;
        var checkpositionfull = checkposition + playertyped;
        var checkyearfull = checkyear + playertyped;
        var checknumberfull = checknumber + playertyped;

        //
        document.getElementById("player_name_" + turn_number).innerHTML = playertyped;

        $.getJSON(
          checkwinnerfull,

          function (data) {
            localStorage.setItem("game_over", data.result);
            if (localStorage.getItem("game_over") === "winner") {
              document.getElementById("player_name_" + turn_number).classList.add("greensquare");
              document.getElementById("winnerbox").click();
              localStorage.setItem("namecolor", "green");
            } else {
            }
          }
        );
        $.getJSON(urlsportfull, function (data) {
            alert(turn_number);
          document.getElementById("sport_" + turn_number).innerHTML = data.result;
        });

        $.getJSON(checksportfull, function (data) {
          if (data.result === "true") {
            document.getElementById("sport_" + turn_number).classList.add("greensquare");
          } else if (data.result === "middle") {
            document.getElementById("sport_" + turn_number).classList.add("yellowsquare");
          } else {
            document.getElementById("sport_" + turn_number).classList.add("greysquare");
          }
        });

        $.getJSON(urlpositionfull, function (data) {
          document.getElementById("position_" + turn_number).innerHTML = data.result;
        });

        $.getJSON(checkpositionfull, function (data) {
          if (data.result === "true") {
            document.getElementById("position_" + turn_number).classList.add("greensquare");
          } else if (data.result === "middle") {
            document
              .getElementById("position_" + turn_number)
              .classList.add("yellowsquare");
          } else {
            document.getElementById("position_" + turn_number).classList.add("greysquare");
          }
        });

        $.getJSON(urlyearfull, function (data) {
          document.getElementById("year_" + turn_number).innerHTML = data.result;
        });

        $.getJSON(checkyearfull, function (data) {
          if (data.result) {
            // == true
            document.getElementById("year_" + turn_number).classList.add("greensquare");
          } else {
            document.getElementById("year_" + turn_number).classList.add("greysquare");
          }
        });

        $.getJSON(urlheightfull, function (data) {
          document.getElementById("height_" + turn_number).innerHTML = data.result;
        });

        $.getJSON(checkheightfull, function (data) {
          if (data.result === "true") {
            document.getElementById("height_" + turn_number).classList.add("greensquare");
          } else if (data.result === "middle") {
            document.getElementById("height_" + turn_number).classList.add("yellowsquare");
          } else {
            document.getElementById("height_" + turn_number).classList.add("greysquare");
          }
        });

        $.getJSON(urlnumberfull, function (data) {
          document.getElementById("number_" + turn_number).innerHTML = data.result;
        });

        $.getJSON(checknumberfull, function (data) {
          if (data.result === "true") {
            document.getElementById("number_" + turn_number).classList.add("greensquare");

            if (localStorage.getItem("game_over") === "winner") {
              fix_stats_on_win();
              document
                .getElementById("enter_div_" + next_turn)
                .classList.add("getridofrow");
            }
          } else if (data.result === "middle") {
            document.getElementById("number_" + turn_number).classList.add("yellowsquare");
          } else {
            document.getElementById("number_" + turn_number).classList.add("greysquare");
          }
        //   .then(() => {
            turn_number++;
            next_turn++;;
        //   })
        });


      },
    });
  })


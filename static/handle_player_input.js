// Endpoints to get the values for the player's attributes
var urlheight = url_prefix + "determine/height?player_typed=";
var urlsport = url_prefix + "determine/sport?player_typed=";
var urlposition = url_prefix + "determine/position?player_typed=";
var urlyear = url_prefix + "determine/year?player_typed=";
var urlnumber = url_prefix + "determine/number?player_typed=";

// Endpoints to check for partial and full matches with the correct player
var urlcheckwinner = url_prefix + "check/winner?player_typed=";
var checkheight = url_prefix + "check/height?player_typed=";
var checksport = url_prefix + "check/sport?player_typed=";
var checkposition = url_prefix + "check/position?player_typed=";
var checkyear = url_prefix + "check/year?player_typed=";
var checknumber = url_prefix + "check/number?player_typed=";

// The current guess turn and next turn
var turn_number = "0";
var next_turn = "1";

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
function autocomplete_player_input() {
  turn_number++;
  next_turn++;

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

          // Hide the keyboard on mobile so the guess results table is visable
          let el = document.querySelector(":focus");
          if (el) el.blur();
          
          // Increase the guess count by 1
          localStorage.setItem(
            "guess_count",
            parseInt(localStorage.getItem("guess_count")) + 1
          );
          // Hide the input box, reveal the next one, and reveal the next row of the
          // clues table
          document
            .getElementById("hide_row_sometimes_" + turn_number)
            .classList.add("reveal_row");
          document
            .getElementById("hide_row_sometimes_" + turn_number)
            .classList.remove("hide_table_row");

          if (next_turn <= 6) {
            document
              .getElementById("enter_div_" + next_turn)
              .classList.remove("hide_table_row");
          }
          document
            .getElementById("submit_player_" + turn_number)
            .classList.add("hide_input");

          // Get the player name the player chose
          var player_typed = document.getElementById(
            "enter_field_" + turn_number
          ).value;

          // Add the player name to the endpoints to get the values for
          // the player's attributes
          var url_height_full = urlheight + player_typed;
          var url_sport_full = urlsport + player_typed;
          var url_position_full = urlposition + player_typed;
          var url_year_full = urlyear + player_typed;
          var url_number_full = urlnumber + player_typed;

          // Add the player name to the endpoints to check for partial and
          // full matches with the correct player
          var check_winner_full = urlcheckwinner + player_typed;
          var check_height_full = checkheight + player_typed;
          var check_sport_full = checksport + player_typed;
          var check_position_full = checkposition + player_typed;
          var check_year_full = checkyear + player_typed;
          var checknumberfull = checknumber + player_typed;

          // Set player name in this row of the table to be the selected player
          document.getElementById("player_name_" + turn_number).innerHTML =
            player_typed;

          // Array of promises to be executed in order
          promises = [];

          // Check if the player has won and make the player name box green if they have
          promises.push(
            $.getJSON(check_winner_full, function (data) {
              localStorage.setItem("game_over", data.result);
              if (localStorage.getItem("game_over") === "winner") {
                document
                  .getElementById("player_name_" + turn_number)
                  .classList.add("green_square");
                document.getElementById("winner_popup_box").click();
              } else {
              }
            })
          );

          // Set the sport in this row of the table to be the sport for the selected player
          promises.push(
            $.getJSON(url_sport_full, function (data) {
              document.getElementById("sport_" + turn_number).innerHTML =
                data.result;
            })
          );

          // Check if the player got the sport correct
          promises.push(
            $.getJSON(check_sport_full, function (data) {
              // If they have, make the sport box green
              if (data.result === "correct") {
                document
                  .getElementById("sport_" + turn_number)
                  .classList.add("green_square");
                localStorage.setItem("sport_check_" + turn_number, "correct");
                // If they got the sport right and the gender wrong, make it yellow
              } else if (data.result === "partially_correct") {
                document
                  .getElementById("sport_" + turn_number)
                  .classList.add("yellow_square");
                localStorage.setItem(
                  "sport_check_" + turn_number,
                  "partially_correct"
                );
                // Otherwise, make it grey
              } else {
                document
                  .getElementById("sport_" + turn_number)
                  .classList.add("grey_square");
                localStorage.setItem("sport_check_" + turn_number, "incorrect");
              }
            })
          );

          // Set the position in this row of the table to be the position for the selected player
          promises.push(
            $.getJSON(url_position_full, function (data) {
              document.getElementById("position_" + turn_number).innerHTML =
                data.result;
            })
          );

          // Check if the player got the position correct
          promises.push(
            $.getJSON(check_position_full, function (data) {
              // If they have, make the position box green
              if (data.result === "correct") {
                document
                  .getElementById("position_" + turn_number)
                  .classList.add("green_square");
                localStorage.setItem(
                  "position_check_" + turn_number,
                  "correct"
                );
                // If they got the position close in baseball, make it yellow
              } else if (data.result === "partially_correct") {
                document
                  .getElementById("position_" + turn_number)
                  .classList.add("yellow_square");
                localStorage.setItem(
                  "position_check_" + turn_number,
                  "partially_correct"
                );
                // Otherwise, make it grey
              } else {
                document
                  .getElementById("position_" + turn_number)
                  .classList.add("grey_square");
                localStorage.setItem(
                  "position_check_" + turn_number,
                  "incorrect"
                );
              }
            })
          );

          // Set the year in this row of the table to be the year for the selected player
          promises.push(
            $.getJSON(url_year_full, function (data) {
              document.getElementById("year_" + turn_number).innerHTML =
                data.result;
            })
          );

          // Check if the player got the year right
          promises.push(
            $.getJSON(check_year_full, function (data) {
              // If they have, make the year box green
              if (data.result) {
                document
                  .getElementById("year_" + turn_number)
                  .classList.add("green_square");
                localStorage.setItem("year_check_" + turn_number, "correct");
                // Otherwise, make it grey
              } else {
                document
                  .getElementById("year_" + turn_number)
                  .classList.add("grey_square");
                localStorage.setItem("year_check_" + turn_number, "incorrect");
              }
            })
          );

          // Set the height in this row of the table to be the height for the selected player
          promises.push(
            $.getJSON(url_height_full, function (data) {
              document.getElementById("height_" + turn_number).innerHTML =
                data.result;
            })
          );

          // Check if the player got the height correct
          promises.push(
            $.getJSON(check_height_full, function (data) {
              // If they have, make the height box green
              if (data.result === "correct") {
                document
                  .getElementById("height_" + turn_number)
                  .classList.add("green_square");
                localStorage.setItem("height_check_" + turn_number, "correct");
                // If they got the height within 2 inches, make it yellow
              } else if (data.result === "partially_correct") {
                document
                  .getElementById("height_" + turn_number)
                  .classList.add("yellow_square");
                localStorage.setItem(
                  "height_check_" + turn_number,
                  "partially_correct"
                );
                // Otherwise, make it grey
              } else {
                document
                  .getElementById("height_" + turn_number)
                  .classList.add("grey_square");
                localStorage.setItem(
                  "height_check_" + turn_number,
                  "incorrect"
                );
              }
            })
          );

          // Set the number in this row of the table to be the number for the selected player
          promises.push(
            $.getJSON(url_number_full, function (data) {
              document.getElementById("number_" + turn_number).innerHTML =
                data.result;
            })
          );

          // Check if the player got the number correct
          promises.push(
            $.getJSON(checknumberfull, function (data) {
              // If they have, make the number box green
              if (data.result === "correct") {
                document
                  .getElementById("number_" + turn_number)
                  .classList.add("green_square");
                localStorage.setItem("number_check_" + turn_number, "correct");
                // Also, check to see if the player has won and set uo the winner popup
                // and display it if they have
                if (localStorage.getItem("game_over") === "winner") {
                  fix_stats_on_win();
                  if (next_turn <= 6) {
                    document
                      .getElementById("enter_div_" + next_turn)
                      .classList.add("hide_table_row");
                  }
                }
                // If they got the number within 2, make it yellow
              } else if (data.result === "partially_correct") {
                document
                  .getElementById("number_" + turn_number)
                  .classList.add("yellow_square");
                localStorage.setItem(
                  "number_check_" + turn_number,
                  "partially_correct"
                );
                // Otherwise, make it grey
              } else {
                document
                  .getElementById("number_" + turn_number)
                  .classList.add("grey_square");
                localStorage.setItem(
                  "number_check_" + turn_number,
                  "incorrect"
                );
              }
            })
          );

          // Resolve the promises above in order
          Promise.all(promises).then(() => {
            // Afterwards, if it is the 6th and final turn of the game and
            // the player has not won, set up the loss popup and display it
            if (
              localStorage.getItem("guess_count") >= 6 &&
              localStorage.getItem("game_over") != "winner"
            ) {
              document.getElementById("loser_box").click();
              localStorage.setItem("game_over", "loser");
              fixstatsonloss();
              // If it is not the last turn, set up the the player input box for
              // the next guess
            } else {
              autocomplete_player_input();
            }
          });
        },
      });
    });
}

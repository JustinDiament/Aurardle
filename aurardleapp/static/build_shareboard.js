// Set emoji blocks for share copy paste text (aka the "shareboard")
var correct_guess = "🟩";
var partially_correct_guess = "🟨";
var incorrect_guess = "⬛";

// Overwritten daily by a cron job
var game_number = "125";

// Construct the shareboard based on the game results
function construct_shareboard() {
  // set up the hidden element to construct the shareboard in
  var shareboard = document.getElementById("shareboard-text-for-clipboard");
  shareboard.textContent = "";
  shareboard.textContent += "Aurardle #" + game_number + " - ";

  // If the player won, include the number of guesses it took
  if (localStorage.getItem("game_over") === "winner") {
    shareboard.textContent += localStorage.getItem("guess_count");
    // if they lost, put an X
  } else {
    shareboard.textContent += "X";
  }

  // Out of 6 allowed guess attempts
  shareboard.textContent += "/6\n";

  // Add the rows representing how well the user guessed each turn to the shareboard
  add_all_rows_to_shareboard(shareboard);

  // End the shareboard with the site link
  shareboard.textContent += "www.aurardle.com";
}

// Add the rows representing how well the user guessed each turn to the shareboard
function add_all_rows_to_shareboard(shareboard) {
  // add the turn 1 row to the shareboard
  add_row_to_shareboard(shareboard, "1");

  // if it took the player 2 or more turns, add the turn 2 row to the shareboard
  if (localStorage.getItem("guess_count") != "1") {
    add_row_to_shareboard(shareboard, "2");
  } else {
    return;
  }

  // if it took the player 3 or more turns, add the turn 3 row to the shareboard
  if (localStorage.getItem("guess_count") != "2") {
    add_row_to_shareboard(shareboard, "3");
  } else {
    return;
  }

  // if it took the player 4 or more turns, add the turn 4 row to the shareboard
  if (localStorage.getItem("guess_count") != "3") {
    add_row_to_shareboard(shareboard, "4");
  } else {
    return;
  }

  // if it took the player 5 or more turns, add the turn 5 row to the shareboard
  if (localStorage.getItem("guess_count") != "4") {
    add_row_to_shareboard(shareboard, "5");
  } else {
    return;
  }

  // if it took the player 6 or more turns, add the turn 6 row to the shareboard
  if (localStorage.getItem("guess_count") != "5") {
    add_row_to_shareboard(shareboard, "6");
  }
}


// Add one row representing how good the user's was to the shareboard
function add_row_to_shareboard(shareboard, number_of_guess) {
  // If the user got the answer this turn, add green. Else, add black
  if (localStorage.getItem("guess_count") === number_of_guess && localStorage.getItem("game_over") === "winner") {
    shareboard.textContent += correct_guess;
  } else {
    shareboard.textContent += incorrect_guess;
  }

  // If the user got the right sport and gender, add green. If right sport but wrong gender, add yellow.
  // Else, add black.
  if (localStorage.getItem("sport_check_" + number_of_guess) === "true") {
    shareboard.textContent += correct_guess;
  } else if (
    localStorage.getItem("sport_check_" + number_of_guess) === "middle"
  ) {
    shareboard.textContent += partially_correct_guess;
  } else {
    shareboard.textContent += incorrect_guess;
  }

  // If the user got the right position, add green. If close baseball position, add yellow.
  // Else, add black.
  if (localStorage.getItem("position_check_" + number_of_guess) === "true") {
    shareboard.textContent += correct_guess;
  } else if (
    localStorage.getItem("position_check_" + number_of_guess) === "middle"
  ) {
    shareboard.textContent += partially_correct_guess;
  } else {
    shareboard.textContent += incorrect_guess;
  }

  // If the user got the right year, add green. Else, add black.
  if (localStorage.getItem("year_check_" + number_of_guess) === "true") {
    shareboard.textContent += correct_guess;
  } else {
    shareboard.textContent += incorrect_guess;
  }

  // If the user got the right height, add green. If within 2 inches, add yellow.
  // Else, add black.
  if (localStorage.getItem("height_check_" + number_of_guess) === "true") {
    shareboard.textContent += correct_guess;
  } else if (
    localStorage.getItem("height_check_" + number_of_guess) === "middle"
  ) {
    shareboard.textContent += partially_correct_guess;
  } else {
    shareboard.textContent += incorrect_guess;
  }

  // If the user got the right number, add green. If within two, add yellow.
  // Else, add black.
  if (localStorage.getItem("number_check_" + number_of_guess) === "true") {
    shareboard.textContent += correct_guess + "\n";
  } else if (
    localStorage.getItem("number_check_" + number_of_guess) === "middle"
  ) {
    shareboard.textContent += partially_correct_guess + "\n";
  } else {
    shareboard.textContent += incorrect_guess + "\n";
  }
}

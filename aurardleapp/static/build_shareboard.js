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

  // if the player won, include the number of guesses it took
  if (localStorage.getItem("wonthegame") === "winner") {
    shareboard.textContent += localStorage.getItem("guesscount");
    // if they lost, put an X
  } else {
    shareboard.textContent += "X";
  }

  // out of 6 allowed guess attempts
  shareboard.textContent += "/6\n";


  add_row_to_shareboard(shareboard, "1");
  //
//   if (localStorage.getItem("guesscount") === "1") {
//     shareboard.textContent += "🟩";
//   } else {
//     shareboard.textContent += "⬛";
//   }
//   if (localStorage.getItem("sport_check_1") === "true") {
//     shareboard.textContent += "🟩";
//   } else if (localStorage.getItem("sport_check_1") === "middle") {
//     shareboard.textContent += "🟨";
//   } else {
//     shareboard.textContent += "⬛";
//   }
//   if (localStorage.getItem("position_check_1") === "true") {
//     shareboard.textContent += "🟩";
//   } else if (localStorage.getItem("position_check_1") === "middle") {
//     shareboard.textContent += "🟨";
//   } else {
//     shareboard.textContent += "⬛";
//   }
//   if (localStorage.getItem("year_check_1") === "true") {
//     shareboard.textContent += "🟩";
//   } else {
//     shareboard.textContent += "⬛";
//   }
//   if (localStorage.getItem("height_check_1") === "true") {
//     shareboard.textContent += "🟩";
//   } else if (localStorage.getItem("height_check_1") === "middle") {
//     shareboard.textContent += "🟨";
//   } else {
//     shareboard.textContent += "⬛";
//   }
//   if (localStorage.getItem("number_check_1") === "true") {
//     shareboard.textContent += "🟩\n";
//   } else if (localStorage.getItem("number_check_1") === "middle") {
//     shareboard.textContent += "🟨\n";
//   } else {
//     shareboard.textContent += "⬛\n";
//   }

  if (localStorage.getItem("guesscount") != "1") {
    add_row_to_shareboard(shareboard, "2");
    // if (localStorage.getItem("guesscount") === "2") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("sport_check_2") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("sport_check_2") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("position_check_2") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("position_check_2") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("year_check_2") === "true") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("height_check_2") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("height_check_2") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("number_check_2") === "true") {
    //   shareboard.textContent += "🟩\n";
    // } else if (localStorage.getItem("number_check_2") === "middle") {
    //   shareboard.textContent += "🟨\n";
    // } else {
    //   shareboard.textContent += "⬛\n";
    // }
  }

  if (
    localStorage.getItem("guesscount") != "2" &&
    localStorage.getItem("guesscount") != "1"
  ) {
    add_row_to_shareboard(shareboard, "3");
    // if (localStorage.getItem("guesscount") === "3") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("sport_check_3") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("sport_check_3") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("position_check_3") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("position_check_3") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("year_check_3") === "true") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("height_check_3") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("height_check_3") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("number_check_3") === "true") {
    //   shareboard.textContent += "🟩\n";
    // } else if (localStorage.getItem("number_check_3") === "middle") {
    //   shareboard.textContent += "🟨\n";
    // } else {
    //   shareboard.textContent += "⬛\n";
    // }
  }

  if (
    localStorage.getItem("guesscount") != "3" &&
    localStorage.getItem("guesscount") != "2" &&
    localStorage.getItem("guesscount") != "1"
  ) {
    add_row_to_shareboard(shareboard, "4");
    // if (localStorage.getItem("guesscount") === "4") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("sport_check_4") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("sport_check_4") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("position_check_4") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("fourthsitioncheck") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("year_check_4") === "true") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("height_check_4") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("height_check_4") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("number_check_4") === "true") {
    //   shareboard.textContent += "🟩\n";
    // } else if (localStorage.getItem("number_check_4") === "middle") {
    //   shareboard.textContent += "🟨\n";
    // } else {
    //   shareboard.textContent += "⬛\n";
    // }
  }

  if (
    localStorage.getItem("guesscount") != "4" &&
    localStorage.getItem("guesscount") != "3" &&
    localStorage.getItem("guesscount") != "2" &&
    localStorage.getItem("guesscount") != "1"
  ) {
    add_row_to_shareboard(shareboard, "5");
    // if (localStorage.getItem("guesscount") === "5") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("sport_check_5") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("sport_check_5") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("position_check_5") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("position_check_5") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("year_check_5") === "true") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("height_check_5") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("height_check_5") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("number_check_5") === "true") {
    //   shareboard.textContent += "🟩\n";
    // } else if (localStorage.getItem("number_check_5") === "middle") {
    //   shareboard.textContent += "🟨\n";
    // } else {
    //   shareboard.textContent += "⬛\n";
    // }
  }

  if (
    localStorage.getItem("guesscount") != "5" &&
    localStorage.getItem("guesscount") != "4" &&
    localStorage.getItem("guesscount") != "3" &&
    localStorage.getItem("guesscount") != "2" &&
    localStorage.getItem("guesscount") != "1"
  ) {
    add_row_to_shareboard(shareboard, "6")
    // if (localStorage.getItem("wonthegame") === "winner") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("sport_check_6") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("sport_check_6") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("position_check_6") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("position_check_6") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("year_check_6") === "true") {
    //   shareboard.textContent += "🟩";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("height_check_6") === "true") {
    //   shareboard.textContent += "🟩";
    // } else if (localStorage.getItem("height_check_6") === "middle") {
    //   shareboard.textContent += "🟨";
    // } else {
    //   shareboard.textContent += "⬛";
    // }
    // if (localStorage.getItem("number_check_6") === "true") {
    //   shareboard.textContent += "🟩\n";
    // } else if (localStorage.getItem("number_check_6") === "middle") {
    //   shareboard.textContent += "🟨\n";
    // } else {
    //   shareboard.textContent += "⬛\n";
    // }
  }

  shareboard.textContent += "www.aurardle.com";
}

function add_row_to_shareboard(shareboard, number_of_guess) {
  if (localStorage.getItem("guesscount") === number_of_guess) {
    shareboard.textContent += "🟩";
  } else {
    shareboard.textContent += "⬛";
  }

  if (localStorage.getItem("sport_check_" + number_of_guess) === "true") {
    shareboard.textContent += "🟩";
  } else if (localStorage.getItem("sport_check_" + number_of_guess) === "middle") {
    shareboard.textContent += "🟨";
  } else {
    shareboard.textContent += "⬛";
  }

  if (localStorage.getItem("position_check_" + number_of_guess) === "true") {
    shareboard.textContent += "🟩";
  } else if (
    localStorage.getItem("position_check_" + number_of_guess) === "middle"
  ) {
    shareboard.textContent += "🟨";
  } else {
    shareboard.textContent += "⬛";
  }

  if (localStorage.getItem("year_check_" + number_of_guess) === "true") {
    shareboard.textContent += "🟩";
  } else {
    shareboard.textContent += "⬛";
  }

  if (localStorage.getItem("height_check_" + number_of_guess) === "true") {
    shareboard.textContent += "🟩";
  } else if (localStorage.getItem("height_check_" + number_of_guess) === "middle") {
    shareboard.textContent += "🟨";
  } else {
    shareboard.textContent += "⬛";
  }

  if (localStorage.getItem("number_check_" + number_of_guess) === "true") {
    shareboard.textContent += "🟩\n";
  } else if (localStorage.getItem("number_check_" + number_of_guess) === "middle") {
    shareboard.textContent += "🟨\n";
  } else {
    shareboard.textContent += "⬛\n";
  }
}

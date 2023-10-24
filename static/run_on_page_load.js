// Set up local storage on page load
window.onload = function () {
  // Set the game over value to not_yet
  localStorage.setItem("game_over", "not_yet");

  // Set the guess count for this playthrough to 0
  localStorage.setItem("guess_count", "0");

  // If the player has no previous games played, initialize wins, current win streak, max win streak,
  // win percent, and losses to 0
  if (!localStorage.getItem("wins_storage")) {
    localStorage.setItem("wins_storage", "0");
  }

  if (!localStorage.getItem("wins_percent_storage")) {
    localStorage.setItem("wins_percent_storage", "0");
  }

  if (!localStorage.getItem("current_streak_storage")) {
    localStorage.setItem("current_streak_storage", "0");
  }

  if (!localStorage.getItem("max_streak_storage")) {
    localStorage.setItem("max_streak_storage", "0");
  }

  if (!localStorage.getItem("losses_storage")) {
    localStorage.setItem("losses_storage", "0");
  }

  // Use the local storage values to set the values in the statistics popup
  document.getElementById("wins").innerHTML =
    localStorage.getItem("wins_storage");
  document.getElementById("winpercent").innerHTML = localStorage.getItem(
    "wins_percent_storage"
  );
  document.getElementById("streak").innerHTML = localStorage.getItem(
    "current_streak_storage"
  );
  document.getElementById("maxstreak").innerHTML =
    localStorage.getItem("max_streak_storage");

  // Set up the player input box for the first guess
  autocomplete_player_input();
};

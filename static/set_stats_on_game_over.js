// Update player stats in local storage and in the statistics menu when the player wins a game
function fix_stats_on_win() {
  // Add one win to the total count
  localStorage.setItem(
    "wins_storage",
    String(Number(localStorage.getItem("wins_storage")) + 1)
  );

  // Increase the current win streak
  localStorage.setItem(
    "current_streak_storage",
    String(Number(localStorage.getItem("current_streak_storage")) + 1)
  );

  // If the new streak is longer than the old max streak, increase the max streak by one
  if (
    localStorage.getItem("max_streak_storage") <
    localStorage.getItem("current_streak_storage")
  ) {
    localStorage.setItem(
      "max_streak_storage",
      String(Number(localStorage.getItem("max_streak_storage")) + 1)
    );
  }

  // If the player has never lost, set win percent to 100% (to avoid divide by 0 error)
  if (localStorage.getItem("losses_storage") === "0") {
    localStorage.setItem("wins_percent_storage", "100");
    // otherwise, set win percentage to wins / total games completed
  } else {
    var answer = String(
      Math.floor(
        100 *
          (Number(localStorage.getItem("wins_storage")) /
            (Number(localStorage.getItem("wins_storage")) +
              Number(localStorage.getItem("losses_storage"))))
      )
    );
    localStorage.setItem("wins_percent_storage", answer);
  }

  // Use the new local storage values to update the displayed values in the statistics popup
  document.getElementById("wins").innerHTML =
    localStorage.getItem("wins_storage");
  document.getElementById("win_percent").innerHTML = localStorage.getItem(
    "wins_percent_storage"
  );
  document.getElementById("streak").innerHTML = localStorage.getItem(
    "current_streak_storage"
  );
  document.getElementById("maxstreak").innerHTML =
    localStorage.getItem("max_streak_storage");
}

// Update player stats in local storage and in the statistics menu when the player loses a game
function fixstatsonloss() {
  // Add one to the loss count
  localStorage.setItem(
    "losses_storage",
    String(Number(localStorage.getItem("losses_storage")) + 1)
  );

  // Revert the current win streak to 0
  localStorage.setItem("current_streak_storage", "0");

  // Set win percentage to wins / total games completed
  var answer = String(
    Math.floor(
      100 *
        (Number(localStorage.getItem("wins_storage")) /
          (Number(localStorage.getItem("wins_storage")) +
            Number(localStorage.getItem("losses_storage"))))
    )
  );
  localStorage.setItem("wins_percent_storage", answer);

  // Use the new local storage values to update the displayed values in the statistics popup
  document.getElementById("wins").innerHTML =
    localStorage.getItem("wins_storage");
  document.getElementById("win_percent").innerHTML = localStorage.getItem(
    "wins_percent_storage"
  );
  document.getElementById("streak").innerHTML = localStorage.getItem(
    "current_streak_storage"
  );
  document.getElementById("maxstreak").innerHTML =
    localStorage.getItem("max_streak_storage");
}

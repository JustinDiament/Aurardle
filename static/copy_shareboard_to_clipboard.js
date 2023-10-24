// Handles making the "Text copied to clipboard" mini popup appear inside the Stats popup
function mini_copied_popup_stats_in_stats_popup() {
  // Only make the mini popup appear if the game is over (and thus something is actually put
  // on the clipboard)
  if (
    localStorage.getItem("game_over") === "winner" ||
    localStorage.getItem("game_over") === "loser"
  ) {
    // make this popup appear
    var popup = document.getElementById(
      "mini_copied_popup_stats_in_stats_popup_text"
    );
    popup.classList.toggle("show");
  }
}

// Set up shareboard and write it to the clipboard when the user clicks the share button
function copy_shareboard_to_clipboard() {
  if (
    localStorage.getItem("game_over") === "winner" ||
    localStorage.getItem("game_over") === "loser"
  ) {
    // build the shareboard
    construct_shareboard();

    // write it to the clipboard
    navigator.clipboard.writeText(
      document.getElementById("shareboard-text-for-clipboard").innerText
    );
  }
}

// Assign the shareboard setup and write to clipboard function to all three share buttons
document.getElementById("share_button_in_stats_popup").onclick =
  copy_shareboard_to_clipboard;
document.getElementById("share_button_in_won_popup").onclick =
  copy_shareboard_to_clipboard;
document.getElementById("share_button_in_lost_popup").onclick =
  copy_shareboard_to_clipboard;

// Handles making the "Text copied to clipboard" mini popup appear inside the game loss popup
function mini_copied_popup_stats_in_game_loss_popup() {
  // make this popup appear
  var popup = document.getElementById(
    "mini_copied_popup_stats_in_game_loss_popup_text"
  );
  popup.classList.toggle("show");
}

// Handles making the "Text copied to clipboard" mini popup appear inside the game win popup
function mini_copied_popup_stats_in_game_win_popup() {
  // make this popup appear
  var popup = document.getElementById(
    "mini_copied_popup_stats_in_game_win_popup_text"
  );
  popup.classList.toggle("show");
}

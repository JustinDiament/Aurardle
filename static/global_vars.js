// URL of the site
var url_prefix = "https://www.aurardle.com/";

// Players text file
var players_txt = "/player_files/all_players_ordered_2023_24.txt";

// Daily correct player that must be guessed
// Overwritten daily by a cron job
var correct_player = "Alex Campbell"

// The index in the set player order of the current correct player
// Increased by 1 daily by a cron job
var game_number = "1";

// Set emoji blocks for share copy paste text (aka the "shareboard")
var correct_guess = "🟩";
var partially_correct_guess = "🟨";
var incorrect_guess = "⬛";

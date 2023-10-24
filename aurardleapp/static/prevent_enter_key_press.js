// Prevents the enter key from interacting with the text input boxes and 
// causing illegal name submissions. Only way to ssubmit a name is 
// by clicking one from the autocomplete suggest
document.onkeydown = function (e) {
  if (e.key === "Enter") {
    return false;
  }
};

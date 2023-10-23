

  // When the user clicks on <div>, open the popup
  function mini_copied_popup_stats_in_stats_popup() {
    if (localStorage.getItem("wonthegame")==="winner" || localStorage.getItem("lostthegame")==="loser") {
    var popup = document.getElementById("mini_copied_popup_stats_in_stats_popup_text");
    popup.classList.toggle("show");
    }
  }
 




    document.getElementById('share_button_in_stats_popup').onclick=function() {
      
        if (localStorage.getItem("wonthegame")==="winner" || localStorage.getItem("lostthegame")==="loser") {
            construct_shareboard();
        }

      navigator.clipboard.writeText(document.getElementById('shareboard-text-for-clipboard').innerText)
      .then(function(){
          console.log('text copied')
      })
    }




  // When the user clicks on <div>, open the popup
  function mini_copied_popup_stats_in_game_loss_popup() {
    var popup = document.getElementById("mini_copied_popup_stats_in_game_loss_popup_text");
    popup.classList.toggle("show");
  }



    document.getElementById('sharebutton2').onclick=function() {
      construct_shareboard();
    navigator.clipboard.writeText(document.getElementById('shareboard-text-for-clipboard').innerText)
    .then(function(){
        console.log('text copied')
    })
  }



  // When the user clicks on <div>, open the popup
  function mini_copied_popup_stats_in_game_win_popup() {
    var popup = document.getElementById("mini_copied_popup_stats_in_game_win_popup_text");
    popup.classList.toggle("show");
  }

  document.getElementById('sharebutton').onclick=function() {
      construct_shareboard();
    navigator.clipboard.writeText(document.getElementById('shareboard-text-for-clipboard').innerText)
    .then(function(){
        console.log('text copied')
    })
  }

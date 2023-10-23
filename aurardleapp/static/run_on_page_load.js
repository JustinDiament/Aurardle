window.onload = function() {
    localStorage.setItem("wonthegame", "false")
    localStorage.setItem("lostthegame", "false")
  
    if(!localStorage.getItem("winspersist")) {
      localStorage.setItem("winspersist", "0")
    }
  
    if(!localStorage.getItem("winpercentpersist")) {
      localStorage.setItem("winpercentpersist", "0")
    }
  
    if(!localStorage.getItem("streakpersist")) {
      localStorage.setItem("streakpersist", "0")
    }
  
    if(!localStorage.getItem("maxstreakpersist")) {
      localStorage.setItem("maxstreakpersist", "0")
    }
  
    if(!localStorage.getItem("lossespersist")) {
      localStorage.setItem("lossespersist", "0")
    }
  
    document.getElementById("wins").innerHTML = localStorage.getItem("winspersist");
    document.getElementById("winpercent").innerHTML = localStorage.getItem("winpercentpersist");
    document.getElementById("streak").innerHTML = localStorage.getItem("streakpersist");
    document.getElementById("maxstreak").innerHTML = localStorage.getItem("maxstreakpersist");
  
  }
  
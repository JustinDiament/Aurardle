

  function fixstatsonwin() {
    localStorage.setItem("winspersist", String(Number(localStorage.getItem("winspersist")) + 1));


    if (localStorage.getItem("maxstreakpersist")===localStorage.getItem("streakpersist")) {
      localStorage.setItem("maxstreakpersist", String(     Number(localStorage.getItem("maxstreakpersist")) + 1));
    }

    localStorage.setItem("streakpersist", String(   Number(localStorage.getItem("streakpersist")) + 1));


    if (localStorage.getItem("lossespersist")==="0") {
      localStorage.setItem("winpercentpersist", "100");
    }
    else {
      var answer = String(Math.floor(100 *((Number(localStorage.getItem("winspersist"))) / (Number(localStorage.getItem("winspersist")) + Number(localStorage.getItem("lossespersist"))))));
      localStorage.setItem("winpercentpersist", answer);
    }


  document.getElementById("wins").innerHTML = localStorage.getItem("winspersist");
  document.getElementById("winpercent").innerHTML = localStorage.getItem("winpercentpersist");
  document.getElementById("streak").innerHTML = localStorage.getItem("streakpersist");
  document.getElementById("maxstreak").innerHTML = localStorage.getItem("maxstreakpersist");
  }



  function fixstatsonloss() {


    localStorage.setItem("lossespersist", String(Number(localStorage.getItem("lossespersist")) + 1));

    localStorage.setItem("streakpersist", "0");


      var answer = String(Math.floor(100 *((Number(localStorage.getItem("winspersist"))) / (Number(localStorage.getItem("winspersist")) + Number(localStorage.getItem("lossespersist"))))));
      localStorage.setItem("winpercentpersist", answer);


  document.getElementById("wins").innerHTML = localStorage.getItem("winspersist");
  document.getElementById("winpercent").innerHTML = localStorage.getItem("winpercentpersist");
  document.getElementById("streak").innerHTML = localStorage.getItem("streakpersist");
  document.getElementById("maxstreak").innerHTML = localStorage.getItem("maxstreakpersist");
  }
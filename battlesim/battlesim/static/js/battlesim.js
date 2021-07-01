// battlesim.js
// author: colin seifer
// description: handles requests from DOM

// populate elements
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       // Typical action to be performed when the document is ready:
       // populate elements
       console.log(xhttp.response);
    }
};
xhttp.open("GET", 'backend/');
xhttp.send(null);

var fighters = 0;

function fighterSelect(fighter){
    // determine whether element was already selected.
    var style = window.getComputedStyle(document.getElementById(fighter));
    var color = style.backgroundColor;
    // beige.
    if(color == "rgb(245, 245, 220)"){
        fighters++;
        document.getElementById(fighter).style.backgroundColor = "aquamarine";
    }
    // aquamarine.
    else if(color == "rgb(127, 255, 212)"){
        fighters--;
        document.getElementById(fighter).style.backgroundColor = "beige";
    }

    // once 3 fighters are selected, redirect to battle screen.
    if(fighters >= 3){
        window.location.replace(window.location + "battle/");
    }
}
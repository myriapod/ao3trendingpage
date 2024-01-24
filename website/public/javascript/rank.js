var fandomObject = {
    "ATEEZ": "ATEEZ"}
    // list of fandom available to be looked into, currently just Ateez is working

$(document).onready(function(){
    
    
    const data = require('getrank.js')
    console.log(data)
    // Dropdown menu to select which fandom to look into
    var fandomSel = document.querySelector("fandom-choice");
    for (var x in fandomObject) {
        fandomSel.options[fandomSel.options.length] = new Option(x, x);
    };
    fandomSel.onchange = function() {
        // important var for future references //
        var fandomChosen = fandomObject[this.value];
        /////////////////////////////////////////
        document.querySelector("#fandom-chosen").innerHTML = fandomChosen;
    };


    this.document.querySelector("#timestamp").innerHTML = top10json[0]["timestmp"]

    // Show the top 10 
    document.querySelector("#ranking-body").innerHTML = data[0]
});


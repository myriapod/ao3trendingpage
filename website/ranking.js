var fandomObject = {
  "ATEEZ": "ATEEZ"}
  // list of fandom available to be looked into, currently just Ateez is working

window.onload = function() {
  // Dropdown menu to select which fandom to look into
  var fandomSel = document.getElementById("fandom-choice");
  for (var x in fandomObject) {
    fandomSel.options[fandomSel.options.length] = new Option(x, x);
  };
  fandomSel.onchange = function() {
    // important var for future references //
    var fandomChosen = fandomObject[this.value];
    /////////////////////////////////////////
    document.querySelector("#fandom-chosen").innerHTML = fandomChosen;
  };

  document.querySelectorAll("#show-button").forEach(elem => elem.addEventListener("click", () => {
    document.querySelector("#button-check").innerHTML = "<p>button clicked!</p>";
  }));
  
  /* document.querySelector("#button-check").innerHTML = showButtons.length;
  
  showButtons.forEach((item) => {
    item.addEventListener = function(){
      document.querySelector("#button-check").innerHTML = "<p>button clicked!</p>";

      item.siblings('.entry-info').slideToggle('slow');
    };
  })*/

    
  }

  // Query the top10.json file





//const mariadb = require('mariadb');
//const pool = mariadb.createPool({
//     host: 'mydb.com', 
//     user:'root', 
//     password: 'root',
//     connectionLimit: 5
//});
//async function asyncFunction() {
//  let conn;
//  try {
//	conn = await pool.getConnection();
//	const rows = await conn.query("SELECT 1 as val");
//	console.log(rows); //[ {val: 1}, meta: ... ]
//	const res = await conn.query("INSERT INTO myTable value (?, ?)", [1, "mariadb"]);
//	console.log(res); // { affectedRows: 1, insertId: 1, warningStatus: 0 }
//
//  } catch (err) {
//	throw err;
//  } finally {
//	if (conn) return conn.end();
//  }
//};
//
//function docWrite() {
//    document.getElementById("demo").innerHTML("We're in the ranking file")
//}



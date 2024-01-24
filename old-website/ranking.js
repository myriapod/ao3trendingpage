var fandomObject = {
  "ATEEZ": "ATEEZ"}
  // list of fandom available to be looked into, currently just Ateez is working

top10json = [{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 1,
  "worktitle": "Title of 1",
  "workauthor": "writer of 1",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "NEW"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 2,
  "worktitle": "Title of 2",
  "workauthor": "writer of 2",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "+2"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 1,
  "worktitle": "Title of 3",
  "workauthor": "writer of 3",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "-3"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 4,
  "worktitle": "Title of 4",
  "workauthor": "writer of 4",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "NEW"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 5,
  "worktitle": "Title of 5",
  "workauthor": "writer of 5",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "+2"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 6,
  "worktitle": "Title of 6",
  "workauthor": "writer of 6",
  "timestmp": "2024-01-17 15:21:46"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 7,
  "worktitle": "Title of 7",
  "workauthor": "writer of 7",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "-3"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 8,
  "worktitle": "Title of 8",
  "workauthor": "writer of 8",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "NEW"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 9,
  "worktitle": "Title of 9",
  "workauthor": "writer of 9",
  "timestmp": "2024-01-17 15:21:46",
  "keyword": "+2"
}, 
{
  "workid": 42109437,
  "fandom": "ATEEZ",
  "ranking": 10,
  "worktitle": "Title of 10",
  "workauthor": "writer of 10",
  "timestmp": "2024-01-17 15:21:46"
}]

window.addEventListener('load', function() {
  
  
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


  this.document.querySelector("#timestamp").innerHTML = top10json[0]["timestmp"]

  // Show the top 10 
  for (let i = 1; i <= 10; i ++) {
    var rank = `#rank-${i}`;
    let link = `<td><a href="https://archiveofourown.org/works/${top10json[i-1]["workid"]}">`

    document.querySelector(rank).innerHTML = `${link}${top10json[i-1]["ranking"]}</a></td>${link}${top10json[i-1]["worktitle"]}</a></td>${link}${top10json[i-1]["workauthor"]}</a></td>${link}${top10json[i-1]["keyword"]}</a></td>`  
  };
    
})



  /* document.querySelectorAll("#show-button").forEach(elem => elem.addEventListener("click", () => {
    document.querySelector("#button-check").innerHTML = "<p>button clicked!</p>";
  }));
  
  document.querySelector("#button-check").innerHTML = showButtons.length;
  
  showButtons.forEach((item) => {
    item.addEventListener = function(){
      document.querySelector("#button-check").innerHTML = "<p>button clicked!</p>";

      item.siblings('.entry-info').slideToggle('slow');
    };
  }) */



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



const http = require('node:http');
var fs = require('fs');

const hostname = '127.0.0.1';
const port = 3000;

fs.readFile('./index.html', function (err, html) {
    if (err) throw err;
    http.createServer((req, res) => {
        res.writeHead(200, {"Content-Type": "text/html"});
        res.write(html);
        res.end();
    }).listen(port, hostname, () => {
        console.log(`Server running at http://${hostname}:${port}/`);
    });
});
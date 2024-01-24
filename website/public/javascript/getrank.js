const fs = require('fs')
const top10json = JSON.parse(fs.readFileSync('views/top10test.json', 'utf-8', (err, data) => {
    if (err) {
    console.error(err);
    return;
    }
    return data
}));

function getRankData (){
    const data = [];
    for (let i = 1; i <= 10; i ++) {
        const link = `<td><a href="https://archiveofourown.org/works/${top10json[i-1]["workid"]}">`

        data.push(`${link}${top10json[i-1]["ranking"]}</a></td>${link}${top10json[i-1]["worktitle"]}</a></td>${link}${top10json[i-1]["workauthor"]}</a></td>${link}${top10json[i-1]["keyword"]}</a></td>`);
    return data
}};

console.log(getRankData()[0])

module.exports = getRankData()
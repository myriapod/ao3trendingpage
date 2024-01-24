var express = require('express');
var router = express.Router();
const getRankData = require('/home/myri/Documents/coding-projects/ao3trendingpage/website/public/javascript/getrank.js')

/* GET home page. */
router.get('/', function(req, res, next) {
  const data = getRankData;
  res.render('index', {data: data, page: ''});
});


module.exports = router;
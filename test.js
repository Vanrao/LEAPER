

var http = require('http');
var url=require('url');

//var express=require('express');
//var bodyParser = require('body-parser');
//app.use(express.bodyParser());
  //console.log(req.body);
//});
var fs=require('fs');
var server=http.createServer(function (req, res) {

    console.log('Request received');
    res.setHeader('Connection','close');
    res.writeHead(200, { 
        'Content-Type': 'text/plain',
        'Access-Control-Allow-Origin': '*' // implementation of CORS
    });
    var data='';
    req.on('data', function (chunk) {
        data+=chunk.toString();
    });
    
var url_parts = url.parse(req.url, true);
    var query = url_parts.query;
    //req.on('end', function() {
      //  console.log(query);                         
      //}); 
    //var str=JSON.stringify(req.body);
    //res.end('msg:ok'); // removed the 'callback' stuff
    //app.post('/', function(req, res) {
      //console.log(req.data);
      fs.appendFile('./input.txt',"\n"+JSON.stringify(query),function(err) {
   if (err) {
      return console.error(err);}});
      //req.connection.destroy();
    //server.close();



});
server.listen(8080,'localhost');
console.log('Server running at http://localhost');
var Blocks = require('/home/vanrao/scratch-vm/LEAPER-master/src/engine/blocks');
var http = require('http');
var url=require('url');
var fs=require('fs');
var prevcoor="";

var server=http.createServer(function (req, res){
    
    console.log('Request received');
    var url_parts = url.parse(req.url, true);
    var query = url_parts.query;
    //console.log(query); 
            //query is a json object
    //arr=query['jsonData[]'];
    //console.log(arr);
    var arr = Object.keys(query);
    //console.log(arr);
    //console.log(query[arr[0]]);
    //console.log(query[arr[0]][1]);qq
    for(var i=0;i<arr.length;i++) {
       fs.appendFile('./input.txt',String(query[arr[i]])+"\n",function(err) {
        if (err)
        {
          return console.error(err);
        }
      });
   
}
}).listen(8080, 'localhost');
console.log('Server running at http://localhost');


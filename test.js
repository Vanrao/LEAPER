
var Blocks = require('/home/vanrao/scratch-vm/LEAPER-master/src/engine/blocks');
var http = require('http');
var url=require('url');
var fs=require('fs');
var server=http.createServer(function (req, res){

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
    //console.log(query);             //query is a json object
    var arr=query['jsonData[]'];
    var timestamp=arr[0];             // string
    var blockData=arr[1];             //string

    //To retrieve the json data,first convert the string to JSON
    var jsonObj=JSON.parse(blockData);
    
    //Get all the block IDs   
    var blockIDs=Object.keys(jsonObj['_blocks']);
    //var val=jsonObj['_scripts'];
    
    //Calling blocks.js functions to retrieve all the properties of a block
    var blockObj = new Blocks();
    

    console.log(blockIDs);
    for (var i = 0; i < blockIDs.length; i++) {
      //To retrieve,first create the block with that received data
      blockObj.createBlock(jsonObj['_blocks'][blockIDs[i]]);
      
      //use all the functions defined in blocks.js
      console.log(blockObj.getBlock(blockIDs[i]));
      console.log(blockObj.getNextBlock(blockIDs[i]));
      console.log(blockObj.getBranch(blockIDs[i]));
      console.log(blockObj.getOpcode(blockIDs[i]));
      console.log(blockObj.getFields(blockIDs[i]));
      console.log(blockObj.getInputs(blockIDs[i]));

      // TODO : retrieve all these params and write it into a csv file

    };

    fs.appendFile('./input.txt',JSON.stringify(query)+"\n",function(err) {
    if (err)
    {
      return console.error(err);
    }
  });
}).listen(8080, 'localhost');
console.log('Server running at http://localhost');


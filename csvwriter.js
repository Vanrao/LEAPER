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
       

    
    
    var date = query[arr[i]][0];
   
    //To retrieve the json data,first convert the string to JSON
    var jsonObj=JSON.parse(query[arr[i]][1]);
    var jsonArr=[];

    //Get all the block IDs   
    var blockIDs=Object.keys(jsonObj['_blocks']);
    //var val=jsonObj['_scripts'];
    
    //Calling blocks.js functions to retrieve all the properties of a block
    var blockObj = new Blocks();
    

    
    var dataArray;
    //console.log(blockIDs);
    for (var i = 0; i < blockIDs.length; i++) {
      //To retrieve,first create the block with that received data
      blockObj.createBlock(jsonObj['_blocks'][blockIDs[i]]);
      
      //use all the functions defined in blocks.js
      var id=blockObj.getBlock(blockIDs[i])['id'];
      var opcode=blockObj.getBlock(blockIDs[i])['opcode'];
      var inputs=blockObj.getBlock(blockIDs[i])['inputs'];
      var fields=blockObj.getBlock(blockIDs[i])['fields'];
      var next=blockObj.getBlock(blockIDs[i])['next'];
      var toplevel=blockObj.getBlock(blockIDs[i])['toplevel'];
      var parent=blockObj.getBlock(blockIDs[i])['parent'];
      var shadow=blockObj.getBlock(blockIDs[i])['shadow'];
      var X=blockObj.getBlock(blockIDs[i])['x'];
      var Y=blockObj.getBlock(blockIDs[i])['y'];


      // TODO : retrieve all these params and write it into a csv file
      var onlyData=id+"    "+opcode+"    "+JSON.stringify(inputs)+"    "+JSON.stringify(fields)+"    "+next+"    "+toplevel+"    "+parent+"    "+shadow;
      var coordinates=X+"    "+Y;
      
      
        dataArray=date+"    "+onlyData+"    "+coordinates;

      fs.appendFileSync('./InteractionData.csv',dataArray+"\n");



    
}
}
}).listen(3000, 'localhost');
console.log('Server running at http://localhost');


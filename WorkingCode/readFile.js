var fs=require('fs');
fs.readFile('/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/DPSNorthWorkshop/Tanay.txt','utf8', function(err, contents) {
    if (err)
    {
      return console.error(err);
    }
   var contentsList = contents.split("\n");
   for(var line=0;line<contentsList.length;line++)
   {
     
      var array = contentsList[line].split(/,(.+)/);
      var Timestamp = array[0];
      var time = "Timestamp: " + Timestamp + "\n";
      var Data = array[1];
      try
      {
        var jsonObj=JSON.parse(Data);
        var blockIDs=Object.keys(jsonObj['_blocks']);
        var opcodesList = [];
      
      for(var i=0; i<blockIDs.length; i++) 
      {
        
         var opcode = []; 
        
        var innerkeys = Object.keys(jsonObj['_blocks'][blockIDs[i]]);
        for(var j=0; j<innerkeys.length; j++) 
        {
          if(innerkeys[j] == 'opcode') 
          {
            //console.log(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]);
            opcode.push(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]);
          }
          else if(innerkeys[j] == 'inputs')
          {
            opcode.push(JSON.stringify(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]));
          }
          else if(innerkeys[j] == 'fields')
          {
            opcode.push(JSON.stringify(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]));
          }
          else if(innerkeys[j] == 'id')
          {
            opcode.push(JSON.stringify(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]));
          }
          else if(innerkeys[j] == 'parent')
          {
            opcode.push(JSON.stringify(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]));
          }
          else if(innerkeys[j] == 'next')
          {
            opcode.push(JSON.stringify(jsonObj['_blocks'][blockIDs[i]][innerkeys[j]]));
          }
        
        }
        opcodesList.push(opcode);
        
      }
      
      fs.appendFile("/home/vanrao/scratch-vm/LEAPER-master/WorkingLeaper/DPSWorshopDataOpcodesFiles/Tanay.txt",time + JSON.stringify(opcodesList) + "\n");
      }
      catch(err)
      {
        console.log(err);
      }
    }
});

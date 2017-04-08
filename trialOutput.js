

var values = [];
var newDict = {}
var childIds = []
var currParent = 'NULL';
	var prevChild = '';
	var wholeList = [];
	var removeList = [];
	var jsonObj ;

	var ff = function createNestedBlocks(key) {
		//console.log(newDict[key].length);
		if(newDict[key] != undefined) {
				
				for(var h=0;h<newDict[key].length;h++) {
				wholeList.push((jsonObj['_blocks'][newDict[key][h]]['opcode']));
				removeList.push((jsonObj['_blocks'][newDict[key][h]]['opcode']));
				ff(newDict[key][h]);
				if(jsonObj['_blocks'][newDict[key][h]]['opcode'] == 'control_if'|| jsonObj['_blocks'][newDict[key][h]]['opcode'] == 'control_forever')
				wholeList.push(('end'));
			}
			//console.log('end');
		
		

			

		}
	}


var fs=require('fs');
fs.readFile('/home/vanrao/Downloads/inputVini.txt','utf8', function(err, contents) {
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
      // integrate above commented code properly according to the global variables.
	//var jsonData = '{"_blocks":{"?Q)vV7P?-D#^K6REvUC=":{"id":"?Q)vV7P?-D#^K6REvUC=","opcode":"event_whenbackdropswitchesto","inputs":{},"fields":{"BACKDROP":{"name":"BACKDROP","value":"level2"}},"next":"dLa75dj0ufMtr1xraKwI","shadow":false,"x":586,"y":198,"topLevel":true,"parent":null},"dLa75dj0ufMtr1xraKwI":{"id":"dLa75dj0ufMtr1xraKwI","opcode":"looks_hide","inputs":{},"fields":{},"next":"/u+7+sszMSJVb6m7?)4?","shadow":false,"parent":"?Q)vV7P?-D#^K6REvUC="},"/u+7+sszMSJVb6m7?)4?":{"id":"/u+7+sszMSJVb6m7?)4?","opcode":"motion_gotoxy","inputs":{"X":{"name":"X","block":"Y-N?q.IVy[pvrt2A5Q^Z","shadow":"Y-N?q.IVy[pvrt2A5Q^Z"},"Y":{"name":"Y","block":"}w(Y1Vn3tbG+[|+|yug(","shadow":"}w(Y1Vn3tbG+[|+|yug("}},"fields":{},"next":null,"shadow":false,"parent":"dLa75dj0ufMtr1xraKwI"},"Y-N?q.IVy[pvrt2A5Q^Z":{"id":"Y-N?q.IVy[pvrt2A5Q^Z","opcode":"math_number","inputs":{},"fields":{"NUM":{"name":"NUM","value":-195}},"next":null,"topLevel":false,"parent":"/u+7+sszMSJVb6m7?)4?","shadow":true},"}w(Y1Vn3tbG+[|+|yug(":{"id":"}w(Y1Vn3tbG+[|+|yug(","opcode":"math_number","inputs":{},"fields":{"NUM":{"name":"NUM","value":143}},"next":null,"topLevel":false,"parent":"/u+7+sszMSJVb6m7?)4?","shadow":true},"LJkTs)vSYO+.!n`-Me,s":{"id":"LJkTs)vSYO+.!n`-Me,s","opcode":"event_whenflagclicked","inputs":{},"fields":{},"next":"5UH.3=F]3v:,!y!CI}xZ","shadow":false,"x":124,"y":376,"topLevel":true,"parent":null},"5UH.3=F]3v:,!y!CI}xZ":{"id":"5UH.3=F]3v:,!y!CI}xZ","opcode":"motion_gotoxy","inputs":{"X":{"name":"X","block":"7q4w#v`}[+%=bRV8YwM8","shadow":"7q4w#v`}[+%=bRV8YwM8"},"Y":{"name":"Y","block":"xz@PG25jl8vXFViI.!?L","shadow":"xz@PG25jl8vXFViI.!?L"}},"fields":{},"next":"#vEt,7mMf~dv?vt}}cr|","shadow":false,"parent":"LJkTs)vSYO+.!n`-Me,s"},"7q4w#v`}[+%=bRV8YwM8":{"id":"7q4w#v`}[+%=bRV8YwM8","opcode":"math_number","inputs":{},"fields":{"NUM":{"name":"NUM","value":-195}},"next":null,"topLevel":false,"parent":"5UH.3=F]3v:,!y!CI}xZ","shadow":true},"xz@PG25jl8vXFViI.!?L":{"id":"xz@PG25jl8vXFViI.!?L","opcode":"math_number","inputs":{},"fields":{"NUM":{"name":"NUM","value":203}},"next":null,"topLevel":false,"parent":"5UH.3=F]3v:,!y!CI}xZ","shadow":true},"#vEt,7mMf~dv?vt}}cr|":{"id":"#vEt,7mMf~dv?vt}}cr|","opcode":"looks_show","inputs":{},"fields":{},"next":"0Y.wbxE:.D6G2A:`nXN5","shadow":false,"parent":"5UH.3=F]3v:,!y!CI}xZ"},"0Y.wbxE:.D6G2A:`nXN5":{"id":"0Y.wbxE:.D6G2A:`nXN5","opcode":"motion_pointindirection","inputs":{"DIRECTION":{"name":"DIRECTION","block":"FhH.rO9,i!whRhJl?EL:","shadow":"FhH.rO9,i!whRhJl?EL:"}},"fields":{},"next":"vCzeIhMomBj8{`KfOiMS","shadow":false,"parent":"#vEt,7mMf~dv?vt}}cr|"},"FhH.rO9,i!whRhJl?EL:":{"id":"FhH.rO9,i!whRhJl?EL:","opcode":"math_angle","inputs":{},"fields":{"NUM":{"name":"NUM","value":180}},"next":null,"topLevel":false,"parent":"0Y.wbxE:.D6G2A:`nXN5","shadow":true},"vCzeIhMomBj8{`KfOiMS":{"id":"vCzeIhMomBj8{`KfOiMS","opcode":"motion_movesteps","inputs":{"STEPS":{"name":"STEPS","block":"xq,5z9t4G24LqtrDn*?-","shadow":"xq,5z9t4G24LqtrDn*?-"}},"fields":{},"next":"Aw_?aJW.3U6e|y0`i}O`","shadow":false,"parent":"0Y.wbxE:.D6G2A:`nXN5"},"xq,5z9t4G24LqtrDn*?-":{"id":"xq,5z9t4G24LqtrDn*?-","opcode":"math_number","inputs":{},"fields":{"NUM":{"name":"NUM","value":10}},"next":null,"topLevel":false,"parent":"vCzeIhMomBj8{`KfOiMS","shadow":true},"Aw_?aJW.3U6e|y0`i}O`":{"id":"Aw_?aJW.3U6e|y0`i}O`","opcode":"control_forever","inputs":{"SUBSTACK":{"name":"SUBSTACK","block":"%j=iaSIUEif}mCl#`Fr(","shadow":null}},"fields":{},"next":null,"shadow":false,"parent":"vCzeIhMomBj8{`KfOiMS"},"%j=iaSIUEif}mCl#`Fr(":{"id":"%j=iaSIUEif}mCl#`Fr(","opcode":"control_if","inputs":{"CONDITION":{"name":"CONDITION","block":"yWvS66Wr2-O79;1HJh}p","shadow":null},"SUBSTACK":{"name":"SUBSTACK","block":"ueAHG~d#pY_J.f@U.49i","shadow":null}},"fields":{},"next":null,"shadow":false,"parent":"Aw_?aJW.3U6e|y0`i}O`"},"yWvS66Wr2-O79;1HJh}p":{"id":"yWvS66Wr2-O79;1HJh}p","opcode":"sensing_touchingobject","inputs":{"TOUCHINGOBJECTMENU":{"name":"TOUCHINGOBJECTMENU","block":"#o%8~m~1r*b-WvYU`1zR","shadow":"#o%8~m~1r*b-WvYU`1zR"}},"fields":{},"next":null,"shadow":false,"parent":"%j=iaSIUEif}mCl#`Fr("},"#o%8~m~1r*b-WvYU`1zR":{"id":"#o%8~m~1r*b-WvYU`1zR","opcode":"sensing_touchingobjectmenu","inputs":{},"fields":{"TOUCHINGOBJECTMENU":{"name":"TOUCHINGOBJECTMENU","value":"Stop"}},"next":null,"topLevel":false,"parent":"yWvS66Wr2-O79;1HJh}p","shadow":true},"ueAHG~d#pY_J.f@U.49i":{"id":"ueAHG~d#pY_J.f@U.49i","opcode":"looks_switchbackdropto","inputs":{"BACKDROP":{"name":"BACKDROP","block":"JtV^~-yku%fj,@T;ynX8","shadow":"JtV^~-yku%fj,@T;ynX8"}},"fields":{},"next":null,"shadow":false,"parent":"%j=iaSIUEif}mCl#`Fr("},"JtV^~-yku%fj,@T;ynX8":{"id":"JtV^~-yku%fj,@T;ynX8","opcode":"looks_backdrops","inputs":{},"fields":{"BACKDROP":{"name":"BACKDROP","value":"level2"}},"next":null,"topLevel":false,"parent":"ueAHG~d#pY_J.f@U.49i","shadow":true},"DzO*XgM?sE5R%;%MXRuE":{"id":"DzO*XgM?sE5R%;%MXRuE","opcode":"motion_pointindirection","inputs":{"DIRECTION":{"name":"DIRECTION","block":"1{v-YmaoNK.*J4~8?lH+","shadow":"1{v-YmaoNK.*J4~8?lH+"}},"fields":{},"next":null,"topLevel":true,"parent":null,"shadow":false,"x":"-321","y":"501"},"1{v-YmaoNK.*J4~8?lH+":{"id":"1{v-YmaoNK.*J4~8?lH+","opcode":"math_angle","inputs":{},"fields":{"NUM":{"name":"NUM","value":"90"}},"next":null,"topLevel":false,"parent":"DzO*XgM?sE5R%;%MXRuE","shadow":true}},"_scripts":["?Q)vV7P?-D#^K6REvUC=","LJkTs)vSYO+.!n`-Me,s","DzO*XgM?sE5R%;%MXRuE"]}'
	try {
	jsonObj = JSON.parse(Data);
	var blockIds = Object.keys(jsonObj["_blocks"]);
	var parentList = [];
	var newList = {};
	var key;
	for(var i=0;i<blockIds.length;i++) {
		var innerkeys = Object.keys(jsonObj['_blocks'][blockIds[i]]);
			
			var childList = [];
	        for(var j=0; j<innerkeys.length; j++) {
	        	/*if(innerkeys[j] == 'opcode') {
	        		console.log(jsonObj['_blocks'][blockIds[i]][innerkeys[j]]);
	        	}*/
	        	
	        	if(innerkeys[j] == 'id') {
	        		//console.log(jsonObj['_blocks'][blockIds[i]][innerkeys[j]]);
	        		//newList.push(jsonObj['_blocks'][blockIds[i]][innerkeys[j]]);
	        		key = jsonObj['_blocks'][blockIds[i]][innerkeys[j]];
	        		newList[key] = '';
	        			
	        		
	        	}
	        	else if(innerkeys[j] == 'parent') {
	        		//console.log(jsonObj['_blocks'][blockIds[i]][innerkeys[j]]);
	        		//newList.push(jsonObj['_blocks'][blockIds[i]][innerkeys[j]]);
	        		//console.log('\n');
	        		//parentList.push(newList);
	        		newList[key] = jsonObj['_blocks'][blockIds[i]][innerkeys[j]];
	        		
	        		
	        	}
	        } 
	}
	//console.log(newList);
	
	var keys = Object.keys(newList);
	for(var t=0;t<keys.length;t++) {
		values.push(newList[keys[t]]);
	}
	
	for(var w=0;w<values.length;w++) {
		childIds = [];
		for(var f=0;f<keys.length;f++) {
			if(values[w]!=null) {
				if(newList[keys[f]] == values[w]) {
				childIds.push(keys[f]);
				}
			newDict[values[w]] = childIds;
			}
			
		}
	}

	var parentKeys = Object.keys(newDict);
	


	


	//console.log(newDict);

	for(var p=0;p<parentKeys.length;p++) {
		
		if(p==0 && jsonObj['_blocks'][parentKeys[1]] != undefined ){
		currParent = jsonObj['_blocks'][parentKeys[1]]['opcode'];
		wholeList.push(jsonObj['_blocks'][parentKeys[p]]['opcode']);
		}

		else{
			//if(!newDict[parentKeys[p]].includes(jsonObj['_blocks'][parentKeys[p]]['opcode']) && jsonObj['_blocks'][parentKeys[p]]['opcode']!= 'control_forever' && 
			//	jsonObj['_blocks'][parentKeys[p]]['opcode']!= 'control_if' ) {
			if(jsonObj['_blocks'][parentKeys[p]]!= undefined){
			if(!removeList.includes(jsonObj['_blocks'][parentKeys[p]]['opcode']) && jsonObj['_blocks'][parentKeys[p]]['opcode']!= 'control_forever'){
				currParent = jsonObj['_blocks'][parentKeys[p]]['opcode'];
			if(currParent != prevChild) {
				wholeList.push(jsonObj['_blocks'][parentKeys[p]]['opcode']);
			}
				
			
			for(var d=0;d<newDict[parentKeys[p]].length;d++){
				wholeList.push(jsonObj['_blocks'][newDict[parentKeys[p]][d]]['opcode']);
			}
			prevChild = jsonObj['_blocks'][newDict[parentKeys[p]][newDict[parentKeys[p]].length-1]]['opcode'] 
			//console.log('\n');	
			}
			else if(jsonObj['_blocks'][parentKeys[p]]['opcode'] == 'control_forever') {
					//wholeList.push((jsonObj['_blocks'][parentKeys[p]]['opcode']));
				ff(parentKeys[p]);
				wholeList.push(('end'));
				
				
			}
		}

		}

			
		
		
	}


	console.log(wholeList);
	//console.log(removeList);
}
catch(err) {
	console.log('');
}
  }
});
	
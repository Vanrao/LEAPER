/*var fil=require("/home/vanrao/scratch-vm/playground/playground.js");
var jsonStrng=fil.writeFile();


var fs = require('fs');
fs.writeFile("./test.txt", jsonStrng, function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 


//Trying to write to a file using node.js
//trying to listen from the server-not working

*/
const http = require('http')  
const port = 4000

const requestHandler = (request, response) => {  
  console.log(request.url)
  response.end('Hello Node.js Server!')
}

const server = http.createServer(requestHandler)

server.listen(port, (err) => {  
  if (err) {
    return console.log('something bad happened', err)
  }

  console.log(`server is listening on ${port}`)
})


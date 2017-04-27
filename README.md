# LEAPER
# Learning Analytics For Block Based Programming
Scratch Logging engine-Scratch VM (version 3.0)
#How to run Scratch VM
>Install Node.js
>Cd into the project directory.
>Start the server by the command 'npm start' on the terminal
>Open another terminal in the same directory and execute 'node test.js' comand
>This is for logging the student's data

-> Server will start on 8073 port
>Open the browser and go to the url localhost/8073 to play with scratch.
>The log files will be saved as a .txt file in the project directory
--------------------------------------------------------------------------------------------
The following set of codes are executed in the same order on the log text files.

createData.py - Runs readFile.js on all the student data to get the opcode formatted lists

getTreeFormats.py - Gets all the tree format data form the opcodes to give it as input to the TreeEditdistance jar file

TreeScoresForAll.py - Creates CSVs for each student for Level-1 and level-2 separately.

Note: There are separate folders maintained for each type of data gathered. Paths need to be carefully changed if codes are executed locally on your systems.

Integrate the CSVs(results of TreeScoresForAll.py) into UI dashboards for each student.

ALL WORKING CODES ARE IN THE WorkingCode directory

------------------------------------------------------------------------------------------------

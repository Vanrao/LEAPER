import json
import os
import sys
import re
import ast
import time
from collections import OrderedDict

file_obj = open("/home/vinitha/Leaper/Data/output9-j-1843.txt","r");
file_obj1 = open("blocks_output.txt","w");
file_obj2 = open("treeOutput.txt","w");

content = {};
for line in file_obj.readlines():
	if(line == "\n"):
		pass
	elif(re.search("Timestamp:",line)):
		Timestamp = line.split(" ")[1];
		content[Timestamp] = [];
	else:
		content[Timestamp] = line;

content = OrderedDict(sorted(content.items()));



prevStr = "";
newStr = "";
start = 0;
count = 0;
motion_goto = 0;
motion_gotoxy = 0;

def orderBlocks(value,key):
	indexList = [];
	opcodesList = {};
	opcodesList[key] = [];
	for List in value:
		if(List[5] == "null"):
			indexList.append(List);
			opcode = [];
			opcode.append(List);
			nextOpcode = List[4];
			index = 0;
			while(index < len(value)):
				if(value[index][0] == nextOpcode):
					opcode.append(value[index]);
					indexList.append(value[index]);
					if(value[index][4] is "null"):
						break;
					else:
						nextOpcode = value[index][4];
						index = 0;
				else:
					index = index + 1;
			opcodesList[key].append(opcode);

	for index in indexList:
		#print(index);
		value.remove(index);
	
	def addIf(List,i,parentList):
		found = 0;
		for index in range(0,len(i)):
			if(index == 4 and i[index] == List[0]):
				if(parentList != None):
					parentList.append(List);
					return;
				else:
					i.append(List);
			elif(index == 0  and i[index] == List[5]):
				if(parentList != None):
					parentList.append(List);
					return;
				else:
					i.append(List);
			elif(isinstance(i[index] ,list)):
				addIf(List,i[index],i);
			

	for List in value:
		if(List[1] == "control_if"):
			
			for i in opcodesList[key]:
				addIf(List,i,None);
			
	for List in value:
		if("control_if" in List):
			value.remove(List);		
	

	def reOrderBlocks(parentOpcode,i,List):
		for index in range(0,len(i)):
			
			if(index == 0 and i[index] == parentOpcode):
				i.append(List);
				return;
			elif(isinstance(i[index],list)):
				reOrderBlocks(parentOpcode,i[index],List);

	for List in value:
		parentOpcode = List[5];
		for i in opcodesList[key]:
			reOrderBlocks(parentOpcode,i,List);

	return opcodesList;
			
def checkBlocks(List):
	global newStr;
	global motion_goto;
	global motion_gotoxy;
	if(len(List) == 6):
		if("event_whenflagclicked"in List):
			#print("when green flag clicked");
			#file_obj1.write("when green flag clicked\n");
			newStr = newStr + "when green flag clicked\n";
				
		if("looks_show"in List):
			#print("show");
			#file_obj1.write("show\n");
			newStr = newStr + "show\n";

		if("looks_hide"in List):
			#print("show");
			#file_obj1.write("show\n");
			newStr = newStr + "hide\n";

		if("event_whenbackdropswitchesto" in List):
			val = List[3];
			val = eval(val);
			value = val["BACKDROP"]["value"];
			newStr = newStr + "when backdrop switches to [" +  value + "]\n";

		if("math_number" in List):
			val = List[3];
			val = eval(val);
			value = val ["NUM"]["value"];
			newStr = newStr + "(" + str(value) + ") ";
			motion_gotoxy = motion_gotoxy + 1;

		if("math_angle" in List):
			val = List[3];
			val = eval(val);
			value = val ["NUM"]["value"];
			newStr = newStr + "(" + str(value) + ")";

		if("sensing_touchingobjectmenu" in List):
			val = List[3];
			val = eval(val);
			value = val["TOUCHINGOBJECTMENU"]["value"];
			newStr = newStr + value + "] > then";	 

		if("looks_backdrops" in List):
			val = List[3];
			val = eval(val);
			value = val["BACKDROP"]["value"];
			newStr = newStr + value + "]";

		if("sensing_keyoptions" in List):
			val = List[3];
			val = eval(val);
			value = val["KEY_OPTION"]["value"];
			newStr = newStr + value + "] pressed > then";

		if("colour_picker" in List):
			val = List[3];
			val = eval(val);
			value = val["COLOUR"]["value"];
			newStr = newStr + value + "] > then";

		if("sound_sounds_menu" in List):
			val = List[3];
			val = eval(val);
			value = val["SOUND_MENU"]["value"];
			newStr = newStr + value + "]";

		if ("control_forever" in List):
					newStr = newStr + "Forever\n"	

		if("control_if" in List):
					newStr = newStr + "If <> then";	


	else:
		for index in range(0,len(List)):
			if(index == 1):
				if("motion_gotoxy" in List):
					newStr = newStr + "go to " ;
					motion_goto = 1;
				elif("motion_pointindirection" in List):
					newStr = newStr + "point in direction ";
				elif("motion_movesteps" in List):
					newStr = newStr + "move steps ";	
				elif("control_forever" in List):
					newStr = newStr + "forever\n";
				elif("control_if" in List):
					newStr = newStr + "if <";
				elif("sensing_touchingobject" in List):
					newStr = newStr + "touching [";	
				elif("looks_switchbackdropto" in List):
					newStr = newStr + "switch backdrop to [";
				elif("sensing_keypressed" in List):
					newStr = newStr + "key [";
				elif("sensing_touchingcolor" in List):
					newStr = newStr + "touching [";
				elif("sound_play" in List):
					newStr = newStr + "play sound [";
				elif("motion_turnleft" in List):
					newStr = newStr + "turn left ";	
				elif("motion_turnright" in List):
					newStr = newStr + "turn right ";
				elif("motion_changexby" in List):
					newStr = newStr + "move X ";
			elif(isinstance(List[index],list)):
				checkBlocks(List[index]);
				if (index == len(List)-1 and List[1] == "control_if"):
					newStr = newStr + "end\n"
				else:
					if(motion_goto == 0):
						newStr = newStr + "\n"
					if(motion_goto == 1 and motion_gotoxy == 2):
						newStr = newStr + "\n"
						motion_gotoxy = 0
						motion_goto = 0
					if(motion_goto == 0 and motion_gotoxy > 0):
						motion_gotoxy = 0
						motion_goto = 0
				
for key,value in content.items():
	if(count == 0):
		startTime = key;
		count = 1;
		file_obj1.write(key);
		percentageTime = str((int(key)-int(startTime)) / 1000 ) + "th Second\n";
		file_obj1.write(percentageTime);
		lines = json.loads(value);
		orderedLines = orderBlocks(lines,key);
		for k,v in orderedLines.items():
			for val in v:
				for val1 in val:
					
					checkBlocks(val1);

				newStr = newStr + "end\n\n";
		file_obj1.write(newStr);
		prevStr = newStr;
		print(key);
		if(key == '1491453510213'):
			print(orderedLines);
		def treeIF(index1,opcode):
			noOfBraces = 0;
			for index in range(index1,len(opcode)):
				opcode[index] = opcode[index].replace(")","");
				opcode[index] = opcode[index].replace("(","");
				if(opcode[index] == ''):
					pass;
				elif(opcode[index] == "end"):
					for i in range(0,noOfBraces):
						file_obj2.write("}");
					return index;
				elif(index == len(opcode)-1):
					file_obj2.write("}");
					return len(opcode);
				else:
					file_obj2.write("{");
					file_obj2.write(opcode[index]);
					noOfBraces = noOfBraces + 1;

		Level_1 = 'when backdrop switches to [level2]\nhide\ngo to (-195) (143) \n';
		Level_2 = 'when backdrop switches to [level1]\nhide\n'
		#Level_3 = "when backdrop switches to [level3]";
		treeOpcodes = newStr.split("end\n\n");
		if(Level_1 in treeOpcodes):
			file_obj2.write("Level 1\n");
		elif(Level_2 in treeOpcodes):
			file_obj2.write("Level2\n");
		#file_obj2.write("Level 1\n");
		file_obj2.write(key);
		file_obj2.write("{root");
		for opcodes in treeOpcodes:
			opcode = opcodes.strip().split("\n");
			noOfBraces = 0;
			index = 0;
			while(index < len(opcode)):
				opcode[index] = opcode[index].replace(")","");
				opcode[index] = opcode[index].replace("(","");
				if(opcode[index] == ''):
					index = index + 1;
					pass;
				elif('if' in opcode[index]):
					index1 = treeIF(index,opcode);
					index = index1 + 1;
				else:
					file_obj2.write("{");
					file_obj2.write(opcode[index]);
					noOfBraces = noOfBraces + 1;
					index = index + 1;

			for j in range(0,noOfBraces):
				file_obj2.write("}");
		file_obj2.write("}\n\n");


		newStr = "";
		
	else:
		file_obj1.write(key);
		
		percentageTime = str((int(key)-int(startTime)) / 1000 ) + "th Second\n";
		file_obj1.write(percentageTime);
		lines = json.loads(value);
		orderedLines = orderBlocks(lines,key);
		for k,v in orderedLines.items():
			for val in v:
				for val1 in val:
					checkBlocks(val1);
				newStr = newStr + "end\n\n";
		if(newStr != prevStr):
			file_obj1.write(newStr);
			prevStr = newStr;
			#print(key);
		if(key == '1491453510213\n'):
			for k,v in orderedLines.items():
				print("=================================");
			for val in v:
				for val1 in val:
					print(val1);
			print("======================================");
		newStr = newStr + "end\n\n";

		#To print into treeOutput.txt
		def treeIF(index1,opcode):
			noOfBraces = 0;
			for index in range(index1,len(opcode)):
				opcode[index] = opcode[index].replace(")","");
				opcode[index] = opcode[index].replace("(","");
				if(opcode[index] == ''):
					pass;
				elif(opcode[index] == "end"):
					for i in range(0,noOfBraces):
						file_obj2.write("}");
					return index;
				elif(index == len(opcode)-1):
					file_obj2.write("}");
					return len(opcode);
				else:
					file_obj2.write("{");
					file_obj2.write(opcode[index]);
					noOfBraces = noOfBraces + 1;

		Level_1 = 'when backdrop switches to [level2]\nhide\ngo to (-195) (143) \n';
		Level_2 = 'when backdrop switches to [level1]\nhide\n'
		#Level_3 = "when backdrop switches to [level3]";
		
		treeOpcodes = newStr.split("end\n\n");
		if(Level_1 in treeOpcodes):
			file_obj2.write("Level 1\n");
		elif(Level_2 in treeOpcodes):
			file_obj2.write("Level2\n");
		file_obj2.write(key);
		file_obj2.write("{root");
		for opcodes in treeOpcodes:
			opcode = opcodes.strip().split("\n");
			noOfBraces = 0;
			index = 0;
			while(index < len(opcode)):
				opcode[index] = opcode[index].replace(")","");
				opcode[index] = opcode[index].replace("(","");
				if(opcode[index] == ''):
					index = index + 1;
					pass;
				elif('if' in opcode[index]):
					index1 = treeIF(index,opcode);
					index = index1 + 1;
				else:
					file_obj2.write("{");
					file_obj2.write(opcode[index]);
					noOfBraces = noOfBraces + 1;
					index = index + 1;

			for j in range(0,noOfBraces):
				file_obj2.write("}");
		file_obj2.write("}\n\n");

		newStr = "";
from automaton import *
"""
class TrafficLight(Automaton):

    go = Event("red", "green")
    slowdown = Event("green", "yellow")
    stop = Event("yellow", "red")
crossroads = TrafficLight(initial_state="red")
assert(crossroads.state == "red")
crossroads.go()
assert crossroads.state == "green"
print(stategraph(TrafficLight, fmt='plantuml'))
"""

#define the dfa
class Level1(Automaton):
	start1 = Event("flagClicked", "gotoXY")
	start2 = Event("gotoXY", "show")
	start3 = Event("show", "pointInDirection")
	start4 = Event("pointInDirection", "move")

#pass a list of input block opcodes as strings	
inputList=["flagClicked", "gotoXY", "show", "pointInDirection", "move"]

#set the initial state to any input
dist = 0
start = Level1(initial_state = "flagClicked")
s1 = start.start1
s2 = start.start2
s3 = start.start3
s4 = start.start4
opsList = [s1,s2,s3,s4]
for i,j in zip(range(1,len(inputList)),opsList):
	j()
	if(start.state == inputList[i]):
		dist+= 1
		print("Accepting...")
	else :
		print("Rejected")
		print(start.state+" and "+inputList[i]+" are not same")
print("Distance travelled to reach the final solution is "+str(dist))


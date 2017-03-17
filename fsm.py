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
class Level1(Automaton):
	start1 = Event("flagClicked", "gotoXY")
	start2 = Event("gotoXY", "show")
	start3 = Event("show", "pointInDirection")
	start4 = Event("pointInDirection", "move")


#pass a list of input block opcodes as strings
def validateInput(*inputList):
	start = Level1(initial_state = "flagClicked")
	try:
		start.start1()
		start.start2()
		start.start3()
		start.start4()
		assert start.state == "move"
		print("automaton accepted")
	except:
		print("Not accepted")

#Put this inside the automata-lib folder and run
from automata.fa.dfa import DFA

"""
A : whenGreenFlagClicked
B : goToXY
C : show
D : point in direction
E : move steps 
F : forever
G : if
H : touching step
I : switch backdrop to level2
"""
#level1
#Label each opcode with A,B etc.
dfa1 = DFA(
    states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7','q8','q9','q10','q11'},
    input_symbols={'A', 'B','C','D','E','F','G','H','I'},
    transitions={
        'q0': {'A': 'q0', 'B': 'q1','C':'q11','D':'q11','E':'q11','F':'q11','G':'q11','H':'q11','I':'q11'},
        'q1': {'C': 'q2', 'A':'q11','B':'q11','D':'q11','E':'q11','G':'q11','H':'q11','I':'q11','F':'q11'},
        'q2': {'D': 'q3' ,'C':'q11','A':'q11','E':'q11','F':'q11','G':'q11','H':'q11','I':'q11','B':'q11'},
        'q3': {'E':'q4','C':'q11','D':'q11','A':'q11','F':'q11','G':'q11','H':'q11','I':'q11','B':'q11'},
        'q4': {'D':'q5','F':'q11','C':'q11','B':'q11','E':'q4','A':'q11','G':'q11','H':'q11','I':'q11'},
        'q5': {'G':'q11','C':'q11','D':'q11','E':'q6','F':'q11','A':'q11','H':'q11','I':'q11','B':'q11'},
        'q6': {'H':'q11','C':'q11','D':'q11','E':'q6','F':'q7','G':'q11','A':'q11','I':'q11','B':'q11'},
        'q7': {'I':'q11','C':'q11','D':'q11','E':'q8','F':'q11','G':'q8','H':'q11','A':'q11','B':'q11'},
	'q8': {'I':'q11','C':'q11','D':'q11','E':'q11','F':'q11','G':'q11','H':'q9','A':'q11','B':'q11'},
	'q9': {'A': 'q11', 'B': 'q10','C':'q11','D':'q11','E':'q11','F':'q11','G':'q11','H':'q11','I':'q10'},
	'q10': {'A': 'q10', 'B': 'q10','C':'q10','D':'q10','E':'q10','F':'q10','G':'q10','H':'q10','I':'q10'},
	'q11': {'A': 'q11', 'B': 'q11','C':'q11','D':'q11','E':'q11','F':'q11','G':'q11','H':'q11','I':'q11'}
    },
    initial_state='q0',
    final_states={'q10','q11'}
)
stopped_state1 = dfa1.validate_input('ABCDEFGHI')
if(stopped_state1 != 'q8'):
	print("DFA accepted!")
else:
	print("DFA Rejected!")

	
"""
a - when backdrop switches to level2
b - show
c - goto xy
d - forever
1 - [up,down,left,right,stop]
0 - [if any of the above repeat]
"""
#level2
dfa2 = DFA(
    states={'q0', 'q1', 'q2','q3','q4','q5'},
    input_symbols={'a','b','c','d','0', '1'},
    transitions={
        'q0': {'a': 'q0', 'b': 'q1','c':'q5','d':'q5','0':'q5','1':'q5'},
        'q1': {'c': 'q2','a':'q5','b':'q5','0':'q5','1':'q5','d':'q5' },
        'q2': {'d': 'q3', 'c':'q5','a':'q5','0':'q5','1':'q5','b':'q5'},
	'q3': {'1':'q4','0':'q5','a':'q5','b':'q5','c':'q5','d':'q5'},
	'q4': {'1':'q4','0':'q5','a':'q5','b':'q5','c':'q5','d':'q5'},
	'q5': {'1':'q5','0':'q5','a':'q5','b':'q5','c':'q5','d':'q5'}
    },
    initial_state='q0',
    final_states={'q4','q5'}
)
#gives the state at which the dfa stops. With this calculate the distance metric
stopped_state2 = dfa2.validate_input('abcd0') #rejected, with abcd1 gets accepted
if(stopped_state2 != 'q5'):
	print("DFA accepted!")
else:
	print("DFA Rejected!")







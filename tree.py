from zss import simple_distance, Node
#only forever,repeat,if then, if then else,repeat until-- are nestable blocks. Hence they have children.rest will not
#whenever we encounter these blocks, start adding child nodes.

fileName = ''
fName = open(fileName,'r')

control_blocks = ['forever', 'if-then', 'if-then-else', 'repeat', 'repeat-until']
for opcode in fName:
	if opcode in control_blocks:
		Node(prevNode).addkid(currentNode)
A = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("h"))
            .addkid(Node("c")
                .addkid(Node("l"))))
        .addkid(Node("e"))
    )
B = (
    Node("f")
        .addkid(Node("a")
            .addkid(Node("d"))
            .addkid(Node("c")
                .addkid(Node("b"))))
        .addkid(Node("e"))
    )
print simple_distance(A, B) 

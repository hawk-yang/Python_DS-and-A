class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

#Unordered list class that kind of concatenates all the nodes together
class UnorderedList:
    #Head is initialized here
    def __init__(self):
        self.head = None

    #Is the head empty?
    def isEmpty(self):
        return self.head == None

    
    def addNode(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        print("Addition successful.")

    def countNodes(self):
        print("WOAH")
        cursor = self.head
        count = 0

        while cursor != None:
            count += 1
            cursor = cursor.getNext()
        
        return count

        
node1 = Node (1)
node2 = Node (2)
node3 = Node (3)

testList = UnorderedList()

testList.addNode(node1)
testList.addNode(node2)
testList.addNode(node3)

print(testList.countNodes())










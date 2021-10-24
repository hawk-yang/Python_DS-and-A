thingy = __import__("4_12".Queue)


testQueue = thingy()

testQueue.enqueue("hola")
testQueue.enqueue("yay!")
testQueue.enqueue("21")

print(testQueue.items)
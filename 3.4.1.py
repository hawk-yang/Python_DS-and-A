#This uses the checking off method which is fairly intuitive and is probably a decent solution
def anagramSolutionOne(s1, s2):
    stillOK = True
    if(len(s1) != len(s2)):
        stillOK= False

    l1 = list(s1)
    l2 = list(s2)

    if(stillOK):
        for i in range(len(l1)):
            for j in range (len(l1)):
                if(l2[j] == l1[i]):
                    l2[j] = None
                    break


    noneCount = l2.count(None)

    if(noneCount != len(l2)):
        print("NANI?")
        stillOK = False

    print("Is this an anagram?", stillOK)
    print(l2)

string1 = "hello"
string2 = "ollah"
anagramSolutionOne(string1, string2)





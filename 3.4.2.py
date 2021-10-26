#Sort and compare
def anagramSolutionTwo(s1,s2):
    anagram = True

    l1 = list(s1)
    l2 = list(s2)

    if( len(l1) != (len(l2))):
        anagram = False
        return anagram

    l1.sort()
    l2.sort()

    print(l1)
    print(l2)

    for i in range (len(l1)):
        if(l1[i] != l2[i]):
            anagram = False
            break
        
    return anagram


string1 = "hello"
string2 = "lloeh"
print(anagramSolutionTwo(string1, string2))
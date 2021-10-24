#This is the count and compare approach

def anagramSolutionFour(s1, s2):
    letters1 = [0]*26
    letters2 = [0]*26
    isOkay = True

    if(len(s1) != len(s2)):
        isOkay = False
        return isOkay

    for i in range(len(s1)):
        letters1[ord(s1[i]) - ord("a")] += 1
    print(letters1)

    for i in range(len(s2)):
        letters2[ord(s2[i]) - ord("a")] += 1
    print(letters2)

    for i in range(len(s1)):
        if (letters1[i] != letters2[i]):
            isOkay = False
            return isOkay

    return isOkay




string1 = "hello"
string2 = "olleh"
print(anagramSolutionFour(string1, string2))
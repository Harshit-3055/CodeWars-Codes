"""

WAP in Python to print all the words of a sentence


"""


word = ""
sen = input("Enter a sentence = ")
sen = sen + " "

for i in range(len(sen)):
    if(sen[i]==" "):
        for j in range(len(word)):
            if(int(word[j])==i):
                print()
        
        word=""
    else:
        word = word + sen[i]

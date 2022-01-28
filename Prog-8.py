"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""


"""
NewString = ""
word = ""
c=0
space  = int(0)
sen = str(input("Enter the sentence = "))
sen = sen + " "
for i in sen:
    if(i==' '):
        space = space + 1
NoOfWords = int(space + 1)

for i in range(1,NoOfWords):
    l = len(sen)
    for j in range(l):
        if(sen[j]!=" "):
            word = word + sen[j]
        else:
            print(word)
            for k in range(len(word)):
                #print("Word[k] = ", word[k], " i = ",i)
                if(word[k]=="1" or word[k]=="2" or word[k]=="3" or word[k]=="4" or word[k]=="5" or word[k]=="6" or word[k]=="7" or word[k]=="8" or word[k]=="9"):
                   if(int(word[k])==i):
                      NewString = NewString + " " + word
                      sen = sen.replace(word+" ","")
                      word = ""
                      break
                   else:
                        c=c+1
            if(len(word)==c):
                word=""
            
            break
#print(NewString)
#print(i)
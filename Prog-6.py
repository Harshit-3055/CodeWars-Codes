"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

"""
count = 0
sen = input("Enter a sentence in lowercase = ")
for a in sen:
    if(a == "a"):
        count = count + 1
    elif(a=="e"):
        count = count + 1
    elif(a=="i"):
        count = count + 1
    elif(a=="o"):
        count = count + 1
    elif(a=="u"):
        count = count + 1

print("The total number of vovels in this sentence = ",count)
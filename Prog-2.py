"""
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing second character 
of the final pair with an underscore ('_').

Examples:

StringSplit.solution("abc") // should return {"ab", "c_"}
StringSplit.solution("abcdef") // should return {"ab", "cd", "ef"}


"""

input_string = input("Enetr a string = ")
lenght = int(len(input_string))
if(lenght%2 == 0):
    for i in range(lenght*2):
        remove = input_string[:2]
        print(remove)
        input_string = input_string.replace(remove,"")
else:
    input_string = input_string + "_"
    for i in range(lenght*2):
        remove = input_string[:2]
        print(remove)
        input_string = input_string.replace(remove,"")
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""
num2 = 0
num = int(input("Enter the number [row no.] = "))
num1 = (((num-1)/2)*(2+(num-2)))
num1 = (num1*2)+1
#num1 = num1 - 1
#num1 = num1+2
for i in range(num):
   num2 = num2 + num1
   num1 = num1+2
print("Your answer is = ",num2)

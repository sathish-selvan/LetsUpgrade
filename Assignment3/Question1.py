# Question 1
# Write a Python program to add two numbers using class and object.
# (Take both numbers as input from the user)

#Answer:::

class Test():
    def sum(self,a,b):
        return a+b


a = int(input("Enter the first number "))
b = int(input("Enter the second number "))

s = Test()
ans = s.sum(a,b)
print(ans)

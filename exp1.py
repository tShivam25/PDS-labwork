#float to int
num=3.85
b=int(num)
print(b)
print(type(b))


# int to float
a=9
b=float(a)
print(b)
print(type(b))

#number to string
num=100
a=str(num)
print(a)
print(type(a))

#question
age=int(input("how old are you ?"))
#print("in 5 years ,your age will be ",age + 5) #pops error cause we are adding  a int to str
#correct way
print("in 5 years your age will be ",int(age)+5)
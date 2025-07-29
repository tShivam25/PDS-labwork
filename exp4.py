
# numerical ops randomized 


import random 

list = [ 'mustang ' , 'charger ' , 'supra mk4' , 'rx7' ,'gt63','aston martin dbs', 'rr spectre']
list1 = ['ashish', 'aksh', 'dikesh' , 'manoj','kamlesh' , 'shivam' , 'shreyansh']
print(random.choice(list) , random.choice(list1))



# random no. fuction 

num = random.random()
print(num)


# function 
def spoon(list1):
    for i in range(7):
        print("Spoon ",i+1, "is" ,random.choice(list1))

spoon(list1)

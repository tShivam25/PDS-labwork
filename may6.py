#decision making 
a = int(input ("enter a "))
b= int(input("enter b "))

if(b%a!=0):
    #loop statement 
    for i in range(1,10):
        a=a*2
        b=b*2
        
       
if(a%b!=0):
    while(a!=b):
        if(a>b):
            a=a-1
            b=b+1
        else :
            print("never be same ")
        
else:
    print("valid numbers only");  
    
          
print(a)
print(b)        
        
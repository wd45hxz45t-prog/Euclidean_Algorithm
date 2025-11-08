


#Eculidean Algorithm task 3 :
    
#get use of encapsulation by using classes:
#this class implements the Eulidean algorithm to find the GCD of two numbers :
    
class EuclideanAlgorithm : 
    
    def __init__ (self , a , b ):  
        #initialize the object(our numbers) with two numbers (a , b)
        self.a = a
        self.b = b
        
        
        
        
    def GCD (self):
    #change the value of (a,b) to local variables so we can use them un the finction :
        a , b = self.a , self.b 
        
        #loop until the remainder (b) = 0 
        while b!= 0 :
            
            #swap values : a become b , and b become the remainder :
            a , b = b , a % b 
            
            #when b =0 , a is the GCD :
        return a 
        
 #main "refactored" program \ task 3:
     
     
    # In this case , I used (try & except) to handle valid user input 
    #This makes the program more flexible : so if the user entered non_numeric value (e.g. letters),
    #the program will not  crash , but instead display a clear error message and continue running safely 
try :
    a = abs(int(input("Enter the first number : ")))
    b = abs(int(input("Enter the second number : ")))
    
    
    if a == 0 and b ==0 :
        print("Error , both  numbers cannot equal zero")
        
    else: 
        algorithm = EuclideanAlgorithm(a, b)
        print (f"The GCD is :  {algorithm.GCD()}")
     
        
     
        
# dealing with invalid numbers (inputs like letters , symbols )
except ValueError : 
    print("ERROR: please enter valid numbers only ! ")
     
     
     
     
     
     


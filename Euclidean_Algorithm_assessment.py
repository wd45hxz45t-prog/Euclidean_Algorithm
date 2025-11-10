#Eculidean Algorithm :
    
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
        
        
#example:         
algorithm = EuclideanAlgorithm (48,18)
print ("the GCD is : " , algorithm.GCD ())







     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
#include the Numpy library
import numpy as np

#define the main() function
def main():

    i = 0    #declare an integer i, set to 0
    x = 119.0    #declare a float (has decimal 0) x, whith value 119
    
       for i in range(120):    #loops i from 0 through 119
           if((i%2)==0): #if i is even
               x += 3.0    #add 3 to x :o
           else:           #if i is odd
               x -= 5.0    #x = x-5

       s = "%3.2e"    #string. % indicates format. 3 amount of int.
                      #2 amount of dec. e sci notation
                      #Then, make a string showing x with sci notation
                      
      print(s)
      
#now, the rest of the program
if __name__ == "__main__":    #if the name of the program is 'main', run it
     main ()                  #This is important if we have more than one function
     
#continue

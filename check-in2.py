import numpy as np		#y

def main():				#y

	i = 0				#y
	x = 119.0			#y	
	
	'''	
	for i in main():	
		i = [x]
							#NOPE
	s = [x, %3.2e]
	print(s)
	'''
	
	for i in range(120):
		if((i%2) == 0):		#The way to check even/odd is with modulo!
			x += 3.			#Remember, x is a float... 
		else:	
			x -= 5.			#...so operations must be w/floats

	s = "%3.2e" % x			#"" make it a string, 3 says the integers, 
							#2 the decimals,
							#e the sci notation
		
	print(s)				
	
'''You forgot the most important part: running the function!'''
if __name__ == "__main__":
	main()
	
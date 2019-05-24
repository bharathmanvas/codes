def find_gcd(a, b): 
      
    while(b): 
        a, b = b, a % b 
      
    return a
		 
def gcd():

    l=(5,10,15,25,35);
    num1 = l[0] 
    num2 = l[1] 
    gcd = find_gcd(num1, num2) 

    for i in range(2, len(l)): 
    	  gcd = find_gcd(gcd, l[i]) 
    print(gcd)

gcd();



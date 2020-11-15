def minimumCntOfFlipsRequired(str): 
      
    # Stores length of str 
    n = len(str);   
    # Store count of 0s in the string 
    zeros = 0; 
  
    # Traverse the string 
    for i in range(n): 
               
        # If current character 
        # is 0 
        if (str[i] == '0'): 
                    
            # Update zeros 
            zeros += 1; 
  
    # If count of 0s in the string 
    # is 0 or n 
    if (zeros == 0 or zeros == n): 
        return 0; 
  
    # Store minimum count of flips 
    # required to make all 0s on the 
    # left and all 1s on the right 
    minFlips = 10000001; 

    # Stores count of 1s on the left 
    # of each index 
    currOnes = 0; 
      
    # Stores count of flips required to make 
    # all 0s on the left and all 1s on the right 
    flips = 0; 
  
    # Traverse the string 
    for i in range(n): 
  
        # If current character is 1 
        if (str[i] == '1'): 
  
            # Update currOnes 
            currOnes += 1; 
  
        # Update flips 
        flips = currOnes + (zeros - (i + 1 - currOnes)); 
  
  
        # Update the minimum  
        # count of flips 
        minFlips = min(minFlips, flips); 
  
    return minFlips; 

# Driver Code 
if __name__ == '__main__': 
    str = "100101"; 
    print(minimumCntOfFlipsRequired(str));

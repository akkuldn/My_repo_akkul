a = [1, 2, 'a'] 
try:  
    print ("Second element = %d" %a[1]) 
  
    # Throws error since there are only 3 elements in array 
    print ("thirdFourth element = %s" %a[2])  
    print("fourth element=%d"%a[4]) 
except Exception as e: 
    print ("Exception ",e)
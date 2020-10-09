def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 2017) : 
            return x 
    return 1
  
# Driver Program 
a = 1701040003
m = 2029
print(modInverse(a, m)) 
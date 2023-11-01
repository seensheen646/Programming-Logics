#7!
#7(6!)....6(5!)....5(4!)...4(3!)...3(2!)
#n(n-1)!

def fact(n): #let say yha n ki value 7 aa gai
   
    a=n  #a k andr 7 ko store kr diya
    while(a>1): #7 greater hai 1 sy to loop k andr aa jao
        n=n*(a-1)  # 7=7*(6) => 7=42 ye condition satify nai ho rhi to kiya kro a ki value km kr do a-1 kr k aur a main store krwa do
         # 7=7*(6) => 7=42 => 7=42*(5) => 7=210 => 7=210*(4) => 7=840 => 7=840*(3) => 7=2520 => 7=2520*(2) => 7=5040
        a=a-1
    return n
print(fact(7))
  
    
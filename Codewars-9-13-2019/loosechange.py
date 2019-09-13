coins= {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
cents=int(4.9999934)

while(cents>=0):
    if cents >= 25:
        coins['Quarters']= cents //25
        cents=cents % 25
        
        continue
    if cents >= 10:
        coins['Dimes']= cents//10
        cents= cents %10
        
        continue
    if cents >=5:
        coins['Nickels']= cents//5
        cents = cents %5
        
        continue
    if cents >=1:
        coins['Pennies']= cents//1
        cents= cents %1
        
        continue
    else:
        break

print(coins)  


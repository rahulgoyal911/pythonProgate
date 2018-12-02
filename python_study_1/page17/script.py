apple_price = 2
# Assign 10 to the money variable
money=10

input_count = input('How many apples do you want?: ')
count = int(input_count)
total_price = apple_price * count
print('You will buy ' + str(count) + ' apples')
print('The total price is ' + str(total_price) + ' dollars')


# Add control flow based on the comparison of money and total_price
if(money>total_price):
    print('You have bought '+str(count)+' apples')
    print('You have '+str(10-total_price)+' dollars left')
    
    
elif(money==total_price):
    print('You will buy ' +count + ' apples')
    print('The total price is ' + str(total_price) + ' dollars')
else:
    print("You do not have enough money")
    
        

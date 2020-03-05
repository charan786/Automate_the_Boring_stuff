def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3*number+1)
        return(3*number+1)

while True:
    try:
       value = int(input('Enter a number!'))
    except:
        print(' A number smarty pants!')
        continue
    if value <0:
        print(' It should not be negative')
        continue
    else:
        break


while value !=1:
    value = collatz(value)
    
        

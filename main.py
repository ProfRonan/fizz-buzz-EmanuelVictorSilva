print ("Digite um número: ")
a = int(input(">"))
if a % 3 == 0 and a % 5 == 0 :
    print("FizzBuzz")
else:
    if a % 3 == 0 :
        print("Fizz")
    elif a % 5 == 0 :
        print("Buzz")
    else:
        print(a)
    

        
    
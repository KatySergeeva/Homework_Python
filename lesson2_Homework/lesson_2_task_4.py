def fizz_buzz(n):
    if n % 3 == 0:
        print ("Fizz") 
    if n % 5 == 0:
        print ("Buzz") 
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
n = int(input("Введите число: "))
print(f"{fizz_buzz(n)}")

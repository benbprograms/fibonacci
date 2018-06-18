def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end='\n')
        a, b = b, a + b
    print("\n")


howFar = input("how far do you want the fibonacci sequence up to: ")
try:
    fib(int(howFar))
except ValueError:
    where = input("enter a number only: ")
except MemoryError:
    print("out of memory")

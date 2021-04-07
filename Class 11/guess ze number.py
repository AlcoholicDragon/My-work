import random
n=random.randint(1,100)
guess=int(input("Guess a number between 1-100:"))
while n!=guess:
    if guess>n:
        print("Too high brah.... too high.")
        print(n)
        break 
    elif guess<n:
        print("Too low boi.")
        print(n)
        break
    elif n==guess:
        print("Bravissimo!Magnificent!Marvellous!Beautiful!")
        print(n) 
        break

import random

def guess_number():
    print("Welcome to the Guess the Number Game!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    guessed = False
    
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
        
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()

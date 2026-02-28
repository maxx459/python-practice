# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number


from random import randint

class Computer:
    def __init__(self):
        self.number = randint(1, 10)


class Game:
    def __init__(self):
        print("-------The Perfect Guess-------")
        print("Hiscore : the lower the greater ")
        try:
            with open("./files/hi-score.txt") as f:
                self.hiscore=int(f.read())
                print(f"Current Hiscore:{self.hiscore}")
        except:
            self.hiscore=0
            print(f"Currently no Hiscore")

        print("Lets start!")

        self.com = Computer()
        self.guess_count = 0

    def play(self):
        while True:
            userguess = int(input("Enter your guess: "))
            self.guess_count += 1

            if userguess > self.com.number:
                print("Lower number please")
            elif userguess < self.com.number:
                print("Higher number please")
            else:
                print("You guessed it right!")
                print("Number of guesses:", self.guess_count)
                if self.hiscore!=0:
                    if self.guess_count<self.hiscore:
                        with open("./files/hi-score.txt","w") as f:
                            f.write(str(self.guess_count))
                        print("new Hiscore updated!")
                else:
                        with open("./files/hi-score.txt","w") as f:
                            f.write(str(self.guess_count))
                        print("Hiscore created!")
                break


# Start game
g = Game()
g.play()
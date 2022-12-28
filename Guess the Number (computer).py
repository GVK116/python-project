import random as ran

class guess:
    def __init__(self,x):
        self.x = x
        self.rand= ran.randint(1,x)

    def guess(self):
        score = 0
        gue = 0
        # gue = int(input(f"Guess the number between {self.x}: "))
        while gue != self.rand:
            gue = int(input(f"Guess the number between {self.x}: "))
            if gue < self.rand:
                print("your number is less than the real number")
            elif gue > self.rand:
                print("your number is greater than the real number")
            score +=1
        print(f"WoW you have guessed the number correctly!! it is {gue}")
        return score

karthik = guess(100)
k = karthik.guess()
print(f"your score is {k}")
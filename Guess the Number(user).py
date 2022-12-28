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

    def computer(self):
        low,high,feedback,score = 1,self.x,'',0
        while feedback != 'c':
            if low !=high:
                gue = ran.randint(low,high)
            else:
                gue = low
            feedback = input(f"is {gue} too high (H), too low(L) or correct(C)").lower()
            if feedback == 'h':
                high = gue -1
            else:
                low = gue +1
            score+=1
        print(f"WoW!! you have guessed correctly")
        return score



karthik = guess(1000)
k = karthik.computer()
print(f"your score is {k}")
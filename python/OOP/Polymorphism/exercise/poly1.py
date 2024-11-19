import random

class Lottery:
  def shuffle(self):
    return [random.randint(1, 99) for _ in range(6)]


class PowerBall(Lottery):
    def shuffle(self):
        # Override to get six random numbers between 1 and 99
        return [random.randint(1, 99) for _ in range(6)]


powerball = PowerBall()
print(powerball.shuffle())
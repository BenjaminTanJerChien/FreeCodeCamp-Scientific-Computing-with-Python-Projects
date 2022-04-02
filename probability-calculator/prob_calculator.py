import copy
import random
import math
# Consider using the modules imported above.

class Hat:
  
  def __init__(self, **kwargs):
    self.contents = []
    for name, value in kwargs.items():
      for i in range(value):
        self.contents.append(name)
    print(self.contents)

  def draw(self, remove):
    removed_balls = []
    if (remove > len(self.contents)):
      return self.content 
    for i in range(remove):
      removed = self.contents.pop(random.randint(0, (len(self.contents) - 1)))
      removed_balls.append(removed)
    return removed_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)

    for color in colors_gotten:
      if (color in expected_copy):
        expected_copy[color] -= 1

  if(all(x <= 0 for x in expected_copy.values())):
     count += 1

  return count / num_experiments
    

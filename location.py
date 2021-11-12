import random
import math

# movement speed is fixed as a global variable (not good practice)
movement_speed = 0.05

class Location:

  def __init__(self, x = None, y = None):

    # when x and y are not provided, generate random coordinates
    if x is None:
      self.x = random.random()
      self.y = random.random()
    # when x and y are given, use those
    else:
      self.x = x
      self.y = y

  # function to check whether x and y are not outside the boundaries
  # of the ideological map; if they are, move back to the boundary
  def boundary_check(self):
    if self.x > 1:
      self.x = 1
    elif self.x < 0:
      self.x = 0
    
    if self.y > 1:
      self.y = 1
    elif self.y < 0:
      self.y = 0
  
  # calculate Euclidean distance between two locations
  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
  
  # move in a particular direction (in degrees)
  def move_direction(self, degrees):
    self.x += math.sin(degrees / 180 * math.pi) * movement_speed
    self.y += math.cos(degrees / 180 * math.pi) * movement_speed
    
    self.boundary_check()

  # move towards another location
  def move_towards(self, other):
    delta_x = other.x - self.x
    delta_y = other.y - self.y
    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

    if distance > movement_speed:
      self.x += delta_x * movement_speed / distance
      self.y += delta_y * movement_speed / distance
    else:
      self.x += delta_x
      self.y += delta_y
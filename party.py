from location import Location
import random

class Party:

  def __init__(self, simulation, strategy):
    self.simulation = simulation
    self.location = Location(self.simulation)
    self.strategy = strategy
    self.voters = []

    # extra information needed for predator parties
    self.previous_votes = None
    self.previous_direction = None

  def add_voter(self, voter):
    self.voters.append(voter)
  
  def clear_votes(self):
    self.voters = []
  
  def votes(self):
    return len(self.voters)

  def store_votes(self):
    self.previous_votes = self.votes()

  # sticker strategy: do nothing
  def update_sticker(self):
    pass
  
  # aggregate strategy: find the mean position of all voters and move
  # towards it
  def update_aggregator(self):
    sumx = sumy = 0

    for voter in self.voters:
      sumx += voter.location.x
      sumy += voter.location.y
    
    self.location.move_towards(Location(self.simulation, sumx / len(self.voters), sumy / len(self.voters)))
  
  # hunter strategy: go in a random direction, if votes decrease, turn
  def update_hunter(self):
    # if there was no previous election, move in a random direction
    if self.previous_votes is None:
      self.previous_direction = random.randint(0, 359)
      self.location.move_direction(self.previous_direction)
    # if votes go down, move in a random direction, at least 90 degrees
    # to the right or left
    elif self.previous_votes > self.votes():
      self.previous_direction += random.randint(90, 180)
      self.previous_direction %= 360
      self.location.move_direction(self.previous_direction)
    # if votes do not go down, continue in same direction
    else:
      self.location.move_direction(self.previous_direction)

  # predator strategy: find the largest party and move towards it
  def update_predator(self, parties):
    biggest_party = parties[0]
    for party in parties:
      if party.votes() > biggest_party.votes():
        biggest_party = party
        
    self.location.move_towards(biggest_party.location)

  # random strategy: move in a random direction
  def update_random(self):
    self.location.move_direction(random.randint(0, 359))
  
  # general update function to select update function based on strategy
  def update(self, parties):
    if self.strategy == "sticker":
      self.update_sticker()
    elif self.strategy == "hunter":
      self.update_hunter()
    elif self.strategy == "predator":
      self.update_predator(parties)
    elif self.strategy == "aggregator":
      self.update_aggregator()
    elif self.strategy == "random":
      self.update_random()
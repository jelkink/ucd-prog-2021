from location import Location

class Voter:

  # upon initialisation, take on a random location
  def __init__(self, simulation):
    self.simulation = simulation
    self.location = Location(self.simulation)

  # find nearest party and register self as a voter
  def vote(self, parties):
    nearest_party = parties[0]
    shortest_distance = 1e10

    for party in parties:
      distance = party.location.distance(self.location)
      if distance < shortest_distance:
        nearest_party = party
        shortest_distance = distance
    
    nearest_party.add_voter(self)
from voter import Voter
from party import Party
from log import Log

class Simulation:

  def __init__(self, number_of_voters):
    self.voters = []
    self.parties = []
    self.time = 0
    self.log = Log("log.txt")

    for i in range(number_of_voters):
      self.voters.append(Voter(self))
  
  def add_party(self, strategy):
    self.log.write("Add party with " + strategy + " strategy")
    self.parties.append(Party(self, strategy))

  def run(self, time_steps):

    self.log.write("Start simulation run of " + format(time_steps, "d") + " steps")
    for t in range(time_steps):
      for party in self.parties:
        party.clear_votes()
      
      for voter in self.voters:
        voter.vote(self.parties)
      
      for party in self.parties:
        party.update(self.parties)

      self.time += 1
    self.log.write("End simulation run")
  
  def print_parties_list(self):
    print("\nTime = %d" % self.time)
    for i, party in enumerate(self.parties):
      print("Party %02d (%10s @ %.2f,%.2f): %10d votes" % (i, party.strategy, party.location.x, party.location.y, party.votes()))
  
  def get_log(self):
    return self.log
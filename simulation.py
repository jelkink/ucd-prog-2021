from voter import Voter
from party import Party
from log import Log
from tracker import Tracker

class Simulation:

  def __init__(self, config):
    self.config = config
    self.voters = []
    self.parties = []
    self.time = 0
    self.tracker = Tracker(self)

    self.log = Log(config.get_log_filename())
    self.log.write("Create simulation with " + format(config.get_number_of_voters(), "d") + " voters")

    for i in range(config.get_number_of_voters()):
      self.voters.append(Voter(self))
    
    for party in config.get_parties():
      self.parties.append(Party(self, party["name"], party["strategy"]))

  def run(self, time_steps):

    self.log.write("Start simulation run of " + format(time_steps, "d") + " steps")
    for t in range(time_steps):
      for party in self.parties:
        party.clear_votes()
      
      for voter in self.voters:
        voter.vote(self.parties)
      
      for party in self.parties:
        party.update(self.parties)
      
      self.tracker.save_state()

      self.time += 1
    self.log.write("End simulation run")
  
  def save_output(self):
    self.tracker.save_output_file()
  
  def print_parties_list(self):
    print("\nTime = %d" % self.time)
    for party in self.parties:
      print("Party %10s (%10s @ %.2f,%.2f): %10d votes" % (party.name, party.strategy, party.location.x, party.location.y, party.votes()))
  
  def get_log(self):
    return self.log
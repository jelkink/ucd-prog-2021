import csv

class Tracker:

  def __init__(self, simulation):
    self.simulation = simulation
    self.data = []

  def save_state(self):
    for party in self.simulation.parties:
      self.data.append([
        self.simulation.time,
        party.location.x,
        party.location.y,
        party.votes()
      ])
    
  def save_output_file(self):

    party_names = []
    party_strategies = []
    for party in self.simulation.parties:
      party_names.append(party.name)
      party_strategies.append(party.strategy)
    n_parties = len(self.simulation.parties)

    with open(self.simulation.config.get_output_filename(), "w") as output:
      output_writer = csv.writer(output)
      output_writer.writerow(["time", "party", "strategy", "x", "y", "votes"])
      
      for i, line in enumerate(self.data):
        output_writer.writerow([
          party_names[i % n_parties],
          party_strategies[i % n_parties]] + line)

    self.simulation.log.write("Output saved to \"" + self.simulation.config.get_output_filename() + "\"")

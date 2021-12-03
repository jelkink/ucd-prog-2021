import csv

class Tracker:

  def __init__(self, simulation):
    self.simulation = simulation
    self.data = []

  def save_state(self):
    for party in self.simulation.parties:
      self.data.append({
        "time": self.simulation.time,
        "party": party.name,
        "strategy": party.strategy,
        "x": party.location.x,
        "y": party.location.y,
        "votes": party.votes()
      })
    
  def save_output_file(self):
    with open(self.simulation.config.get_output_filename(), "w") as output:
      output_writer = csv.writer(output)
      output_writer.writerow(["time", "party", "strategy", "x", "y", "votes"])
      
      for line in self.data:
        output_writer.writerow(line.values())

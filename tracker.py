import csv

class Tracker:

  def __init__(self, simulation):
    self.simulation = simulation
    self.data = []

  ## Note that this is a very memory inefficient way to store
  ## the data, as each time step, all party names and strategies
  ## are saved, and for each data point, the names of the variables
  ## ("time", "party", etc.) are saved to memory again. Much more
  ## efficient to just store the numerical data and write a more
  ## complicated save_output_file that figures out what is what.
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

    self.simulation.log.write("Output saved to \"" + self.simulation.config.get_output_filename() + "\"")

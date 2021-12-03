import json

class Configuration:

  def __init__(self, filename):
    with open(filename, "r") as config_file:
      self.data = json.load(config_file)
    
  def get_log_filename(self):
    return self.data["log-file"]
  
  def get_number_of_voters(self):
    return self.data["voters"]
  
  def get_parties(self):
    return self.data["parties"]
  
  def get_speed(self):
    return self.data["speed"]
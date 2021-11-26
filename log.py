from datetime import datetime

class Log:

  def __init__(self, filename):
    self.filename = filename
  
  def write(self, message):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
    with open(self.filename, "a") as log:
      log.write(stamp + message + "\n")
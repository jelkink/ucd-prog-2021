from simulation import Simulation
from configuration import Configuration

config = Configuration("config.json")

# create simulation
sim = Simulation(config)

# run 1 election to report on starting point
sim.run(1)
sim.print_parties_list()

# show results after 100 elections
sim.run(99)
sim.print_parties_list()

sim.save_output()
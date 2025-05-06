import numpy as np
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

states = ["Sunny", "Cloudy", "Rainy"]

T = np.array([
  [0.50, 0.40, 0.10],
  [0.30, 0.35, 0.35],
  [0.20, 0.50, 0.30]
])

def simulate(init: str, n: int = 10):
  current = init
  sequence = []

  for _ in range(n):
    match current:
      case "Sunny":
        _next = np.random.choice(states, p=T[0])
      case "Cloudy":
        _next = np.random.choice(states, p=T[1])
      case "Rainy":
        _next = np.random.choice(states, p=T[2])
    current = _next
    sequence.append(current)
  
  return sequence

simulate("Sunny", 10)

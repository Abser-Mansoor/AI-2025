import numpy as np
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

disease_states = ['Flu', 'Cold']
symptom_states = ['Yes', 'No']

model = DiscreteBayesianNetwork([
  ('Disease', 'Fever'),
  ('Disease', 'Cough'),
  ('Disease', 'Fatigue',),
  ('Disease', 'Chills')
])

disease_cpd = TabularCPD(
  variable='Disease',
  variable_card=2,
  values=[
    [0.3],
    [0.7]
  ],
  state_names={
    'Disease': disease_states
  }
)

# P(Fever | Disease)
fever_cpd = TabularCPD(
  variable='Fever',
  variable_card=2,
  values=[
    [0.9, 0.5],
    [0.1, 0.5]
  ],
  evidence=['Disease'],
  evidence_card=[2],
  state_names={
    'Fever': symptom_states,
    'Disease': disease_states
  }
)

# P(Cough | Disease)
cough_cpd = TabularCPD(
  variable='Cough',
  variable_card=2,
  values=[
    [0.8, 0.6],
    [0.2, 0.4]
  ],
  evidence=['Disease'],
  evidence_card=[2],
  state_names={
    'Cough': symptom_states,
    'Disease': disease_states
  }
)

# P(Chills | Disease)
chills_cpd = TabularCPD(
  variable='Chills',
  variable_card=2,
  values=[
    [0.6, 0.4],
    [0.4, 0.6]
  ],
  evidence=['Disease'],
  evidence_card=[2],
  state_names={
    'Chills': symptom_states,
    'Disease': disease_states
  }
)

# P(Fatigue | Disease)
fatigue_cpd = TabularCPD(
  variable='Fatigue',
  variable_card=2,
  values=[
    [0.7, 0.3],
    [0.3, 0.7]
  ],
  evidence=['Disease'],
  evidence_card=[2],
  state_names={
    'Fatigue': symptom_states,
    'Disease': disease_states
  }
)

model.add_cpds(fever_cpd, disease_cpd, chills_cpd, cough_cpd, fatigue_cpd)

assert model.check_model(), "Model incorrect"

plt.figure(figsize=(3, 3))
nx.draw(model,
  with_labels=True, 
  node_size=1500,
  pos=nx.circular_layout(model)
)
plt.show()

inference = VariableElimination(model)

result1 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes'})
result2 = inference.query(variables=['Disease'], evidence={'Fever': 'Yes', 'Cough': 'Yes', 'Chills': 'Yes'})
result3 = inference.query(variables=['Fatigue'], evidence={'Disease': 'Flu'})

print(result1)
print(result2)
print(result3) # P(Fatigue = Yes | Disease = Flu) = 0.7

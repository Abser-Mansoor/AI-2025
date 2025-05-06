grade_states = ['A', 'B', 'C']
intel_states = ['High', 'Low']
study_states = ['Suff.', 'Insuff.']
diff_states  = ['Hard', 'Easy']
pass_states = ['Yes', 'No']

model = DiscreteBayesianNetwork([
  ('Intelligence', 'Grade'),
  ('Study Hours', 'Grade'),
  ('Difficulty', 'Grade'),
  ('Grade', 'Pass')
])

cpd_intel = TabularCPD(
  variable='Intelligence',
  variable_card=2,
  values=[
    [0.7],
    [0.3]
  ],
  state_names={
    'Intelligence': intel_states
  }
)

cpd_study = TabularCPD(
  variable='Study Hours',
  variable_card=2,
  values=[
    [0.6],
    [0.4]
  ],
  state_names={
    'Study Hours': study_states
  }
)

cpd_diff = TabularCPD(
  variable='Difficulty',
  variable_card=2,
  values=[
    [0.4],
    [0.6]
  ],
  state_names={
    'Difficulty': diff_states
  }
)

# P(Grade | Intel, Study, Diff)
cpd_grade = TabularCPD(
  variable='Grade',
  variable_card=3,
  values=[
		[0.6, 0.8, 0.3, 0.5, 0.2, 0.4, 0.1, 0.2],
		[0.3, 0.15, 0.4, 0.3, 0.4, 0.4, 0.3, 0.3],
		[0.1, 0.05, 0.3, 0.2, 0.4, 0.2, 0.6, 0.5]
	],
  evidence=['Intelligence', 'Study Hours', 'Difficulty'],
  evidence_card=[2, 2, 2],
  state_names={
    'Intelligence': intel_states,
    'Study Hours': study_states,
    'Difficulty': diff_states,
    'Grade': grade_states
  }
)

# P(Pass | Grade)
cpd_pass = TabularCPD(
  variable='Pass',
  variable_card=2,
  values=[
    [0.95, 0.8, 0.5],
    [0.05, 0.2, 0.5]
  ],
  evidence=['Grade'],
  evidence_card=[3],
  state_names={
    'Grade': grade_states,
    'Pass': pass_states
  }
)

model.add_cpds(cpd_grade, cpd_diff, cpd_intel, cpd_pass, cpd_study)

inference = VariableElimination(model)

result1 = inference.query(variables=['Pass'], evidence={'Study Hours': 'Suff.', 'Difficulty': 'Hard'})
result2 = inference.query(variables=['Intelligence'], evidence={'Pass': 'Yes'})

print(result1)
print(result2)

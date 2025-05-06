import numpy as np
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

p_red = 2 * 13/52

print("P(Red) =", p_red)

p_hearts_and_red = 13/52
p_hearts_given_red = p_hearts_and_red / p_red

print("P(Hearts | Red) =", p_hearts_given_red)

p_face_cards = 4 * 3/52
p_diamonds = 3/52
p_diamonds_given_face_cards = p_diamonds / p_face_cards

print("P(Diamond | Face) =", p_diamonds_given_face_cards)

p_spade_or_queen = (3 + 3) / 52
p_spade_or_queen_give_face_cards = p_spade_or_queen / p_face_cards
print("P(Spade OR Queen | Face) =", p_spade_or_queen_give_face_cards)

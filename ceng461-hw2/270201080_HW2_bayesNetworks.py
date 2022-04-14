# CAN ÇİFTÇİ - 270201080

import numpy as np

from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.factors.discrete import TabularCPD

# EXERCISE 1 CODE

network = BayesianNetwork([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E')])

cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.8], [0.2]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.8, 0.2], [0.2, 0.8]], evidence=['A'], evidence_card=[2])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.95, 0.8], [0.05, 0.2]], evidence=['A'], evidence_card=[2])
cpd_D = TabularCPD(variable='D', variable_card=2, values=[[0.95, 0.2, 0.2, 0.2], [0.05, 0.8, 0.8, 0.8]], evidence=['B', 'C'], evidence_card=[2, 2])
cpd_E = TabularCPD(variable='E', variable_card=2, values=[[0.4, 0.2], [0.6, 0.8]], evidence=['C'], evidence_card=[2])


network.add_cpds(cpd_A, cpd_B, cpd_C, cpd_E, cpd_D)
network.check_model()

inference = VariableElimination(network)
q1 = inference.query(['D'])
q2 = inference.query(['D', 'A'])
q3 = inference.query(['E'], evidence={'B':0})
q4 = inference.query(['A'], evidence={'D': 1, 'E':0})
q5 = inference.query(['B', 'E'], evidence={'A': 1})

print("************* EXERCISE 1 **************\n\n")

print("USING VARIABLE ELIMINATION\nWITH PGMPY\n")

print("P(+D) => ", q1.values[1], "\n")
print("TABLE \n")
print(q1,"\n")
print("******************************************\n")
print("P(+D,-A) => ", q2.values[0][1], "\n")
print("TABLE \n")
print(q2,"\n")
print("******************************************\n")
print("P(+E |-B) => ", q3.values[1], "\n")
print("TABLE \n")
print(q3,"\n")
print("******************************************\n")
print("P(+A | +D, -E) => ", q4.values[1], "\n")
print("TABLE \n")
print(q4,"\n")
print("******************************************\n")
print("P(+B,-E|+A) => ", q5.values[1][0], "\n")
print("TABLE \n")
print(q5,"\n\n")

# EXERCISE 2 CODE

print("************* EXERCISE 2 ************* \n")

A = []
B = []
C = []
D = []
E = []

count_D_not_A = 0
count_E_given_not_B = 0
count_not_B = 0
count_D_not_E = 0
count_A_given_D_E = 0
count_A = 0
count_B_not_E_given_A = 0
SAMPLE_NUMBER = 1000000

for i in range (SAMPLE_NUMBER):
    A_happen = np.random.rand() < 0.2
    A.append(A_happen)
    if A_happen:
        B_happen = np.random.rand() < 0.8
        C_happen = np.random.rand() < 0.2
    else:
        B_happen = np.random.rand() < 0.2
        C_happen = np.random.rand() < 0.05
    B.append(B_happen)
    C.append(C_happen)
    if B_happen and C_happen:
        D_happen = np.random.rand() < 0.8
    elif B_happen and not C_happen:
        D_happen = np.random.rand() < 0.8
    elif not B_happen and C_happen:
        D_happen = np.random.rand() < 0.8
    elif not B_happen and not C_happen:
        D_happen = np.random.rand() < 0.05
    D.append(D_happen)
    if C_happen:
        E_happen = np.random.rand() < 0.8
    else:
        E_happen = np.random.rand() < 0.6
    E.append(E_happen)

    if not A_happen and D_happen:
        count_D_not_A += 1
    if not B_happen:
        count_not_B += 1
        if E_happen:
            count_E_given_not_B += 1

    if D_happen and not E_happen:
        count_D_not_E += 1
        if A_happen:
            count_A_given_D_E += 1

    if A_happen:
        count_A += 1
        if B_happen and not E_happen:
            count_B_not_E_given_A += 1

print("USING MONTE CARLO TECHNIQUE\nWITH ",SAMPLE_NUMBER," SAMPLE\n")

print("P(+D) =",sum(D)/SAMPLE_NUMBER)
print("P(+D,-A) =", count_D_not_A / SAMPLE_NUMBER)
print("P(+E |-B) =", count_E_given_not_B / count_not_B)
print("P(+A | +D, -E) =", count_A_given_D_E / count_D_not_E)
print("P(+B,-E|+A) =", count_B_not_E_given_A / count_A)

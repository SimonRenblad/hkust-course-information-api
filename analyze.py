import pickle
from igraph import *

with open('courses.pickle', 'rb') as handle:
    courses = pickle.load(handle)

#create a directed graph
print(courses["IEDA3560"])

g = Graph(directed=True)


import pickle

with open('courses.pickle', 'rb') as handle:
    courses = pickle.load(handle)

print(courses["IEDA3560"])
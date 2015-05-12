import re
import numpy
import math
import random

training_set_a = [] 
test_set_a = []
training_set_b = [] 
test_set_b = []

def load(fn, ds):
	f = open(fn, "r")
	for line in f:
		tokens = line.split()
		features = []
		for i in range(0, len(tokens) - 1):
			features.append(int(tokens[i]))
		data = (features, int(tokens[len(tokens) - 1]))
		ds.append(data)

load("hw4atrain.txt", training_set_a)
load("hw4atest.txt",test_set_a)
load("hw4btrain.txt", training_set_b)
load("hw4btest.txt", test_set_b)

print len(training_set_a)
print len(test_set_a)
print len(training_set_b)
print len(test_set_b)
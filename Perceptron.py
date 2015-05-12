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

def convertLabel(ds, label_neg, label_pos):
	for i in range(0, len(ds)):
		(features, label) = ds[i]
		if label == label_pos:
			ds[i] = (features, 1)
		elif label == label_neg:
			ds[i] = (features, -1)
		else:
			print "uh oh"

load("hw4atrain.txt", training_set_a)
load("hw4atest.txt",test_set_a)
load("hw4btrain.txt", training_set_b)
load("hw4btest.txt", test_set_b)

convertLabel(training_set_a, 0, 6)
convertLabel(test_set_a, 0 ,6)



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
def init_w(sample):
	w = []
	for i in range(0,len(sample[0])):
		w.append(0)
	return w

def dot_product(a, b):
	res = 0
	for i in range(0, len(a)):
		res = res + a[i] * b[i]
	return res

def add_vector(vector0, vector1, y):
	res = []
	for i in range(0, len(vector0)):
		if y == 1:
			res.append(vector0[i] + vector1[i])
		elif y == -1:
			res.append(vector0[i] - vector1[i])
		else:
			print "uhoh"
	return res


def perceptron(training_set):
	res = []
	w = init_w(training_set[0])
	counter = 1
	for (features, label) in training_set:
		if label * dot_product(w, features) <= 0:
			res.append((w,counter))
			counter = 1
			w = add_vector(w, features, label)
		else:
			counter = counter + 1
	return res

load("hw4atrain.txt", training_set_a)
load("hw4atest.txt",test_set_a)
load("hw4btrain.txt", training_set_b)
load("hw4btest.txt", test_set_b)

convertLabel(training_set_a, 0, 6)
convertLabel(test_set_a, 0 ,6)

vecs = perceptron(training_set_a)
print vecs[0]



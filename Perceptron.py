import re
import numpy as np
import math
import random
import copy

def load(fn):
	data_matrix = []
	f = open(fn, "r")
	for line in f:
		tokens = line.split()
		features = []
		for i in range(len(tokens) - 1):
			features.append(int(tokens[i]))
		data = (features, int(tokens[-1]))
		data_matrix.append(data)
	return np.array(data_matrix)

def convertLabel(data_matrix, label_neg, label_pos):
	for i in range(len(ds)):
		(features, label) = ds[i]
		if label in label_pos:
			ds[i] = (features, 1)
		elif label in label_neg:
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
			res.append((w, counter))
			counter = 1
			w = add_vector(w, features, label)
		else:
			counter = counter + 1
	res.append((w, counter))
	return res

def vote(results, features):
	counter = 0
	for (w, count) in results:
		dp = dot_product(w, features)
		if dp < 0:
			counter = counter - count
		elif dp > 0:
			counter = counter + count
	return counter

def voted_perceptron(test_set, results):
	num_samples = len(test_set)
	errors = 0
	for (features, label) in test_set:
		tally = vote(results, features)
		if tally <= 0 and label > 0:
			errors = errors + 1
		elif tally >= 0 and label < 0:
			errors = errors + 1
	return float(errors)/float(num_samples)

def scale(original, scalar):
	scaled = []
	for i in range(0, len(original)):
		scaled.append(original[i] * scalar)
	return scaled

def average_scaled_w(results):
	average_w = results[0][0]
	for i in range (1, len(results)):
		(w, count)  = results[i]
		average_w = add_vector(average_w, scale(w, count), 1)
	return average_w

def average_perceptron(test_set, results):
	w = average_scaled_w(results)
	num_samples = len(test_set)
	errors = 0
	for (feature, label) in test_set:
		dp = dot_product(feature, w)
		if dp <= 0 and label > 0:
			errors = errors + 1
		if dp >= 0 and label < 0:
			errors = errors + 1
	return float(errors)/float(num_samples)

def complement10(k):
	a = []
	b = []
	for i in range (0, 10):
		if i == k:
			a.append(i)
		else:
			b.append(i)
	return (a,b)

def one_vs_all_vector_generate(training_set):
	w_list = []
	for i in range(0, 10):
		(one, a) = complement10(i)
		training_set_copy = copy.deepcopy(training_set)
		convertLabel(training_set_copy, one, a)
		vecs = perceptron(training_set_copy)
		w_list.append(vecs[len(vecs) - 1])
	return w_list

def one_vs_all(test_set, w_vectors):
	num_samples = len(test_set)
	errors = 0
	for (feature, label) in test_set:
		guess = -1
		for i in range(0,10):
			w = w_vectors[i][0]
			dp = -1 * dot_product(w, feature)
			if dp > 0:
				if guess == -1:
					guess = i
				else :
					guess = -2
		if not(guess == label):
			errors = errors + 1
	return float(errors) / float(num_samples)

def main():
	training_set_a = load("hw4atrain.txt")
	test_set_a = load("hw4atest.txt")
	training_set_b = load("hw4btrain.txt")
	test_set_b = load("hw4btest.txt")
	debug_set = load("test.txt")

	convertLabel(training_set_a, [0], [6])
	convertLabel(test_set_a, [0], [6])

	#vecs = perceptron(training_set_a)
	#print voted_perceptron(test_set_a, vecs)
	#print average_perceptron(test_set_a, vecs)

	w_vectors = one_vs_all_vector_generate(training_set_b)
	print one_vs_all(test_set_b, w_vectors)

if __name__ == '__main__':
	main()

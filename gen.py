import random

def generate_random_sequence(n):
	options = ['A', 'T', 'G', 'C']
	output = []
	for i in range(n):
		output.append(options[random.randint(0,3)])
	return output

print(generate_random_sequence(20))
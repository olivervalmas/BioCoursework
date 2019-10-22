#!/usr/bin/python
import time
import sys
import numpy as np

seq1 = ['A', 'C', 'G']
seq2 = ['A', 'G', 'T']

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix

# ------------------------------------------------------------

# matrix full of 0s
scoring_matrix = [[0 for col in range(len(seq1)+1)] for row in range(len(seq2)+1)]
# matrix full of ''
backtrack_matrix = [['' for col in range(len(seq1)+1)] for row in range(len(seq2)+1)]

# populate first column/row of scoring and backtracking matrices
for a in range(len(seq1)+1):
    scoring_matrix[0][a] = -2*a
    backtrack_matrix[0][a] = 'L'
for b in range(len(seq2)+1):
    scoring_matrix[b][0] = -2*b
    backtrack_matrix[b][0] = 'U'

backtrack_matrix[0][0] = 'END'

def s(i,j):
    # idea: check scoring matrix first to see if already defined
    # return an array, first item represents score, second represents where it came from (for backtracking)
    if i == 0:
        return (-2*j,'')
    if j == 0:
        return (-2*i,'')
    else:
        l = [(c(i,j) + s(i-1,j-1)[0], "D"), (s(i-1,j)[0] - 2, "L"), (s(i,j-1)[0] - 2, "U")]
        return max(l,key=lambda item:item[0])

def c(i,j):
    if seq1[i-1] == 'A' and seq2[j-1] == 'A':
        return 4
    elif seq1[i-1] == 'C' and seq2[j-1] == 'C':
        return 3
    elif seq1[i-1] == 'G' and seq2[j-1] == 'G':
        return 2
    elif seq1[i-1] == 'T' and seq2[j-1] == 'T':
        return 1
    elif seq1[i-1] == '-' or seq2[j-1] == '-':
        return -2
    else:
        return -3

# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------

"""
# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()
"""
#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 

# populate rest of scoring matrix

# column
for i in range(1,len(seq1)+1):
	# row
    for j in range(1,len(seq2)+1):
    	# scoring[column][row]
        scoring_matrix[j][i] = s(i,j)[0]
        backtrack_matrix[j][i] = s(i,j)[1]

print(np.array(scoring_matrix))

print(np.array(backtrack_matrix))


best_score = scoring_matrix[len(seq2)][len(seq1)]


letter = backtrack_matrix[-1][-1]  

exit()

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

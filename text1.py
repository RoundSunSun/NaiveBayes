import pandas as pd
from numpy import *
import numpy as np
from np import prob_tokens_spam
from np import prob_tokens_nonspam
emails_nums = 260
# Store the train feature as train_mat
test_f = np.loadtxt('test-features.txt', dtype = int_)
test_mat = np.zeros((emails_nums,2500))
for row in test_f:
    test_mat[row[0]-1][row[1]-1] = row[2]

numTestDocs = 260
numTokens = 2500
output = np.zeros((260, 1))
log_a, log_b = np.zeros((260, 1)), np.zeros((260, 1))
prob_tokens_nonspam_mat = np.mat(prob_tokens_nonspam)
prob_tokens_spam_mat = np.mat(prob_tokens_spam)
prob_tokens_nonspam_T = np.transpose(prob_tokens_nonspam_mat)
prob_tokens_spam_T = np.transpose(prob_tokens_spam_mat)
prob_tokens_nonspam_log = np.log10(prob_tokens_nonspam_T)
prob_tokens_spam_log = np.log10(prob_tokens_spam_T)
prob_tokens_spam_dot = np.dot(test_mat, prob_tokens_spam_log)
prob_tokens_nonspam_dot = np.dot(test_mat, prob_tokens_nonspam_log)
log_a = np.add(prob_tokens_spam_dot, log10(0.5))
log_b = np.add(prob_tokens_nonspam_dot, log10(0.5))
for i in range(260):
    if log_a[i][0] >= log_b[i][0]:
        output[i][0] = 1
    else:
        output[i][0] = 0

test_labels = pd.read_table('test-labels.txt', sep=' ', names=['flag'])
test_labels_mat = mat(zeros((260,1)))
for i in range(len(test_labels)):
    test_labels_mat[i][0] = test_labels.loc[i].flag
numdocs_wrong = np.sum(np.logical_xor(output,test_labels_mat))
print(numdocs_wrong)
fraction_wrong = numdocs_wrong/numTestDocs
print(fraction_wrong)

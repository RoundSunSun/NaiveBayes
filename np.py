import numpy as np
emails_nums = 700

# Store the train feature as train_mat
train_f = np.loadtxt('train-features.txt', dtype = np.int_)
train_mat = np.zeros((emails_nums, 2500))
for row in train_f:
    train_mat[row[0]-1][row[1]-1] = row[2]

# Store the tarin labels as train_labels
# Store (non)spam email index
train_labels = np.loadtxt('train-labels.txt', dtype = np.int_)
spam_indices, nonspam_indices = [], []
for i in range(len(train_labels)):
    if train_labels[i] == 0:
        nonspam_indices.append(i)
    else:
        spam_indices.append(i)
print(spam_indices)
# Calculate probability of spam
prob_spam = len(spam_indices) / emails_nums

# Sum the number of words in each email by summing along each row of train_mat
emails_length = []
for i in range(emails_nums):
    sum = 0
    for j in range(len(train_mat[i])):
        sum = sum + train_mat[i][j]
    emails_length.append(sum)

# Now find the total word counts of all the spam emails and nonspam emails
spam_wc,nonspam_wc = 0,0
for i in range(emails_nums):
    if i in nonspam_indices:
        nonspam_wc = nonspam_wc + emails_length[i]
    else:
        spam_wc = spam_wc + emails_length[i]

total_tokens_spam,total_tokens_nonspam = [0 for i in range(2500)],[0 for i in range(2500)]
for i in range(2500):
    for j in range(len(spam_indices)):
        total_tokens_spam[i] += train_mat[spam_indices[j]][i]
for i in range(2500):
    for j in range(len(nonspam_indices)):
        total_tokens_nonspam[i] += train_mat[nonspam_indices[j]][i]

prob_tokens_spam,prob_tokens_nonspam = [0 for i in range(2500)],[0 for i in range(2500)]
numTokens = 2500
for i in range(2500):
     prob_tokens_spam[i] = round((total_tokens_spam[i] + 1) / (spam_wc + numTokens),5)
     prob_tokens_nonspam[i] = round((total_tokens_nonspam[i] + 1) / (nonspam_wc + numTokens),5)

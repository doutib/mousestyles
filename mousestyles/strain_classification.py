# Classification of multi-feature multi-class dataset
# Single IST
# Home Cage Monitoring (HCM) Data on 16 Mouse Strains
#
# Chris Hillar, Feb 8, 2016
# Tecott Lab, UCSF

# import os
from __future__ import print_function, absolute_import, division
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from scipy.cluster.vq import whiten

from data_utils import (day_to_mouse_average,
                        mouse_to_strain_average,
                        split_data_in_half_randomly)


strains = {0: 'C57BL6J', 1: 'BALB', 2: 'A', 3: '129S1', 4: 'DBA', 5: 'C3H',
           6: 'AKR', 7: 'SWR', 8: 'SJL', 9: 'FVB', 10: 'WSB', 11: 'CZECH',
           12: 'CAST', 13: 'JF1', 14: 'MOLF', 15: 'SPRET'}

num_strains = len(strains)

all_data_name = 'data/all_features_mousedays_11bins.npy'
all_data_orig_master = np.load(all_data_name)

feat_arr = ['ASProb', 'ASCounts', 'ASDur', 'Food',
            'Water', 'Distance', 'F_ASInt', 'D_ASInt', 'L_ASInt']
use_features = [3, 4, 5]  # range(len(feat_arr)) # using these features
AS = ''.join(['%s' % feat_arr[i] for i in use_features])

num_bins = len(use_features) * 11

all_data_orig = np.hstack([all_data_orig_master[0, :, 0:3]] +
                          [all_data_orig_master[AS_i, :, 3:]
                          for AS_i in use_features])

# classifiers
NN_classify = np.zeros(2)  # 1st col mice | 2nd MDs
LR_classify = np.zeros(2)
GNB_classify = np.zeros(2)
RF_classify = np.zeros(2)

data = all_data_orig[:, 3:]
labels = all_data_orig[:, 0:3]
data = whiten(data)  # "Z-score"

train, labels_train, test, labels_test = split_data_in_half_randomly(
    data, labels)

mice_train = day_to_mouse_average(train, labels_train)
mice_test = day_to_mouse_average(test, labels_test)

# NN vanilla classification
strain_centers = mouse_to_strain_average(mice_train[:, 2:], mice_train[:, 0:2])

tot_cor = 0
for cnt, ms in enumerate(mice_test):
    min_dist = np.inf
    for k in range(strain_centers.shape[0]):
        distance = np.sqrt(((strain_centers[k] - ms[2:]) ** 2).sum())
        if distance < min_dist:
            guess = k
            min_dist = distance
    if guess == mice_test[cnt, 0]:
        tot_cor += 1

tot_cor1 = tot_cor
tot_cor = 0
for cnt, md in enumerate(test):
    min_dist = np.inf
    for k in range(strain_centers.shape[0]):
        distance = np.sqrt(((strain_centers[k] - md) ** 2).sum())
        if distance < min_dist:
            guess = k
            min_dist = distance
    if guess == labels_test[cnt, 0]:
        tot_cor += 1
tot_cor2 = tot_cor

NN_classify[1] = tot_cor2
NN_classify[0] = tot_cor1

# Logistic Regression
clf1 = LogisticRegression(random_state=123)
X = train
y = labels_train[:, 0]
clf1.fit(X, y)
LR_classify[1] = labels_test.shape[0] * clf1.score(test, labels_test[:, 0])
LR_classify[0] = mice_test.shape[0] * \
    clf1.score(mice_test[:, 2:], mice_test[:, 0])

# Gaussian Naive Bayes
clf2 = GaussianNB()
X = train
y = labels_train[:, 0]
clf2.fit(X, y)
GNB_classify[1] = labels_test.shape[0] * clf2.score(test, labels_test[:, 0])
GNB_classify[0] = mice_test.shape[0] * \
    clf2.score(mice_test[:, 2:], mice_test[:, 0])

# Random forest classifier
clf3 = RandomForestClassifier(random_state=123)
X = train
y = labels_train[:, 0]
clf3.fit(X, y)
RF_classify[1] = labels_test.shape[0] * clf3.score(test, labels_test[:, 0])
RF_classify[0] = mice_test.shape[0] * \
    clf3.score(mice_test[:, 2:], mice_test[:, 0])

# print ("[NN] %s: %1.2f/%d [%1.3f] Mice | %1.2f/%d [%1.3f] MDs" % (AS,
#     NN_classify[0], mice_train.shape[0],
#     1. * NN_classify[0] / mice_train.shape[0],
#     NN_classify[1], test.shape[0], 1. * NN_classify[1] / test.shape[0]))

# print ("[LogReg] %s: %1.2f/%d [%1.3f] Mice | %1.2f/%d [%1.3f] MDs" % (AS,
#    LR_classify[0], mice_train.shape[0], 1. * LR_classify[0] /
#    mice_train.shape[0], LR_classify[1], test.shape[0],
#    1. * LR_classify[1] / test.shape[0]))

# print ("[GaussNB] %s: %1.2f/%d [%1.3f] Mice | %1.2f/%d [%1.3f] MDs" % (AS,
#    GNB_classify[0], mice_train.shape[0],
#    1. * GNB_classify[0] / mice_train.shape[0],
#    GNB_classify[1], test.shape[0], 1. * GNB_classify[1] / test.shape[0]))

# print ("[RF] %s: %1.2f/%d [%1.3f] Mice | %1.2f/%d [%1.3f] MDs" % (AS,
#     RF_classify[0], mice_train.shape[0],
#     1. * RF_classify[0] / mice_train.shape[0],
#     RF_classify[1], test.shape[0], 1. * RF_classify[1] / test.shape[0]))

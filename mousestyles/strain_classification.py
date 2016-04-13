
# coding: utf-8

# In[1]:

# Single IST
# Home Cage Monitoring (HCM) Data on 16 Mouse Strains

import os
import numpy as np
from scipy.cluster.vq import whiten
from data_utils import day_to_mouse_average, mouse_to_strain_average, split_data_in_half_randomly


# In[2]:

strains = {0: 'C57BL6J', 1: 'BALB', 2: 'A', 3: '129S1', 4: 'DBA', 5: 'C3H', 6: 'AKR', 7: 'SWR', 8: 'SJL', 9: 'FVB',10: 'WSB', 11: 'CZECH', 12: 'CAST', 13: 'JF1', 14: 'MOLF', 15: 'SPRET'}

num_strains = len(strains)

all_data_name = 'data/all_features_mousedays_11bins.npy'
all_data_orig_master = np.load(all_data_name)

feat_arr = ['ASProb', 'ASCounts', 'ASDur', 'Food', 'Water', 'Distance', 'F_ASInt', 'D_ASInt', 'L_ASInt']
use_features = [3, 4, 5]  # range(len(feat_arr)) # using these features
AS = ''.join(['%s' % feat_arr[i] for i in use_features])

num_bins = len(use_features) * 11

all_data_orig = np.hstack([all_data_orig_master[0, :, 0:3]]+ [all_data_orig_master[AS_i, :, 3:] for AS_i in use_features])


# In[3]:

data = all_data_orig[:, 3:]
labels = all_data_orig[:, 0:3]
data = whiten(data)  # "Z-score"

X_train, Y_train, X_test, Y_test = split_data_in_half_randomly(data, labels)



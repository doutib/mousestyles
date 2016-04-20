# Tecott Lab HCM Data
# Normalized PCA anlaysis of HCM Data Features
# C. Hillar, Dec 2015 (Tecott Lab: C. Hillar, G. Onnis, D. Rhea, L. Tecott)

from __future__ import print_function, absolute_import, division
import numpy as np
from data_utils import day_to_mouse_average
import matplotlib.pyplot as plt


strains = {0: 'C57BL6J', 1: 'BALB', 2: 'A', 3: '129S1', 4: 'DBA', 5: 'C3H',
           6: 'AKR', 7: 'SWR', 8: 'SJL', 9: 'FVB', 10: 'WSB', 11: 'CZECH',
           12: 'CAST', 13: 'JF1', 14: 'MOLF', 15: 'SPRET'}

feat_arr = ['ASProbability', 'ASNumbers', 'ASDurations', 'Food', 'Water',
            'Distance', 'ASFoodIntensity', 'ASWaterIntensity',
            'ASLocomotionIntensity']
feat_arr_units = ['Active state probability', 'Number AS onsets',
                  'Total time [sec]', 'Food consumed [g]',
                  'Water consumed [mg]', 'Distance travelled [m]',
                  'ASFoodIntensity', 'ASWaterIntensity',
                  'ASLocomotionIntensity [cm/ASsec]']

all_data_name = 'data/all_features_mousedays_11bins.npy'
# 9 x 1921 x (3 labels + 11 feature time bins)
data_orig_master = np.load(all_data_name)

MOUSEDAYS = False

# Feature to study
AS_i = 0
AS = feat_arr[AS_i]
print("PCA analysis for feature %s" % feat_arr[AS_i])
features = data_orig_master[AS_i, :, 3:]
# 1st col = strain, 2nd = mouse number, 3rd = day
labels = data_orig_master[AS_i, :, 0:3]
if not MOUSEDAYS:
    mice = day_to_mouse_average(features, labels)  # 170 mice
else:
    mice = np.hstack([labels[:, :2], features])  # 1921 mousedays

# Determing linear map L such that vectors LF (F the 11-D feature vector)
# have identity covariance = I
mouse_mz = mice[:, 2:13] - mice[:, 2:13].mean(axis=0)
Cmz = np.dot(mouse_mz.T, mouse_mz) / mouse_mz.shape[0]  # covariance matrix
# eigenvalues and eigenvectors (PCA components) all v[i] norm 1
d, v = np.linalg.eig(Cmz)
idx = np.argsort(d)
v = v[:, idx]       # normalized eigenvectors
d = d[idx]          # eigenvalues
d = d[::-1]         # ordered largest first
v = v[:, ::-1]
for i in range(11):  # make more +s than negatives
    if np.sign(v[:, i]).sum() < 0:
        v[:, i] *= - 1.
Cmz_recon = np.dot(np.dot(v, np.diag(d)), v.T)  # check decomposition
print(np.abs(Cmz - Cmz_recon).sum())

# compute projected features
diag = np.diag(1 / np.sqrt(d))
projected_features = np.dot(mouse_mz, np.dot(v, diag))
projected_features_3d = np.column_stack(
    (mice[:, 0:2], projected_features[:, :3]))
Cov_LF = np.dot(projected_features.T, projected_features) / \
    projected_features.shape[0]
# check covariance of new features is identity
I = np.identity(Cov_LF.shape[0])
print(np.abs(Cov_LF - I).sum())

# plot variance captured
variances_captured = np.zeros(v.shape[0] + 1)
for i in range(Cmz.shape[0] + 1):
    if i > 0:
        variances_captured[i] = d[i - 1] / d.sum()
    print('component %d: %1.4f proportion of variance captured' % (
        i, variances_captured[i]))
plt.figure()
plt.clf()
plt.plot(variances_captured[1:])
plt.xlabel('PCA component (ranked)')
plt.ylabel('Proportion of variance captured')
plt.xticks(np.arange(0, 11, 2), np.arange(1, 12, 2), fontsize=12)
plt.title('Variance captured by %s PCA components' % AS)

plt.figure()
plt.clf()
plt.imshow(v.T, interpolation='nearest')
plt.yticks(np.arange(0, 11, 2), np.arange(1, 11 + 1, 2), fontsize=12)
plt.xticks(np.arange(0, 11, 2), np.arange(1, 12, 2), fontsize=12)
plt.colorbar()
plt.title('PCA Components %s' % (AS))
plt.ylabel('Normalized Component (top component is top row)')
plt.xlabel('Entries of component (2 h time bin)')

# view top components
m_avgs = mice[:, 2:13].mean(axis=0)
first = v[:, 0]
second = v[:, 1]
third = v[:, 2]
fourth = v[:, 3]

plt.figure()
plt.clf()
plt.plot(first, lw=5,
         label='1$^{st}$ principal component: %d%% variance captured' %
               (100 * variances_captured[1]))
plt.plot(second, lw=3, label='2$^{nd}$: %d%%' % (100 * variances_captured[2]))
plt.plot(third, lw=2, label='3$^{rd}$: %d%%' % (100 * variances_captured[3]))
plt.plot(fourth, lw=1, label='4$^{th}$: %d%%' % (100 * variances_captured[4]))
plt.xlabel('2 h Time bin')
plt.ylabel('Normalized PCA units')
plt.xticks(np.arange(0, 11, 2), np.arange(1, 12, 2), fontsize=12)
plt.title('PCA components of %s features' % AS)
legenda = plt.legend(frameon=False, loc='best')
plt.setp(legenda.get_texts(), fontsize=12)

# show how each strain looks like in top 4 components
strain_proj = np.zeros((len(strains), 11))
for strain_num in range(16):
    strain_data = mouse_mz[mice[:, 0] == strain_num, :]
    projected_features = np.dot(strain_data, np.dot(v, diag)).mean(axis=0)
    strain_proj[strain_num] = projected_features

plt.figure()
plt.clf()
plt.imshow(strain_proj[:, :11], interpolation='nearest')
plt.colorbar()
plt.title('%s' % (AS))
plt.ylabel('Strain')
plt.xlabel('Component number (left is top)')
plt.yticks(np.arange(0, len(strains), 2), np.arange(
    1, len(strains) + 1, 2), fontsize=9)
plt.xticks(np.arange(0, 11, 2), np.arange(1, 12, 2), fontsize=12)

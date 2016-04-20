# Tecott Lab HCM Data
# working with AS/IS, IS Duration Thresholds (ISDT)
# using class intervals objects
# C. Hillar, Jan 2016
from __future__ import print_function, absolute_import, division
import numpy as np
from intervals import Intervals


Events = Intervals([[-2, -1], [0, 1], [3, 5], [8, 11]])

ISDT = 2  # IST Threshold

ECG = Events.copy().connect_gaps(ISDT)  # connect gaps <= ISDT
ETm = Events.copy().trim(ISDT)  # trim inteversl <= ISDT

print("Events (%d intervals):" % Events.num(), Events)
# print ("Events connected gaps <= %1.3f:" % ISDT,
#        Events.copy().connect_gaps(ISDT))
print("Events trim intervals <= %1.3f:" % ISDT, Events.copy().trim(ISDT))

print("IS/AS computation version 1")
IS1 = Events.complement().trim(ISDT)  # complement is new object
AS1 = IS1.complement()
print("IS (%d):" % IS1.num(), IS1)
print("AS (%d):" % AS1.num(), AS1)

print("IS/AS computation version 2 (mathematically equivalent)")
AS2 = Events.copy().connect_gaps(ISDT)  # trim alters object
IS2 = AS2.complement()
print("AS2 (%d):" % AS2.num(), AS2)
print("IS2 (%d):" % IS2.num(), IS2)

print("IS/AS built into Intervals")
print("AS1:", Events.ASs(ISDT))
print("IS1:", Events.ISs(ISDT))

# Data set consists of 1921 Mouse days (22 hours each) from 170 Mice and
# 16 Strains:
strains = {0: 'C57BL6J', 1: 'BALB', 2: 'A', 3: '129S1', 4: 'DBA', 5: 'C3H',
           6: 'AKR', 7: 'SWR', 8: 'SJL', 9: 'FVB', 10: 'WSB', 11: 'CZECH',
           12: 'CAST', 13: 'JF1', 14: 'MOLF', 15: 'SPRET'}
events = ['AS', 'F', 'IS', 'M_AS', 'M_IS', 'W']
feat_arr = ['ASProbability', 'ASNumbers', 'ASDurations', 'Food', 'Water',
            'Distance', 'ASFoodIntensity', 'ASWaterIntensity',
            'MoveASIntensity']
feat_arr_units = ['Active state probability', 'Number AS onsets',
                  'Total time [sec]', 'Food consumed [g]',
                  'Water consumed [mg]', 'Distance travelled [m]',
                  'ASFoodIntensity', 'ASWaterIntensity',
                  'MoveASIntensity [cm/ASsec]']
# 9 x 1921 x (3 labels + 11 feature time bins)
data_orig_master = np.load('data/all_features_mousedays_11bins.npy')
features = data_orig_master[:, :, 3:]
# 1st col = strain, 2nd = mouse number, 3rd = day
labels = data_orig_master[0, :, 0:3]

# CHECK: Events = (M_AS + F + W) gives AS correctcly
strain_intervals = [[] for i in range(len(strains))]
for i in range(len(strains)):
    print("Loading Strain %d MDs" % i)
    strain_labels = labels[labels[:, 0] == i]
    mice = {}   # determine mice in strain
    for c in range(strain_labels.shape[0]):
        if not mice.get(strain_labels[c, 1]):
            mice[strain_labels[c, 1]] = 1
        else:
            mice[strain_labels[c, 1]] += 1

    mices = [[[] for c2 in range(mice[c1])] for c1 in range(len(mice))]

    for mouse in range(len(mice)):
        for day in range(mice[mouse]):
            d = np.load('data/intervals/%s/%s_strain%d_mouse%d_day%d.npy' %
                        (events[0], events[0], i, mouse, day))
            AS = Intervals(d)

# to load others:
# F = Intervals(np.load('data/intervals/%s/%s_strain%d_mouse%d_day%d.npy' %
#      (events[1], events[1], i, mouse, day)))
# IS = Intervals(np.load('data/intervals/%s/%s_strain%d_mouse%d_day%d.npy' %
#      (events[2], events[2], i, mouse, day)))
# M_AS = Intervals(np.load('data/intervals/%s/%s_strain%d_mouse%d_day%d.npy' %
#      (events[3], events[3], i, mouse, day)))
# M_IS = Intervals(np.load('data/intervals/%s/%s_strain%d_mouse%d_day%d.npy' %
#      (events[4], events[4], i, mouse, day)))
# W = Intervals(np.load('data/intervals/%s/%s_strain%d_mouse%d_day%d.npy' %
#      (events[5], events[5], i, mouse, day)))
# all_move = M_AS.union(M_IS)
# non_homebase_events = F.union(W).union(M_AS)
# equal to non_homebase_events.ASs(ISDT=20 * 60)
            mices[mouse][day] = AS

    strain_intervals[i] = mices

fmfs = first_mouse_first_strain = strain_intervals[0][0]
nd = nday_this_mouse = len(fmfs)

AS = fmfs[0]
# print "First MD of ASs for first mouse for first strain (%d intervals):" %
# AS.num(), AS

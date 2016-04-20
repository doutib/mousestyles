.. _dynamics:

Dynamics of AS Patterns
=======================

Statement of Problem
--------------------

The objective of Dynamics Analysis is to classify the active states and
inactive states, as well as understand the dynamics/transitions between
AS and IS..

Statement of Statistical Problems
---------------------------------

-  Use the Raw Observation Data of Mouse's spatial and temporal data, to
   classify for each time-stamp whether the mice is in Active State or
   Inactive State, therefore to calculate AS numbers, AS durations, and
   AS probability for the 2-hour bin.
-  Calculate the probability of events transition (e.g. eating =>
   drinking) and of states transition (i.e. active => inactive).
-  Using those probabilities as a feature of our "big model" to predict
   the mice's gene type based on their behavior.

Exploratory Analysis
--------------------

-  Paper Define that when the mice is inside the Home Base, it is in IS.
   However, we make some improvement by adding the assumption that mice
   bring food back to Home Base.

   -  Original Classification:

   -  Improved Classification:

-  EDA on their result to get a rough idea of the expectation: Summary
   statistics and plots can serve starting points to answer our
   problems. For example, it can be helpful to plot the features (e.g.
   food consumption, moving distance) over time bin for all mice.

   -  Food Consumed:

   -  Distance Traveled:

Data Requirements Description
-----------------------------

-  Variables should be explained in detail for further analysis. For
   example, we need to merge the interval data to the main data to apply
   the methodology, but it is little explained how to match the
   time-stamps of the interval data to those of the main data.

Methodology/ Approach Description
---------------------------------

1. First Step: How to define AS and IS States?

-  Feeding(in/out), drinking(in/out), outside HomeBase movement ==> AS
-  The time gaps of two activity < IST ==> AS
-  Complement of AS ==> IS
-  QDA/LDA to classify the IS and AS

   -  P(food \| IS) = 0.01, P(drink \| IS) = 0.01, P(sleep \| IS) = 0.8,
      P(move \| IS) = 0.1, P(digging \| IS) = 0.08
   -  P(food \| AS) = 0.3, P(drink \| AS) = 0.3, P(sleep \| AS) = 0.01,
      P(move \| AS) = 0.3, P(digging \| AS) = 0.09

2. Second Step: Find the Optimal IST(Inactive State Threshold), so as to
   calculate AS numbers, AS Durations. Inspiration by:

   -  Events:

   -  IST vs AS numbers:

3. Third Step: Use Markov chain to model the transition between events:

   .. math:: P(food_{t+1} | drink_{t})

4. Fourth Step: Use Hidden Markov to model the transition between events
   for different stages

.. code:: python

    states = ('AS', 'IS')
     
    observations = ('food', 'water', 'sleep','movement','digging')
     
    start_probability = {'AS': 14/24, 'IS': 10/24}#based on time
     
    transition_probability = {
       'AS' : {'IS': 0.7, 'AS': 0.3},
       'IS' : {'IS': 0.4, 'AS': 0.6},
       }
     
    emission_probability = {
       'IS' : {'food': 0.01, 'water': 0.01, 'sleep': 0.8, 'movement': 0.1, 'digging': 0.08},
       'AS' : {'food': 0.3, 'water': 0.3, 'sleep': 0.01, 'movement': 0.3, 'digging': 0.09},
       }

Testing Framework Outline
-------------------------

-  Main idea: check the reasonability of IST to be the number we choosed
   and the AS probability or Transition probability by testing:
-  Examples:

   -  For each mice, The AS numbers for Night Time bins < The AS numbers
      of Daytime Bins.
   -  P(IS\|Food) < P(AS\|Food)

Additional Remarks:
-------------------

-  Improvement on the definition of AS/IS: whether inside HomeBase
   movement count as AS as well?
-  latent variables?

References:
-----------

http://scikit-learn.sourceforge.net/stable/modules/hmm.html

https://github.com/hmmlearn/hmmlearn

https://en.wikipedia.org/wiki/Hidden\_Markov\_model

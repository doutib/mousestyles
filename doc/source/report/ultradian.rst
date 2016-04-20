.. _ultradian:

Ultradian Analysis
==================

Statement of problem
--------------------

Ultradian rhythm is widely observed in mammalian behavioral patterns.
Ultradian analysis aims to find the time-specific patterns in behavioral
records, without specifying the length of cycle in advance (but need to be
within 1 hour to 1 day). Typical ultradian period for rats includes 4, 12 and
24 hours. For example, we expect rats to be inactive in the nighttime.
Ingestions and movements mostly happened in the daytime. It would be
informative to study the ultradian cycle of the behavior of mouse and we need
to answer the following questions for this study:

What is the variable of interest for the periodic patterns? 

- Summary of activity: Food and water ingestion, distance traveled , movement
  intensity, AS probability.

- Spatial variable: Spatially discrete the data to cells each with its primary
  functions such as food cell, water cell, etc. Examine ultradian cycle of the
  spatial probability densities of the occupancy time in each cells.

How to subset the data?

- Basic subset: 16 strains.

- Strains may not be the primary influence for the variation of ultradian
  rhythms. We may look into the cycle for each mouse and detect the most
  important factors influencing the ultradian rhythms.

How to choose the frequency or period ?

- The Lomb-Scargle (LS) periodogram spectral analysis technique, a widely used
  tool in period detection and frequency analysis.

What is the connection with other subprojects?

- Ultradian rhythms could be treated as one feature for clustering the 16
  strains. We may also subset the data using the results of the cluster and
  analysis the rhythm similarities and differences across clusters.

Statement of statistical problem
--------------------------------

How to determine the optimal bin intervals for constructing the time series?

-  The bin interval may vary according to the frequency. Bin interval
   examples: 5 min, 30 min, 1 hour etc. Need to look into the data.

How to test the autocorrelation coefficient for the data and assess the model?

-  Use the AIC to select best time lags for the time series model and
   the K statistics to test the goodness of fit.

For longitudinal data analysis, how to build the model? Which is the fixed
effect or random effect?

Exploratory Analysis
--------------------

Data investigation

-  Think about known/expected cycles - time to digest, IS/AS cycle,
   etc.
-  Try to investigate cycles that are greater than 24 hours to avoid
   missing cycles.
-  During the acclimatization period, investigate difference in
   cycles.

Plots

-  Plots for determining optimal bin intervals for constructing the
   time series.
-  Plots for discovering the frequency or period.
-  General time series plots for getting intuitions for each
   variables.

Models

-  Usage of Lomb-Scargle (LS) periodogram spectral analysis
   technique, a widely used tool in period detection and frequency
   analysis

Data Requirements Description
-----------------------------

Input: records for each strains (total of 16), each feature of interest (food,
water, distance, active\_state probability, ...), in a duration of 12 days
(excluding 4 acclimation days).

Processed: using one-minute time bins of movement records to binary score the
activity into 0 (IS: inactive state) and 1 (AS: active state); using
thirty-minute bins of food records to calculate the amount of chows consumed by
mice; using LS periodogram technique to select the appropriate time bins for
above.

Output: different patterned visualization for each feature, with the
appropriate time bins that presents the most significant ultradian pattern.

Methodology/Approach Description
--------------------------------

Seasonal decomposition. Seasonal decomposition is a very common method used in
time series analysis. One of the main objectives for a decomposition is to
estimate seasonal effects that can be used to create and present seasonally
adjusted values.

Two basic structures are commonly used::

    1. Additive:  x_t = Trend + Seasonal + Random

    2. Multiplicative:  x_t= Trend * Seasonal * Random

The "Random" term is often called "Irregular" in software for decompositions.

Basic steps::

    1. Estimate the trend

    2. "De-trend" the data

    3. Estimate seasonal factors by using the "de-trended" series

    4. Determine the "random" term

Longitudinal data analysis.

-  Attempts for mixed models

   -  The mixed model is frequently used for longitudinal analysis.
      We should specify the random effects and fixed effects first,
      such as the IS/AS condition, the purpose of the active: like
      food or water and any other important features. Then we can use
      linear mixed model to get the pattern of the movements in
      different time period.
   -  Statsmodels.api package can be used to decompose the dataset we
      have.

Autocorrelation analysis.

-  Implement numpy.correlate functions to investigate autocorrelation
   in several variables for features of interest (food, water,
   distance, active\_state probability ...)
-  Explore different kinds of autocorrelation models (spatial
   analysis, regression analysis) on variables generated by other
   subprojects.

Testing Framework Outline
-------------------------

Step 1: Generating random samples for testing:

- Split the data based on the Mouse Day Cycle
- Number the splits and use numpy.random to subset from these splits

Step 2: Conduct Lomb-Scargle (LS) test to detect the period. Implement the
three different models onto the certain period and get the patterns/ estimated
coefficients for the model.

Step 3: Compare the result with our hypothesis.

Reference
---------

-  Lloyd, David, and Ernest L. Rossi, eds. Ultradian rhythms in life
   processes: An inquiry into fundamental principles of chronobiology
   and psychobiology. Springer Science & Business Media, 2012.
-  Stephenson, Richard, et al. "Sleep-Wake Behavior in the Rat Ultradian
   Rhythms in a Light-Dark Cycle and Continuous Bright Light." Journal
   of biological rhythms 27.6 (2012): 490-501.

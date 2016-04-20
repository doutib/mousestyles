.. _classification:

Classification and Clustering of Mice
=====================================

Statement of overall problem
----------------------------

The mouse style research investigates mouse behaviors of different
genes. The researchers hope to gain insight to human behaviors using
mouse data, since experimenting directly on human is difficult.

The important concern is whether we can classify different strains of
mice based on mouse behaviors through machine learning algorithms.
Important features in classification models will be extracted for future
study. Another question of interest is on whether genetic affects
(different strain effects) psychological disorders such as depression,
or overeating. The fundamental hypothesis is that different mouse
strains have different behaviors, and we are able to use these behaviors
as features to classify mice successfully.

Statement of statistical problems
---------------------------------

The researchers design the experiment as follow: they have 16 different
strains of mice, and each strain has 9 to 12 almost identical male mice
in terms of genetic.

We need to firstly verify the assumption that mouse of different strains
do exhibit different behaviors. One way to do this is to perform
hypothesis testing based on the joint distribution of all the features.
A simpler alternative is to perform EDA on each of the features. If we
observe that each mouse behaves very similarly to its twins, but
differently from other strains of mice, we can conclude that genetic
differences affect mouse behaviors and that behavioral features might be
important for classification. Notice that here we can evaluate the
difference by assessing the classification performance of models based
on behavioral features.

Based on the assumption, the problem is inherently a multiclass
classification problem based on behavioral features either directly
obtained during the experiment or artificially constructed. Here we have
to determine the feature space both from the exploratory analysis and
biological knowledge. If the classification models performed well, we
may conclude that behavioral differences indeed reveal genetic
differences, and dig into the most important features needed seeking the
biological explanations. Otherwise, say if the model fails to
distinguish two different strains of mice, we may study that whether
those strains of mice are genetically similar or the behavior features
we selected are actually homogeneous through different strains of mice.

Exploratory Analysis & Classification Models
--------------------------------------------

In 1D, box plots of each feature, say food consumption or sleeping time,
of each strain can be plotted. In 2D, PCA can be preformed on the
feature data set and the data are then plotted along the first and the
second principal axes colored in different strains. These plots are
useful in verifying assumptions. For instance, we could box-plot
different strains of mice against food consumption to see whether
different strains of mice eat distinctly. If the number of variables
needed to be evaluated is large, we might also use five number summaries
to study the distributions.

Example boxplots: 

.. figure:: figure/features_boxplot_by_strain.png 
   :align:   center

   Example boxplots

Since each strain (each class) only has 9 to 12 mice, inputting too many
features to the classification model is unwise. The exploratory data
analysis will be an important step for hypothesis testing and feature
selection. The process will also help us to find outliers and missing
values in each behavioral variable, and we will decide how to handle
those values after encountering that.

Data Requirements Description
-----------------------------

We dispose of a labeled data set of 16 different strains of mice.
Behavioral features are recorded for each mouse and each day. One
example can be the time spent eating or drinking, and the amount
ingested.

The researchers record the daily activities of each mouse, for example
the time it spends eating, drinking, sleeping, and wondering around its
habitats. Therefore, every behavioral features should be averaged to the
same time period (one mouse day) for each mouse. For example, the food
consumed variable at each timestamp will be aggregated to the average
food consumption.

Notice that the final dataset should be a clean and well formatted
dataframe (in numpy array or pandas dataframe) aggregating the features
of mice so that it can be directly used to train classification models.

Besides, the detailed explanation for each variable and strain type
might be needed for further interpretations of models.

Methodology/ Approach Description
---------------------------------

1.Supervised Classification: Supervised classification algorithms
(logistic regression, random forest, KNN) will be used to detect the
relationship between strain of mice and behavioral features. If we gain
good model performance, we can conclude different mouse behaviors
actually indicate different genetic differences. K-fold cross-validation
might be used to tune model parameters, and a proportion of data would
be used as test data to evaluate the model performance. Notice that we
may manually manipulate so that the both the training data and the test
data cover all strains of mice.

2.Unsupervised clustering In addition, we can use unsupervised machine
learning models (e.g. K-means) to cluster the daily mouse activities
into clusters that correspond to the genes. This means we will not use
the given strain label, instead we will create new labels for mice
purely based on its behaviors by clustering. This can highlight an even
stronger relationship between genes and mouse behaviors.

The step after model fitting is to assess the important behavioral
features in the classification and clustering models. A smaller set of
feature space containing only top features might be used to gain better
interpretations of the model.

Testing Framework outline
-------------------------

-  The first step to test the reproducibility is to test the stability
   of classification models. Since we randomly split the dataset to be
   the test set and the training set, we can train and test the model
   over different seeds and plot the accuracy against different
   trials. We should also see if the important features are stable over
   different trials.

-  From our limited understanding, the results of this research might
   have a meaningful implication on the way we treat psychological
   disorders. If it turns out that nature does influence these
   disorders, we can probably conclude that psychological disorders is
   not much different than physical disabilities. Otherwise, if nature
   has little influence over these disorders, we can try to find way to
   prevent these disorders from happening.

Initial tasks
-------------

1. Clean up the existing strain\_classification.py: create functions and
   objects.
2. Adding new models: knn, random forests, neural networks, logistic
   regressions.
3. Doing unsupervised learning: k-means.
4. Compute confidence interval for the accuracy of each model.
5. Give insights about how mice behavior is related to their genetic
   heritage (strain difference).

References
----------


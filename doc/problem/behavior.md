Project 1: Behavioral Model
===========================

## Statement of Problem:
In order to differentiate mice, we need to create a detailed behavior profile to describe:

1. how they drink, feed or move (locomotion) and
2. how they translate between active state or inactive state.

We have the following key background information from the paper:

>Mouses react differently during Active state and Inactive states and all behavioral record should be classified into 2 mutually exclusive categories, Active States (ASs) and Inactive States (ISs). To designate ISs, we examined all time intervals occurring between movement, feeding, and drinking events while the animal was outside the Home base. Those time intervals exceeding an IS Threshold (IST) duration value were classified as ISs; the set of ASs was then defined as the complement of these ISs. Equivalent mathematically, ASs can also be defined as those intervals resulting from connecting gaps between events outside the Home base of length at most IST; ISs are then defined as the complement of these ASs. (*Active State Organization of Spontaneous Behavior Patterns*, C. Hillar et al.)


## Statement of statistical problems:

The above flowchart shows the key metrics that are required by the study to capture the behavioural profile:

![alt tag](http://cenzhuoyao.com/wp-content/uploads/2016/04/project1_behavior_profile.png)

The main focus is 3 key states of the mice i.e. [_Drinking | Feeding | Locomotion_]

Each of these metrics can be seen visually in the slides referenced below. Each metric is a tree, decomposed into two child node metrics, whereby when the child nodes are multiplied together, they yield the parent metric.

- [_Drinking | Feeding | Locomotion_]
    - AS [_Drinking | Feeding | Locomotion_] Intensity
    - _A note about intensity:_ We are not entirely sure what the Tecott Lab's meaning of "intensity" is. Our current hypothesis is that intensity is defined as quantity over active state time. E.g. for drinking, intensity is the quantity consumed divided by the total amount of time the mouse is in an active state.
        - [_Drinking | Feeding | Locomotion_] Bout Size
            - [_Drinking | Feeding | Locomotion_] Bout Duration
            - [_Drinking | Feeding | Locomotion_] Bout Intensity
                - [_Drinking | Feeding | Locomotion_] Bout EventRate
                - [_Drinking | Feeding | Locomotion_] Event Size
        - [_Drinking | Feeding | Locomotion_] Bout Rt

Additionally the following needs to be calculated for Inactive /Active State:
- AS Probability: the probability of AS among all time period
- AS Duration: the length of time of AS
- AS Rate: the reciprocal of average length of time of AS

## Data Collection:
The data we have:
- the observations of location for each mice, (x, y, t) with \Delta t small.
- the aggregated time bined features about each event and its intensity.

The data we need:
- the observation of consumption size and moving distance with each event.

## Exploratory Analysis
Based on the data requirements being provided, we will need to start plotting the following metrics:

For Event
- Event Consumption or Distance: Already in basic time bin features.
- AS Event Intensity: Already in basic time bin features.
- AS Bout Routine: Use txy_coords within each event intervals to generate the path.
- Event Bout Size or Distance: Use observation of consumption size and moving distance data.
- Event Bout Duration: Use event intervals data.
- Event Bout Intensity: Use Event Consumption or Distance over minute of AS time
- Event Size: Use interval to get the number of event happened in bined time
- Event Bout Rate: Use Event Size over AS time.

For In/Active State:
- AS Probability: Already in basic time bin features.
- AS Duration: Already in basic time bin features.
- AS Rate: Use AS Number over AS Duration.


## Data Requirements Description
The data we have:
- a dataframe of observations of location for each mice, (x, y, t) with \Delta t small.
- The above dataframe with a classification of strain number and mouse number at each time t (if available)

The data we require:
- The above dataframe with AS/ IS properly classified at each point t for each mouse
- The above dataframe with a classification of drinking, feeding and locomotion for each mouse at each time t
- The above dataframe with a classification of consumption size and moving distance with each event at each time t

## Methodology/ Approach Description
We wish to create a single function that should be able to return all of the above metrics as a list:
- Key inputs are:
    - mouse/ strain as string
    - starting time
    - ending time
    - a dictionary containing the rectangular vertices marking the area to restrict the movement to i.e. x_lower, x_upper, y_lower, y_upper.
    - [_Drinking | Feeding | Locomotion_] state specification
- The main output is a list containing the key metrics stated in `Statement of statistical problems` section

- Key idea is that if we have the most granular dataframe in `Data Requirements Description` then the python code is really just a SQL (in `pandas` form) filtering/ grouping query to generate the required output metrics (from flowchart) in the form of a list

## Testing Framework Outline

## Additional Remarks
- It is not clear exactly how the specified required metrics are to be calculated in the form of a single query or multiple queries. We need more clarification on what intensity means.
- Not sure yet whether the required dataframe at the most granular level can be easily constructed. This would be really useful for all projects to use so we should really consider developing it for the wider team.
- Some of the required data metrics like consumption of food/ water at each time t may not be easy to obtain as they are provided for each interval. These may have to be prorated across each time t in some stable way in the construction of the required dataframe
- We also believe that the metrics provided at each point are single point statistics i.e. means. We should consider outputing the actual histogram of values at each point for the given metric rather than just the single-valued mean metrics
    - For example, we may not only be interested in the average amount of active time spent in locomotion, but the distribution of locomotion. This is a more complicated metric than those outlined in the work by the Tecott Lab's papers referenced below. With this information, we could potentially see interesting trends: the proportion of a mouse-day spent in locomotion could be the same in two time chunks, but the types of movements (distances) could form a more nuanced distribution.
- Not sure if this is feasible, but if we had to produce the mean value we could output the time series mean value over the given interval rather than _just_ the overall mean from the given interval

## References

1. http://www.msri.org/people/members/chillar/files/BY/Jarrod_class_slides.pdf
2. http://www.msri.org/people/members/chillar/files/BY/SS1_manu.pdf

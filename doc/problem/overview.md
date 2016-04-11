# Overview

# Table of Contents
1. [Statement of Problem](#statement-of-problem)
<br>1.1 [Project Goal](#project-goal)<br />
1.2 [Computational Ethology](#computational-ethology)
<br>1.3 [Why Mice?](#why-mice)<br />
2. [Methodology Description](#methodology-description)
3. [Statement of Statistical Problems](#statement-of-statistical-problems)
4. [Glossary](#glossary)
5. [References](#references)

<div id='statement-of-problem'/>
## 1. Statement of Problem

<div id='project-goal'/>
### 1.1 Project Goal 

The goal of this project is to explore the effects of genetics on behavior in mice and extrapolate these findings to improve treatment of psychiatric diseases in humans. 

<div id='computational-ethology'/>
### 1.2 Computational Ethology 

[Ethology](#ethology) is the study of animal behavior, and it generally follows one of two approaches. The first approach was developed by B.F. Skinner and relies heavily on laboratory experiments. Skinner postulated that since behavior is predictable, it should be controllable. His most prominent experiment involved training pigeons through [operant conditioning](#operant-conditioning). He found that the pigeons had the ability to learn new behaviors under a reward system. However, the setting of the experiment was incredibly artificial and controlled. In contrast, Konrad Lorenz believed that the only way to truly understand animal behavior is to observe them in their natural context as behavior induced by an artificial environment may not reflect animal behavior in their natural environment. Lorenz's most prominent experiment discovered that a young goose will instinctively bond with the first moving object that it perceives in order to better recognize its own species. This experiment was conducted in a more natural setting to minimize human manipulation. 

This project adopts Lorenz's approach--observing the whole spectrum of animal behavior in their natural state. Previous approaches relied on human observation to score animal behavior. However, slow data collection, low dimensional data, imprecise and subjective measurements, and human visual and language limitations impeded data collection and analysis. Using modern quantitative tools for measurement, description, and analysis, the field of [computational ethology](#computational-ethology1) has emerged to solve these issues. Together, modern mathematics, engineering, and computer science have the potential to establish a causal relationship between genetics and behavior.  

<div id='why-mice'/>
### 1.3 Why Mice? 

Although the human genome was first sequenced over a decade ago, the relationship between genetics and behavior is still not well understood. For ethical reasons, genes cannot be systematically manipulated in humans. Therefore, the familiar scientific testing approach must be edited -- enter mice. There are several reasons the mouse has become the mammal of choice in human behavioral studies. Chief among them is the fact that "approximately 99% of mouse genes have human counterparts--conversely, mouse versions (orthologs) can be identified for 99% of human genes." Additionally, the brain organization and behavioral responses of humans and mice display many similarities. For example, both mammals display complex processes like hunger and fear. This allows scientists to more easily identify and track these behaviors. In addition, the extreme similarities of intra-strain mice, the space efficiency of maintaining their caged environments, and the speed of reproduction make mice a logical alternative to testing on humans. 

<div id='methodology-description'/>
## 2. Methodology Description

The traditional technology to analyze behavior is time-intensive and labor-intensive. For example, recording data requires researchers to track behavior uninterruptedly. This experiment utilized a method for continuous high-resolution behavioral data collection and analysis. The [home cage monitoring (HCM) system](#hcm-system) utilized is a network of photobeam feeding detection, drinking detection, and activity platform sensors that records mouse [active states](#active-state) and [inactive states](#inactive-state) automatically and incessantly over 24-hour periods where 1 hour per day was reserved for HCM maintenance. This facilitates objective, multi-dimensional computer tracking, providing a higher degree of accuracy compared to human observation.

In this project, the HCM system tracked 170 mice, representing 16 [strains](#strain) or approximately 94% of the genome, logging 500,000 behavioral events per mouse per day over 12 days of data collection after 5 days of acclimation. The scope of the study was limited to male mice as females tended to display cyclical changes in behavior. Mice within each strain display strong homogeneity and low variability in genetic composition. This is in part due to high levels of inbreeding which decreases the randomness between individual mouse samples. By studying the behaviors of theses 16 different strains -- each strain with their own unique genetic makeup -- we can begin to understand the importance of genetic makeup on mice behavior. We can then extrapolate to humans thanks to the remarkable genetic similarity between the two species. 

<div id='statement-of-statistical-problems'/>
## 3. Statement of Statistical Problems 

This project utilized sophisticated statistical methods to process data, including machine learning algorithms and statistical inference. The whole project can be divided into 6 sub-projects:

- Project 1: [Behavior Model] (https://github.com/berkeley-stat222/mousestyles/blob/master/doc/problem/behavior.md)
- Project 2: [Exploration and Path Diversity] (https://github.com/berkeley-stat222/mousestyles/blob/master/doc/problem/path.md)
- Project 3: [Dynamics of AS Patterns] (https://github.com/berkeley-stat222/mousestyles/blob/master/doc/problem/dynamics.md)
- Project 4: [Ultradian Analysis] (https://github.com/berkeley-stat222/mousestyles/blob/master/doc/problem/ultradian.md)
- Project 5: [Application of Clustering Analysis] (https://github.com/berkeley-stat222/mousestyles/blob/master/doc/problem/classification.md)
- Project 6: [Power Laws and Universality] (https://github.com/berkeley-stat222/mousestyles/blob/master/doc/problem/distribution.md)

<div id='glossary'/>
## 4. Glossary

- **<a id="active-state">Active State</a> (AS):** The active state in this model is when the mouse is using energy, such as foraging, patrolling, eating, or drinking. Active states are energetically costly and can be dangerous in a natural environment. 
- **<a id="computational-ethology1">Computational Ethology</a>:** The use of mathematics, engineering, and computer science to overcome the difficulties that come from using humans to score animal behavior.
- **<a id="ethology">Ethology</a>:** The study of animal behavior, including the phenomenological, causal, genetic, and evolutionary aspects.
- **<a id="hcm-system">HCM System</a>:** The system used in this experiment to track variables of interest. The HCM System included photobeam sensors at the feeding stations, capacity based sensors at the drinking station, and an activity platform for position detection using an (x,y) system. 
- **<a id="home-environment">Home Environment</a>:** The home environment is the cage of each mouse containing a home base, a food station, and a water station.
- **<a id="inactive-state">Inactive State</a> (IS):** The inactive state in this model is when the mouse is in a state of energy conservation, such as sleeping or resting at the home base.
- **<a id="operant-conditioning">Operant Conditioning</a>:** Altering of behavior through the use of positive reinforcement which is given to the subject after eliciting a desired response. 
- **<a id="phenotype">Phenotype</a>:** The set of observable characteristics of an individual resulting from the interaction of its genotype with the home environment.
- **<a id="strain">Strain</a>:** A strain here is a genetic variant or sub-type of of the more general mouse population.

<div id='references'/>
## 5. References

 - Laurence H Tecott. The genes and brains of mice and men. American Journal of Psychiatry, 2003     
   http://dx.doi.org/10.1176/appi.ajp.160.4.646.
 - David J Anderson and Pietro Perona. Toward a science of computational ethology. Neuron, 84(1):18-31, 2014.   
   http://www.sciencedirect.com/science/article/pii/S0896627314007934.

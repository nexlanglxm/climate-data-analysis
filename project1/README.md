# Project Idea: Simulating high intensity fitness programme workout performance

## Project Outline

- [Introduction](#introduction)
- [Dataset overview](#/project1/project.ipynb)
- [Research and Variable Investigation](/project1/project.ipynb)
- simulation design
- implementation of simulation
- analysis of dataset
- interpretation of results
- conclusion

## Phenomenon

High intensity fitness programme  workout performance; which can be measured in terms of various variables like time taken to complete a workout, number of repetitions completed in a given exercise, heart rate, and perceived workout difficulty.

## Variables

- Time taken to complete workout (continuous variable)
- Number of repetitions (discrete variable)
- Heart rate (continuous variable)
- Subjective difficulty level (ordinal variable)

## Likely Distributions

- Time taken to complete workout might follow a normal distribution
- The number of repetitions..poisson distribution?
- Heart rate.. normal distribution
- Difficulty level should be represented as categorical data

## Relationships

- Time taken and the number of repetitions completed should be negatively correlated, as time decreases, repetitions should increase.
- Heart rate might have a positive correlation with number of repetitions completed, high intensity workouts can lead to higher heart rates.
- Difficulty level vs time taken & heart rate; harder workouts may lead to longer times and higher heart rates.

## Simulation Steps

1. Generate synthetic data for each variable using the appropriate numpy.random distributions
2. Ensure that relationships between variables are reflected in the simulated data.
3. Detail these in the project.ipynb Jupyter Notebook
4. Visualise the synthetic data and the realtionshops using appropriate charts and plots

## Results

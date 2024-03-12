# Functional Fitness Data Modeling using Python

This repository contains a Jupyter notebook focusing on modeling a synthetic dataset representing high-intensity fitness program performance using Python.

## Project Overview

This project aims to simulate a dataset that mirrors real-world phenomena related to high-intensity workout programs. It explores four key variables:

1. Blood lactate concentration
2. Heart rate during the workout
3. Subjective difficulty level experienced during the workout
4. Caloric expenditure

## File Structure

- `project.ipynb`: Jupyter notebook containing the detailed process of dataset simulation, variable investigation, analysis, interpretation, and references.
- `readme.md`: This file, providing an overview of the project, its objectives, and the tools used.
- `.gitignore`: Used to keep the repository tidy, and avoid accidental file upload.

## Project Structure

The `project.ipynb` file within this repository is organized into the following sections, which are stylised using markdown for ease of usage:

- Imports
- Project Brief
- Introduction
- Dataset Overview
- Simulation Steps & Design
- Implementation of Simulation
- Analysis and Insights
- Conclusions
- References

## Tools and Libraries

This project was developed using:

- Visual Studio Code
- Jupyter Notebooks (via Anaconda)
- Python 3.11.5
- Libraries used:
  - Pandas
  - Matplotlib
  - NumPy
  - Seaborn

## Running the Jupyter Notebook

To run the Jupyter Notebook included in this repository, follow these steps:

### Clone the Repository

```bash
git clone https://github.com/nexlanglxm/programming-for-data-analysis.git
```

```bash
cd project1
```

### Install Required Dependencies

Ensure you have Python installed, preferably Python 3.11, along with the necessary libraries. You can install the required libraries using pip:

```bash
pip install pandas matplotlib numpy seaborn
```

### Open the Notebook

Open the Jupyter Notebook using Jupyter Notebook, Jupyter Lab, or Visual Studio Code.

### Execute Cells

Inside the notebook, execute each cell sequentially by clicking on them and pressing `Shift + Enter` to run the code cells.

## Data Generation Methodology

The synthetic dataset was generated following specific distributions for each variable.

- Blood Lactate Concentration (BLC):
  - Description: A continuous variable measuring lactate in the blood during high-intensity workouts.
  - Ranges: Resting blood lactate: Typically up to 2.0 mmol/L; during intense exercise, levels may elevate to 15-25 mmol/L.
  - Simulation: Synthetic data for resting and exercise lactate levels were generated using numpy's random number generation with constrained values to align with realistic physiological levels.

- Heart Rate:
  - Description: A continuous variable reflecting physiological response during workouts.
  - Ranges: Target heart rate zones vary from 70-85% of maximum heart rate for different intensities.
  - Simulation: Synthetic heart rate data was created using numpy's random normal distribution centered around an average of 142 beats per minute.

- Subjective Difficulty Level (SDL):
  - Description: An ordinal variable expressing perceived difficulty levels, which was adapted to be numerical using Borg's Perceived Rate of Exertion.
  - Ranges: Subjective difficulty levels were simulated using numpy's random normal distribution centered around a mean value of 142.
  - CR10 Scaling: Heart rate data was mapped to CR10 scaling categories to simulate subjective difficulty levels based on exercise intensity.

- Caloric Expenditure:
  - Description: A continuous variable measuring energy expended during workouts.
  - Ranges: Caloric expenditure was estimated using Metabolic Equivalent of Task (MET) values for circuit training and an average individual weight of 70 kilograms.
  - Simulation: Synthetic data for caloric expenditure was generated using numpy's random normal distribution with a mean value estimated from the MET values.
  
These methodologies were used to generate synthetic data for the variables, ensuring realistic ranges and distributions aligned with known physiological responses during high-intensity workouts.

## Acknowledgements

References and sources used in this project are cited during and listed in their entireity at the end of the `project.ipynb` file.

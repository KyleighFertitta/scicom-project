# scicom-project
# Final Project for MBIO 691

## Project Overview
This project looks at the relationship between coral cover changes and environmental factors (Sea Surface Temperature (SST) and pH) based on future projections. Using a dataset with environmental variables and coral cover estimates for different climate models, this analysis includes:
- Scatter plots visualizing the relationships between coral cover change and SST/pH changes between models.

## Dataset
The dataset, `coral_forecast.csv`, contains the following columns (per the project instructions written by Noam):

Coral_cover_2020/2100: Simulation estimates of tropical coral cover averaged across 2010-2020, and 2090-2100 respectively (km $^2$).
SST_2020/SST_2100: Mean SST (sea-surface temperature) averaged across 2010-2020, and 2090-2100 respectively (degrees C).
SST_seasonal: Amplitude of the seasonal SST cycle, i.e. difference between summer and winter SST (degrees C).
pH_2020/pH_2100: Mean pH averaged across 2010-2020, and 2090-2100 respectively.
PAR: Benthic Photosynthetically Available Radiation (mol m $^{-2}$ d $^{-1}$ ).
longitude/latitude: Longitude/latitude of the site.
model: Simulation configuration, numbered 0-11.
coral_cover_change: Calculated percentage change in coral cover from 2020 to 2100.
SST_change: Change in SST from 2020 to 2100.
pH_change: Change in pH from 2020 to 2100.

## Figures and Captions
There are three figures with captions explaining the relationship between different variables:

1. **Average Change in Coral Cover Relative to SST Change Per Model**  
   Shows the correlation between SST change and coral cover change, including a trend line and model labels.

2. **Average Change in Coral Cover Relative to pH Change Per Model**  
   Shows the correlation between pH change and coral cover change, including a trend line and model labels.

3. **Average Predicted Change in Coral Cover Per Model**  
   Shows the average coral cover change for each model, indicating any trends.

Each plot is saved as a vector file (SVG format) for high-quality publication use.

## Required Libraries to Load
This project requires following libraries in Python:
- `pandas`: For data manipulation
- `matplotlib`: For plotting
- `seaborn`: For correlation matrix and visualization support
- `numpy`: For trend line calculations

Install the dependencies via pip:
```bash
pip install pandas matplotlib seaborn numpy


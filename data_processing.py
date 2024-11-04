import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Load data
coral = pd.read_csv('coral_forecast.csv')
coral.dtypes

# Calculate percentage change in coral cover
coral['coral_cover_change'] = ((coral['coral_cover_2100'] - coral['coral_cover_2020']) / coral['coral_cover_2020']) * 100


#SST

# Calculate SST change
coral['SST_change'] = coral['SST_2100'] - coral['SST_2020']

# Group by model to get SST and coral change averaged across sites per model
averaged_data = coral.groupby('model')[['coral_cover_change','SST_change']].mean().reset_index()

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(averaged_data['SST_change'], averaged_data['coral_cover_change'], 
         linewidth=2)

# Adding trend line
m, b = np.polyfit(averaged_data['SST_change'], averaged_data['coral_cover_change'], 1)
plt.plot(averaged_data['SST_change'], m*averaged_data['SST_change'] + b, color='red', linestyle='--', linewidth=1)


plt.title('Average Change in Coral Cover Relative to SST Change Per Model')
plt.xlabel('SST Change (°C)')
plt.ylabel('Average Percentage Change in Coral Cover (%)')

# Label points
for i, row in averaged_data.iterrows():
    plt.text(row['SST_change'], row['coral_cover_change'], row['model'], fontsize=9, ha='right', va='bottom')

# Figure Caption
plt.figtext(0.5, -0.1, "Figure 1: Average Change in Coral Cover Relative to SST Change Per Model. "
            "This scatter plot shows average SST change as a function of predicted average coral cover change per model. "
            "The red dashed line indicates the trend across models and shows coral cover decreasing as SST increases.", ha="center", wrap=True)


#Save as a vector file
plt.savefig("coral_cover_vs_sst_change.svg", format="svg")

plt.show()



#PH

# Calculate pH change
coral['pH_change'] = coral['pH_2100'] - coral['pH_2020']

#Group by model to get PH and coral change per model
averaged_data = coral.groupby('model')[['coral_cover_change', 'pH_change']].mean().reset_index()

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(averaged_data['pH_change'], averaged_data['coral_cover_change'], 
         linewidth=2)

# Adding trend line
m, b = np.polyfit(averaged_data['pH_change'], averaged_data['coral_cover_change'], 1)
plt.plot(averaged_data['pH_change'], m*averaged_data['pH_change'] + b, color='red', linestyle='--', linewidth=1)


plt.title('Average Change in Coral Cover Relative to pH Change Per Model')
plt.xlabel('pH Change')
plt.ylabel('Average Percentage Change in Coral Cover (%)')

# Label points
for i, row in averaged_data.iterrows():
    plt.text(row['pH_change'], row['coral_cover_change'], row['model'], fontsize=9, ha='right', va='bottom')

# Figure caption
plt.figtext(0.5, -0.1, "Figure 2: Average Change in Coral Cover Relative to pH Change Per Model. "
            "This plot shows average pH change as a function of average predicted coral cover change, averaged per model. "
            "The red dashed line indicates the trend across models and shows as coral cover decreases pH increases.", ha="center", wrap=True)


#Save as a vector file
plt.savefig("coral_cover_vs_pH_change.svg", format="svg")

plt.show()


#Coral Cover Change

#Group by model, average across sites
averaged_data = coral.groupby('model')[['coral_cover_change']].mean().reset_index()

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(averaged_data['model'], averaged_data['coral_cover_change'], 
         linewidth=2)

# Adding trend line
m, b = np.polyfit(averaged_data['model'], averaged_data['coral_cover_change'], 1)
plt.plot(averaged_data['model'], m*averaged_data['model'] + b, color='red', linestyle='--', linewidth=1)


plt.title('Average Predicted Change in Coral Cover Per model')
plt.xlabel('Model')
plt.ylabel('Average Percentage Change in Coral Cover (%)')

plt.figtext(0.5, -0.1, "Figure 3: Average Predicted Change in Coral Cover Per Model. "
            "This scatter plot shows the average predicted percentage change in coral cover for each climate model. "
            "The red dashed line indicates the trend across models and shows coral cover is decreasing as the model number increases.", ha="center", wrap=True)


#Save as a vector file
plt.savefig("coral_cover_change.svg", format="svg")

plt.show()


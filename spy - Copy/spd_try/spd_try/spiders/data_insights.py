import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt # Importing the required libraries

gdpdata = pd.read_csv("gdp_data.csv") # Reading the data from the csv file
gdp_dataframe = pd.DataFrame(d) # Creating a dataframe from the data    
top10=c.head(10) # Selecting the top 10 countries with highest GDP


plt.figure(figsize=(10, 6))  # Adjust figure size
plot = sns.barplot(x='Country', y='GDP(nominal,2022)', data=top10,hue='Country') # Creating a barplot
plot.set_title('Top 10 GDP of Countries in 2022') # Setting the title of the plot
plt.xticks(rotation=90) # Rotating the x-axis labels






plt.show() # Displaying the plot
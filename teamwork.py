#Ridership code

# import pandas module 
import pandas as pd  
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# making dataframes  
ridership = pd.read_csv("Ridership.csv")  
service = pd.read_csv("AC_Transit_ServicePerformance.csv")
   
# output the dataframe 
print(ridership)
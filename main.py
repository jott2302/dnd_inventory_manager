import os
import pandas as pd


file_path = "C:/Users/julia/Documents/dnd_programme/dnd_inventory.xlsx"
file = "dnd_inventory.xlsx"

dataframe1 = pd.read_excel(file_path)

print(dataframe1)
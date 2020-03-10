import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

file_path = 'google-play-store-apps/googleplaystore.csv'
df = pd.read_csv(file_path)
df = df.filter(items=['Category','Rating','Reviews','Size','Installs','Price','Content Rating','Genres'])
print(df.head())
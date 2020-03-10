import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class preprocessing:
	def __init__(self):
		self.df = self.read_file()
		self.to_categorical('Category')
		self.to_categorical('Content Rating')
		self.to_numerical_size('Size')
		self.to_numerical('Price', ['$'])
		self.to_numerical('Installs', [',','+'])
		print(self.df)
	def read_file(self):
		file_path = 'google-play-store-apps/googleplaystore.csv'
		df = pd.read_csv(file_path)
		df = df.filter(items=['Category','Rating','Reviews','Size','Installs','Price','Content Rating'])
		return df

	def to_categorical(self, col):
		mapping = {}
		count = 0
		for index, row in self.df.iterrows():
			if (row[col] in mapping):
				self.df.at[index, col] = mapping.get(row[col])
				continue
			mapping[row[col]] = count
			self.df.at[index,col] = mapping.get(row[col])
			++count

	def to_numerical(self, col, to_avoid):
		for index, row in self.df.iterrows():
			for avoid in to_avoid:
				self.df.at[index,col] = self.df.at[index,col].replace(avoid,'')
			print(self.df.at[index,col])
			self.df.at[index,col] = float(self.df.at[index,col])

	def to_numerical_size(self, col):
		for index, row in self.df.iterrows():
			if (row[col] == "Varies with device"):
				self.df.at[index,col] = -1
				continue
			if (row[col].count('M') != 0):
				self.df.at[index,col] = 1000 * float(self.df.at[index,col].replace('M',''))
				continue
			if (row[col].count('k') != 0):
				self.df.at[index,col] = float(self.df.at[index,col].replace('k',''))

	def get_df(self):
		return self.df


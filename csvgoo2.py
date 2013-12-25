
import csv
import os
import pprint


'''
This module is a simple utility for working with a single csv file, 
or muttiple csv files in a directory.
You can instantiate a csv file by simply doing 
>>>import csvgoo2
>>> c = CsvFile('sample.csv')    
and then grab the data by doing 
>>>c.fill()

The CsFile object only grabs the data when you explicitly call the fill() method 
in order to save memory.  You can also use the empty() method to clear data once 
its been filled
'''


#CsvFile USAGE
#c = CsvFile('sample.csv')
#print c.columns
#c.fill()


class CsvFile(object):
	def __init__(self, name):
		self.name = name
		self.data = []
		self.columns = []
	def __str__(self):
		return self.name

	def empty(self):
		self.data = []

	def fill(self):
		self.data = [x for x in csv.DictReader(open(self.name, 'rU'))]
		self.columns = self.data[0].keys()


''' 
The Repo class is similar to the csv file object 
but lets you gather all csv files in a directory at once
the get() method just instantiates a CsvFile object. 
'''

class Repo(object):
	def __init__(self, pathdir = '.', fillall = False):
		if not fillall:
			self.items = [CsvFile(f).empty() for f in os.listdir(pathdir) if os.path.isfile(f) and f.lower().endswith('.csv')]
		else:
			self.items = [CsvFile(f) for f in os.listdir(pathdir) if os.path.isfile(f) and f.lower().endswith('.csv')]
	def fill_all(self):
		self.items = [x.fill for x in self.items]
	def get(self, filea):
		return CsvFile(str(filea))

		
# REPO USAGE
#r = Repo()
#g = r.get('sample.csv')
#g.fill()
#print g.data[0]

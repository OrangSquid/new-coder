from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np
from parse import *

def visualize_days():
	"""Visualize data by day of the week"""

	# Grab parsed data
	data_file = parse(MY_FILE, ",")

	# Count each occurrence in each day of the week
	counter = Counter(item["DayOfWeek"] for item in data_file)
	
	# Separate counters
	data_list = [counter["Monday"],
				 counter["Tuesday"],
				 counter["Wednesday"],
				 counter["Thursday"],
				 counter["Friday"],
				 counter["Saturday"],
				 counter["Sunday"]]
	day_tuple = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")

	# Assign y-axis data
	plt.plot(data_list)

	# Assign x-axis data
	plt.xticks(range(len(day_tuple)), day_tuple)

	# Save the plot
	plt.savefig("Days.png")

	# Close
	plt.clf()

def visualize_type():
	"""Visualize data by type"""

	# The same as above
	data_file = parse(MY_FILE, ",")

	counter = Counter(item["Category"] for item in data_file)

	labels = tuple(counter.keys())

	# Set where the labels hit the x-axis
	xlocations = np.arange(len(labels))

	# Width of each bar
	width = 0.5

	# Assign data to a bar plot
	plt.bar(xlocations, counter.values(), width = width)

	# Assign labels and tick location to x-axis
	plt.xticks(xlocations, labels, rotation = 90)

	# Give more room to the labels
	plt.subplots_adjust(bottom = 0.45)

	# Make the graph bigger
	plt.rcParams["figure.figsize"] = 12, 8

	plt.savefig("Type.png")
	plt.clf()

def main():
	visualize_days()
	visualize_type()

if __name__ == "__main__":
	main()

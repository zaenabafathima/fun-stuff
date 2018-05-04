import matplotlib.pyplot as plt
import datetime
import numpy as np

time = []
views = []

def process_file_data(fname):
	fhandle = open(fname, 'rU')
	file_string = fhandle.read()

	# lets split record wise
	file_records = file_string.split('\n')

	# splitting each record into time and views 
	for index, item in enumerate(file_records):
		file_records[index] = file_records[index].split('\t')


	for record in file_records:
		if len(record) == 2: 		# just in case we have some non conforming entries 
			time.append(record[0])
			views.append(int(record[1]))  #converting to int!! Coz 1850000 is less than 75000 in the world of strings (learnt the hard way)

process_file_data('video_stats.txt') #Feb 7
process_file_data('video_stats2.txt') #Feb 8
process_file_data('video_stats3.txt') #Feb 9
process_file_data('video_stats4.txt') #Feb 12
process_file_data('video_stats5.txt') #Feb 13
process_file_data('video_stats6.txt') #Feb 14
print("\n\nThe Time array===>", time)
print("\nThe views array====>", views)


plt.plot(views)
plt.show()
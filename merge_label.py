#! /usr/bin/python3

import os
import sys
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('--data_file', type=str, default='', help='input data file path')
	parser.add_argument('--label_file', type=str, default='', help='input label file path')

	opt = parser.parse_args()
	idf_name = opt.data_file
	ilf_name = opt.label_file

	(path, fname) = os.path.split(idf_name)	
	of_name = 'labeled_' + fname

	data = []
	with open(idf_name, 'rt') as idfs:
		for line in idfs.readlines():
			line = line.strip()
			line = line.strip("\n")
			fields = line.split(" ")
			data.append(fields)

	label = []
	with open(ilf_name, 'rt') as ilfs:
		for line in ilfs.readlines():
			line = line.strip()
			line = line.strip("\n")
			fields = line.split(" ")
			label.append(fields)

	with open(of_name, 'w') as ofs:
		i = 0
		for pt_vec in data:
			data_line = pt_vec[0] + " " + \
						pt_vec[1] + " " + \
						pt_vec[2] + " " + \
						label[i][0] + "\n"
			i += 1
			ofs.write(data_line)
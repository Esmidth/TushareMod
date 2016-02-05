__author__ = 'Esmidth'
import time

import pandas as pd
import tushare as ts

import StringHandler as sh


def write(fileName, id):
	df = ts.get_hist_data(id)  # , start='2000-01-01')
	if type(df) != type(None):
		df = df.sort_index(ascending=True)
		df.to_excel(fileName, sheet_name='Sheet1', index=True, index_label='date', merge_cells=False)
		print("%s Done" % id)
	# return 1
	else:
		print("%s Fail" % id)
	# return 0


def load(fileName):
	return pd.read_excel(fileName, 'Sheet1', index_col='date')


def downloadAll(date):
	# for Windows    path = 'DataBase_' + date.__str__()
	#    for x in sh.lists:
	#        write(path + '/' + x + '.xlsx', x)

	# for Mac#
	path = '/Users/Esmidth/Documents/Github/TushareMod/DataBase' + date.__str__()
	for x in sh.lists:
		write(path + '/' + x + '.xlsx', x)

	print("Download finished")


if __name__ == '__main__':
	print("timer started:%s" % time.clock())
	downloadAll(20160205)
	print("timer ended:%s" % time.clock())

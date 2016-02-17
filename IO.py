__author__ = 'Esmidth'
import time
import tushare as ts
import pandas as pd
import StringHandler as sh


def write(filename, id):
	df = ts.get_hist_data(id)  # , start='2000-01-01')
	if type(df) != type(None):
		df = df.sort_index(ascending=True)
		df.to_excel(filename, sheet_name='Sheet1', index=True, index_label='date', merge_cells=False)
		print("%s Done" % id)
	# return 1
	else:
		print("%s Fail" % id)
	# return 0


def load(filename):
	return pd.read_excel(filename, 'Sheet1', index_col='date')


def downloadAll(date):
	path = 'DataBase_' + date.__str__()
	for x in sh.lists:
		write(path + '\\' + x + '.xlsx', x)
	print("Download finished")


if __name__ == '__main__':
	print("timer started:%ss" % time.clock())
	downloadAll(20160212)
	print("timer ended:%ss" % time.clock())

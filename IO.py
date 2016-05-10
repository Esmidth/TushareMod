__author__ = 'Esmidth'
import time
import tushare as ts
import pandas as pd
import StringHandler as sh
import xlrd
import xlwt


def download(filename, id):
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
	path = '/Users/Esmidth/Documents/Github/TushareMod/DataBase' + date.__str__() + '/'
	for x in sh.lists:
		download(path + x + '.xlsx', x)
	print("Download finished")


def outputToExcel(date, dic, profits):
	fileName = 'Results' + date.__str__() + '.xls'
	wbk = xlwt.Workbook()
	sheet = wbk.add_sheet('Sheet 1', cell_overwrite_ok=True)
	col = 0
	row = 1

	sheet.write(0, 0, 'Stock id')
	sheet.write(0, 1, 'Profit')

	for profit in profits:
		sheet.write(row, col, dic[profit][:6])
		sheet.write(row, col + 1, profit)
		row += 1
	wbk.save(fileName)


def test_output():
	date = 20160412
	dic = {}
	dic[1200] = '600080.xlsx'
	dic[1100] = '600081.xlsx'
	dic[1000] = '600082.xlsx'
	profits = []
	profits.append(1200)
	profits.append(1100)
	profits.append(1000)
	outputToExcel(date=date, dic=dic, profits=profits)


if __name__ == '__main__':
	print("timer started:%ss" % time.clock())
	downloadAll(20160510)
	print("timer ended:%ss" % time.clock())

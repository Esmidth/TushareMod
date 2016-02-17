__author__ = 'Esmidth'

import numpy as np
import talib
import tushare as ts
import IO
import StringHandler as sh
import pandas as pd
import time


def MACDMethod(DataIn):
	"""
	:type DataIn: DataFrame
	:type Output:DataFrame
	"""
	buyIndex = []
	sellIndex = []
	DataOut = talib.abstract.MACD(DataIn, 12, 26, 9, 1)
	# print(output[output > 0][output<0.03]['macdhist'])
	i = 0
	# print(output)
	have = False
	for x in DataOut['macdhist']:
		if have == False and x > 0:
			have = True
			buyIndex.append(i)
		elif have == True and x < 0:
			have = False
			sellIndex.append(i)
		i += 1
	i = 0
	startFund = 100
	for x in sellIndex:
		num = DataIn['close'][sellIndex[i]] - DataIn['close'][buyIndex[i]]
		num = num / DataIn['close'][buyIndex[i]]
		startFund = startFund * (1 + num)
		# print(startFund)
		i += 1
	#   print(startFund)

	purchaseLog(DataIn, buyIndex, sellIndex)
	#   return startFund / 100
	# days = DataIn.index[-1] - DataIn.index[0]
	#   startFund= startFund/100
	# % per day
	return startFund / 100  # / (days.days)


def purchaseLog(inputs, buyIndex, sellIndex):
	i = 0
	for x in sellIndex:
		print("------------------------------------------------------")
		print(inputs.index[buyIndex[i]], inputs['close'][buyIndex[i]])
		print(inputs.index[sellIndex[i]], inputs['close'][sellIndex[i]])
		num = (inputs['close'][sellIndex[i]] - inputs['close'][buyIndex[i]]) * 100 / inputs['close'][buyIndex[i]]
		print("%.3f%%" % num)
		i += 1


def main1():
	files = ['300104', '600080', '600081', '600083', '600084', '600085', '600086']
	for x in files:
		print('----------------------')
		print(x)
		print(MACDMethod(IO.load(x + '.xlsx')))
	#   ori = ori.sort_index(ascending=True)
	# print(ori)
	#  d = MACDMethod(ori)


def main2():
	path = 'DataBase_20151106\\'
	dic = {}
	vals = []
	i = 1
	lenth = len(sh.DataBase20151106)
	for x in sh.DataBase20151106:
		profit = MACDMethod(IO.load(path + x + '.xlsx')) * 100
		dic[profit] = x
		vals.append(profit)
		print("%.2f%%  %s Done\t Profit: %s%%" % (100 * i / lenth, x, profit))
		i += 1
	vals = sorted(vals)
	vals.reverse()
	i = 1
	for x in vals:
		print("#%s\t%s:\t%.2f%%" % (i, dic[x], x))
		i += 1


if __name__ == "__main__":
	date = 20160205
	path = '/Users/Esmidth/Documents/Github/TushareMod/DataBase' + date.__str__() + '/'
	# IO.write('600086.xlsx','600086')
	ori = IO.load(path + '600080.xlsx')
	print(MACDMethod(ori))
	# main2()

	'''
	dic = {}
	dic['123123'] = 123123
	dic['1000'] = 3
	dic['2131231'] = 4
	dic['123123a'] = -12312

	x = sorted(dic.values())
	x.reverse()
	print(x)
	for y in x:
		print(dic[y],y)
	df = IO.load(path+'600080'+'.xlsx')
	print(type(df.index[1]))
	print(df.index[0])
	dd = time.strftime(df.index[0],'%Y-%m-%d')
	print(type(dd))
	'''

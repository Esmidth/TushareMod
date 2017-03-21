__author__ = 'Esmidth'

import numpy as np
import talib
import tushare as ts
import os
import IOput
import StringHandler as sh
import pandas as pd
import time


def MACDMethod(DataIn):
    DataIn = DataIn.sort_index(ascending=True)  # Must Sort Raw Data First Or Calculate in a reserved index
    Log = False
    """
    :type DataIn: DataFrame
    :type Output:DataFrame
    """
    buyLog = []
    sellLog = []
    DataOut = talib.abstract.MACD(DataIn, 12, 26, 9, 1)
    # print(output[output > 0][output<0.03]['macdhist'])
    i = 0
    # print(output)
    have = False
    for x in DataOut['macdhist']:
        if have == False and x > 0:
            have = True
            buyLog.append(i)
        elif have == True and x < 0:
            have = False
            sellLog.append(i)
        i += 1
    i = 0
    startFund = 100
    for x in sellLog:
        num = DataIn['close'][sellLog[i]] - DataIn['close'][buyLog[i]]
        num = num / DataIn['close'][buyLog[i]]
        startFund = startFund * (1 + num)
        # print(startFund)
        i += 1
    # print(startFund)

    if Log:
        purchaseLog(DataIn, DataOut, buyLog, sellLog)
    return startFund / 100


# days = DataIn.index[-1] - DataIn.index[0]
# startFund= startFund/100
# % per day
# return startFund / 100  # / (days.days)


def purchaseLog(inputs, outputs, buyLog, sellLog):
    i = 0
    for x in sellLog:
        print("------------------------------------------------------")
        print("Buy: \t", inputs.index[buyLog[i]], inputs['close'][buyLog[i]])
        print("Sell: \t", inputs.index[sellLog[i]], inputs['close'][sellLog[i]])
        num = (inputs['close'][sellLog[i]] - inputs['close'][buyLog[i]]) * 100 / inputs['close'][buyLog[i]]
        print("%.3f%%" % num)
        i += 1


def main1():
    files = ['300104', '600080', '600081', '600083', '600084', '600085', '600086']
    for x in files:
        print('----------------------')
        print(x)
        print(MACDMethod(IOput.load(x + '.xlsx')))
        #   ori = ori.sort_index(ascending=True)
        # print(ori)
        #  d = MACDMethod(ori)


def testAll(date):
    path = 'DataBase' + date.__str__() + '/'
    files = os.listdir(path)
    dic = {}
    profits = []
    idd = 1
    # lenth = len(sh.DataBase20151106)
    length = len(files)
    '''
    for x in sh.DataBase20151106:
        profit = MACDMethod(IO.load(path + x + '.xlsx')) * 100
        dic[profit] = x
        vals.append(profit)
        print("%.2f%%  %s Done\t Profit: %s%%" % (100 * i / lenth, x, profit))
        i += 1
     '''

    for file in files:
        profit = MACDMethod(IOput.load(path + file)) * 100
        dic[profit] = file
        profits.append(profit)
        print("%.2f%%  %s Done\t Profit: %s%%" % (100 * idd / length, file, profit))
        idd += 1
    profits = sorted(profits)
    profits.reverse()
    idd = 1
    for profit in profits:
        print("#%s\t%s:\t%.2f%%" % (idd, dic[profit], profit))
        idd += 1
    IOput.outputToExcel('2016_04_12', dic, profits)


if __name__ == "__main__":
    '''
    path = 'DataBase_20151106\\'
    # IO.write('600086.xlsx','600086')
    # ori = IO.load(path + '600080.xlsx')
    ori = ts.get_hist_data('600080')
    print(MACDMethod(ori))
    '''
    testAll(date=20170321)

    # path = './DataBase20160510/'
    # file = '600080.xlsx'
    # ori = IO.load(path + file)
    # ori = ts.get_hist_data('600080',start='2016-01-01')
    # ori = ori.sort_index(ascending=True)
    #print(MACDMethod(ori))
    '''

    dic = {}
    dic['123123'] = 123123
    dic['1000'] = 3
    dic['2131231'] = 4
    dic['123123a'] = -12312
'''
    '''
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

import talib
import tushare as ts
import pandas as pd
import MACD
import Download
import os


def RSI6(DataIn):
    '''
    :param DataIn: pandas.DataFrame
    :return: int
    When RSI6 <= 20, buy in
    When RSI6 >= 80, sell out
    '''
    DataIn = DataIn.sort_index(ascending=True)
    RSI6 = talib.abstract.RSI(DataIn, 6)
    buyIndex = []
    sellIndex = []
    i = 0
    have = False

    for x in RSI6:
        if x <= 20 and have == False:
            buyIndex.append(i)
            have = True
        elif x >= 80 and have == True:
            sellIndex.append(i)
            have = False
        i += 1
    i = 0
    startFund = 100
    for x in sellIndex:
        num = DataIn['close'][sellIndex[i]] - DataIn['close'][buyIndex[i]]
        num = num / DataIn['close'][buyIndex[i]]
        startFund = startFund * (1 + num)
        i += 1
    # MACD.purchaseLog(inputs=DataIn, buyIndex=buyIndex, sellIndex=sellIndex)
    return startFund / 100


def main():
    date = 20160212
    #   for mac
    #    path = '/Users/Esmidth/Documents/Github/TushareMod/DataBase' + date.__str__() + '/'

    path = 'DataBase_' + date.__str__() + '\\'

    dic = {}
    vals = []
    i = 1
    files = os.listdir(path)
    lenth = len(files)
    for x in files:
        profit = RSI6(Download.load(path + x)) * 100
        dic[profit] = x
        vals.append(profit)
        print("%.2f%%   %s  Done\t Profit: %s%%" % (100 * i / lenth, x, profit))
        i += 1
    vals = sorted(vals)
    vals.reverse()
    i = 1
    for x in vals:
        print("#%s\t%s:\t%.2f%%" % (i, dic[x], x))
        i += 1


if __name__ == "__main__":
    '''
    date = 20160205
    path = '/Users/Esmidth/Documents/Github/TushareMod/DataBase' + date.__str__() + '/'
    ori = IO.load(path + '600080.xlsx')
    print(RSI6(ori))
    '''
    main()

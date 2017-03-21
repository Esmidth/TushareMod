import tushare as ts
import pandas as pd
import talib as ta
import IOput


def BOLL(DataIn):
    """
    :param DataIn: DataFrame
    :param Output: DataFrame
    :return:
    """
    """
        Parameters:
            timeperiod: 5
            nbdevup: 2
            nbdevdn: 2
            matype: 0 (Simple Moving Average)
        Outputs:
            upperband
            middleband
            lowerband
    """
    buyIndex = []
    sellIndex = []
    DataOut = ta.abstract.BBANDS(DataIn, 20, 2)
    #    DataOut = ta.abstract.BBANDS()
    return DataOut


if __name__ == "__main__":
    path = 'DataBase_20151106\\'
    ori = IOput.load(path + '600080.xlsx')
    print(BOLL(ori))

__author__ = 'Esmidth'

import tushare as ts
import pandas as pd
import StringHandler as sh


def write(fileName, id):
    df = ts.get_hist_data(id, start='2000-01-01')
    if type(df) != type(None):
        df = df.sort_index(ascending=True)
        df.to_excel(fileName, sheet_name='Sheet1', index=True, index_label='date', merge_cells=False)
        return 1
    else:
        return 0


def load(fileName):
    return pd.read_excel(fileName, 'Sheet1', index_col='date')


def downloadAll(date):
    path = 'DataBase_' + date.__str__()
    for x in sh.lists:
        if write(path + '\\' + x + '.xlsx', x) == 1:
            print("%s Done" % x)
        else:
            print("%s Fail" % x)
    print("Download finished")


if __name__ == '__main__':
    downloadAll(20151106)

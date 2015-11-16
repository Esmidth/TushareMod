__author__ = 'Esmidth'

import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCE'))

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=range(4), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': 'foo'
})
x = list('abcdef')

if __name__ == "__main__":
    #   print(df.head())
    #   print(df.tail(3))
    #   print(df.index)
    #   print(df.columns)
    #   print(df.values)  df.values is a binary array
    #   print(df)
    #   print(df.describe()) Describe shows a quick statistic summary of your data
    #   print(df.T) #Transposing your data 转置
    #   print(df)
    #   print(df.sort_index(axis=1,ascending=False))
    #   print(df.sort_index(axis = 0,ascending=False)) #ascending n.上升的
    #   print(df['A'])
    #   print(df[0:3])  #rows
    #   print(df['20130102':'20130104'])
    #   print(df)
    #   print(df.loc[dates[0]])
    #   print(df.loc[:,['A']]) #loc[rows,column]
    #   print(df.iloc[:,3])     #iloc[rows,colum]
    #   print(df.iloc[[1,2,4],[0,2]])
    #   print(df.iloc[1:3,:])
    #    print(df.iloc[1,1])
    #   print(df.iat[1,1])
    #   print(x[4:10])
    print(df[df > 0])

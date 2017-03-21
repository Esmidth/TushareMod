# Tushare Mod
#####_Modified by Esmidth_



---
##Dependency
 - Tushare
 - Anaconda
 - talib

---
##Content

 - MACD
 - BOLL (#Ongoing)
 - RSI  (#Ongoing)
 - IO
 - MTIO (Multi IO)
 - MultiThread (Multi Thread)
 - StringHandler (Original)

----------

###IOput

 - download (filename,id)
 - load (filename)
 - load_chosen_stocks(filename)
 - outputToExcel (date,dic,profits)
 - downloadAll (date)



----------
### MTIO (#~ing)
##### _using Multi Thread_

 - multi_download(date)
 - main_test()


----------
###MACD

 - MACDMethod(DataIn:DataFrame)
 - purchaseLog(inputs,outputs,buyLog,sellLog)
    - inputs,outputs -> DataFrame
    - buyLog,sellLog -> Array
 - testAll()


----------
###StringHandler

 - All Stock IDs


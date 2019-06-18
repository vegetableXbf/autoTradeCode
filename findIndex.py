import pandas as pd
stockLst = pd.read_csv('I:/fInance/data/intitial/stocksHS300.csv',index_col=0,encoding='gbk')
stockLst = list(stockLst.index)
factorLst = pd.read_csv('I:/fInance/data/intitial/allFactors.csv',encoding='gbk')
factorLst = list(factorLst['factor'])
print(stockLst.index("601828.XSHG"))
print(factorLst.index("liquidity"))
print(stockLst[249])
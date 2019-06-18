import pandas as pd
panfu = 'E'
stockLst = pd.read_csv(panfu+':/fInance/data/intitial/stocksHS300.csv',index_col=0,encoding='gbk')
stockLst = list(stockLst.index)
factorLst = pd.read_csv(panfu+':/fInance/data/intitial/allFactors.csv',encoding='gbk')
factorLst = list(factorLst['factor'])
factordfLst = []
for j in factorLst:
    dfLst = []
    for i in stockLst:
        path = panfu + ':/fInance/data/getData/' + j + '_' + i + '_2018.csv'
        df = pd.read_csv(path)
        dfLst.append(df)
    factordf = pd.concat(dfLst, axis=0, ignore_index=True)
    factordfLst.append(factordf)
dataAll = factordfLst[0]
for i in factordfLst[1:]:
    dataAll = pd.merge(dataAll,i,on=['date','code'])
path = panfu + ':/fInance/data/factordata/initial_factordata_2018.csv'
dataAll.to_csv(path,index=0)
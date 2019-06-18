from jqdatasdk import *
import pandas as pd
phoneLst = [18280081014,18982286061,17738727193,13881855494,17740960969,19983140329,17740961686,17738725085,15802849363,18992352316,15683052529,17740960539]
index = 1
auth(str(phoneLst[index]),'123456')
stockLst = pd.read_csv('I:/fInance/data/intitial/stocksHS300.csv',index_col=0,encoding='gbk')
stockLst = list(stockLst.index)
factorLst = pd.read_csv('I:/fInance/data/intitial/allFactors.csv',encoding='gbk')
factorLst = list(factorLst['factor'])
for i in stockLst[270:]:
    for j in factorLst:
        factor = get_factor_values(i, j, '2018-01-01', '2019-01-01')
        for k in factor.keys():
            df = factor[k].copy()
            code = df.columns.tolist()[0]
            df = df.reset_index()
            df = df.rename(columns={"index": "date", code: k})
            df['code'] = code
            path = 'I:/fInance/data/getData/'+k+'_'+code+'_2018.csv'
            df.to_csv(path,index=0)
        if get_query_count()['spare']<300:
            index = index+1
            auth(str(phoneLst[index]), '123456')
            print(j)
            print(i)
            break
    print(stockLst.index(i))
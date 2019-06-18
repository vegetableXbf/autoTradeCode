import pandas as pd
Lst = []
stockLst = pd.read_csv('I:/fInance/data/intitial/stocksHS300.csv',index_col=0,encoding='gbk')
stockLst = list(stockLst.index)
factorLst = pd.read_csv('I:/fInance/data/intitial/allFactors.csv',encoding='gbk')
factorLst = list(factorLst['factor'])
for i in stockLst:
    for j in factorLst:
        path = 'I:/fInance/data/getData/' + j + '_' + i + '_2018.csv'
        try:
            fh = open(path, "r")
            fh.close()
        except IOError:
            Lst.append([i,j])
print(Lst)
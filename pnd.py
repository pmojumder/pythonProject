import pandas as pd

df1=pd.DataFrame({'Id':[1,2,3],
                  'Name':['Alice','Bob','Charlie']
                  })

df2=pd.DataFrame({'Id':[3,4,5],
                'Name':['Alice','man','chan']
})

#df3=df1.compare(df2)
df3=pd.merge(df1,df2,on='Id',how='right')
print (df3)
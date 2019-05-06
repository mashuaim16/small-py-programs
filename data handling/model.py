import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('file:/Users/Brian/Desktop/jester-data-1.xls',header=None)

df.insert(loc=0, column='idn', value=(np.arange(len(df))))
df['idn'] = df['idn'].apply(lambda x: "user " + str(x))



#以IDN为INDEX, 排序这个dataset
df.set_index('idn', inplace = True)

#drop第一列（joke rated counts for the users）
df.drop(columns=[0],inplace=True)

# to replace all values in a dataframe (replace 99 with 0)
df.replace(99.00, 0, inplace=True)

col_list = list(df)
df['sum']=df[col_list].sum(axis=1)

df['mean']=df[col_list].mean(axis=1)

#在 DATASET底部加上MEAN OR SUM 等等
df = df.append(df.agg(['mean']))

# in two decimal format
print (df.round(2))

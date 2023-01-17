import pandas as pd

df = pd.DataFrame(data=[[1,.51,0,.8,1,.29],[0,.51,0,.8,1,.29],[0,.51,1,.8,0,.29]],
                  columns=['r1','r1_weight','r2','r2_weight','r3','r3_weight'])

list_rules = ['r1', 'r2', 'r3']
list_weights = ['r1_weight', 'r2_weight', 'r3_weight']

dict = zip(list_rules,list_weights)

for rule, weight in dict:
    df[rule+'_result'] = df[rule] * df[weight]

print(df)

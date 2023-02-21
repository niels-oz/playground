import pandas as pd

df = pd.DataFrame(data=[[1,0,1],[0,0,1],[0,1,0]],
                  columns=['r1','r2','r3'])

list_rules = ['r1', 'r2', 'r3']

dict_weights = {
    'r1_weight': 0.51,
    'r2_weight': 0.8,
    'r3_weight': 0.29
}

df['result'] = 0

for rule in list_rules:
    df['result'] += df[rule].multiply(dict_weights.get(rule+'_weight'))

print(df)

# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
print(p_a)
p_b = df[df['purpose'] == 'debt_consolidation'].shape[0]/df.shape[0]
print(p_b)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = df1[df1['fico'].astype(float) >700].shape[0]/df1.shape[0]
print(p_a_b)

p_b_a=(p_a_b * p_a)/p_b
result=p_b_a==p_a
result
# code ends herp_ae


# --------------
# code starts here
prob_lp = len(df[df['paid.back.loan']=='Yes'])/df.shape[0]

prob_cs = len(df[df['credit.policy']=='Yes'])/df.shape[0]

new_df = df[df['paid.back.loan']=='Yes']

tot = len(new_df)

prob_pd_cs = len(new_df[(new_df['paid.back.loan']=='Yes') & (new_df['credit.policy']=='Yes')])/tot

bayes = (prob_pd_cs*prob_lp)/prob_cs

# code ends here


# --------------
# code starts here
data=df['purpose'].value_counts()
data.plot(kind='bar')
df1=df[df['paid.back.loan']=='No']
df1.plot(kind='bar')


# code ends here


# --------------
# code starts here

inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
plt.hist(df['installment'])
plt.hist(df['log.annual.inc'])


# code ends here



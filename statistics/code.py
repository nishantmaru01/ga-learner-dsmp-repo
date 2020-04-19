# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind="bar")



# --------------
#Code starts here
plt.figure(figsize=(7,7))
alignment = data['Alignment'].value_counts()
plt.title("Character Alignment")
alignment.plot.pie()
plt.show()


# --------------
#Code starts here
from numpy import cov
from scipy.stats import pearsonr

sc_df = data[['Strength','Combat']]
sc_covariance = round(cov(sc_df['Strength'],sc_df['Combat'])[0,1],2)
print(sc_covariance)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
sc_pearson, _ = pearsonr(sc_df['Strength'],sc_df['Combat'])
print('sc_df Pearsons correlation: %.2f' % sc_pearson)

ic_df = data[['Intelligence','Combat']]
ic_covariance = round(cov(ic_df['Intelligence'],ic_df['Combat'])[0,1],2)
print(ic_covariance)
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
ic_pearson, _ = pearsonr(ic_df['Intelligence'],ic_df['Combat'])
print('ic_df Pearsons correlation: %.2f' % ic_pearson)



# --------------
#Code starts here
total_high = round(data['Total'].quantile(.99),2)
super_best = data[data['Total']>total_high]
super_best_names = super_best['Name'].values.tolist()
print(super_best_names)


# --------------
#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3)
ax_1.boxplot(super_best['Intelligence'])
ax_1.set_title("Intelligence")
ax_2.boxplot(super_best['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(super_best['Power'])
ax_3.set_title('Power')
plt.show()



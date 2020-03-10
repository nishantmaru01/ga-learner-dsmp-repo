# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
data = pd.read_csv(path)
#Sample_Size
sample_size=2000
sample_size=2000
data_sample = data.sample(n=sample_size, random_state=0)
sample_mean = data_sample['installment'].mean()
sample_std = data_sample['installment'].std()
#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))
confidence_interval=(round(sample_mean-margin_of_error,2),round(sample_mean+margin_of_error,2))
# path        [File location variable]
true_mean = data['installment'].mean()
print(true_mean)
#Code starts here



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])
#fig, axes = plt.subplot(nrows = 3 , ncols = 1)
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        mean=data['installment'].sample(sample_size[i]).mean()
        m.append(mean)
    mean_series=pd.Series(m)
    plt.hist(mean_series)
    plt.show()

#Code starts here



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest
data['int.rate'] = data['int.rate'].map(lambda x: str(x)[:-1])
data['int.rate'] = data['int.rate'].astype(float)/100
#Code starts here

# apply ztest 
z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')

# print z statistic and p value
print('z_statistic : ',z_statistic)
print('p_value : ',p_value)

# check the p-value
inference=''
if(p_value<0.05):
    inference = 'Accept'
else:
    inference = 'Reject'
print(inference)



# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])

# print z statistic and p value
print('z_statistic : ',z_statistic)
print('p_value : ',p_value)

# check the p-value
inference=''
if(p_value<5):
    inference = 'Accept'
else:
    inference = 'Reject'
print(inference)


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
print(yes)
no = data[data['paid.back.loan']=='No']['purpose'].value_counts()
print(no)
observed = pd.concat([yes.transpose(),no.transpose()],axis=1,keys=['Yes','No'])
chi2, p, dof, ex = stats.chi2_contingency(observed)
print("Chi-square statistic = ",chi2)
print("p-value = ",p)



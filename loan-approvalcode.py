# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.DataFrame(pd.read_csv(path))
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var.head(2))
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var.head(2))

# code ends here


# --------------
# code starts here
bank.drop(['Loan_ID'],inplace=True,axis=1)
banks = pd.DataFrame(bank)
#print(banks.head(2))
bank_mode = banks.mode().iloc[0]
print(bank_mode.head(2))
banks.fillna(bank_mode, inplace=True)

#code ends here




# --------------
# Code starts here

avg_loan_amount = pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc='mean')

print(avg_loan_amount)
# code ends here



# --------------
# code starts here
loan_approved_se = len(banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)
loan_approved_nse = len(banks[(banks['Self_Employed']=='No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_nse)

percentage_se = (loan_approved_se/614)*100
print(percentage_se)
percentage_nse = (loan_approved_nse/614)*100
print(percentage_nse)
# code ends here


# --------------
# code starts here

loan_term = banks.apply(lambda x: x['Loan_Amount_Term']/12,axis=1)

big_loan_term = 0
for x in loan_term:
    if x>=25:
        big_loan_term += 1
print(loan_term.value_counts())
print(big_loan_term)
#print(big_loan_term)

# code ends here


# --------------
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)
print(banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History'].agg('mean'))



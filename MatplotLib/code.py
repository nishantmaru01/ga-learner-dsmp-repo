# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data =  pd.read_csv(path)

loan_status = data['Loan_Status'].value_counts()
print(loan_status)
loan_status.plot(kind="bar")
#Code starts here


# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
print(property_and_loan)

property_and_loan.plot.bar(stacked = False,figsize=(10,7))
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot.bar(stacked = True,figsize=(10,7))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()


# --------------
#Code starts here
graduate = pd.DataFrame(data[data['Education'] == 'Graduate'])
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate = pd.DataFrame(data[data['Education'] == 'Not Graduate'])
print(not_graduate)
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')









#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig ,(ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
data['TotalIncome'] = data['ApplicantIncome'] +data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])



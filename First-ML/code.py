# --------------
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
# code starts here
df = pd.read_csv(path)
df.head(5)
y = df['list_price']
X = df.drop('list_price',axis=1)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 6)
# code ends here



# --------------
import matplotlib.pyplot as plt

# code starts here        
cols=X_train.columns
fig ,axes=plt.subplots(3,3)
for i in range(3):
    for j in range(3):
        col=cols[i * 3 + j]
        axes[i,j].scatter(X_train[col],y_train)
plt.show()
# code ends here



# --------------
# Code starts here
corr=X_train.corr(method="pearson")
# if corr > 0.75 | corr > -0.75:
#     Print(corr)
print(corr)
X_train.drop(['play_star_rating','val_star_rating'],inplace=True,axis=1)
X_test.drop(['play_star_rating','val_star_rating'],inplace=True,axis=1)


# Code ends here


# --------------
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Code starts here
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pred=regressor.predict(X_test)
mse=mean_squared_error(y_pred,y_test)
r2=r2_score(y_test,y_pred)
# Code ends here


# --------------
# Code starts here


residual=y_test - y_pred
residual.hist()

# Code ends here



# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data=pd.read_csv(path)
data['Rating'].hist()
data=data[data['Rating']<=5]

#Code ends here


# --------------
# code starts here
total_null=data.isnull().sum()
percent_null=(total_null/data.isnull().count())*100
missing_data=pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)
data=data.dropna()
total_null_1=data.isnull().sum()
percent_null_1=(total_null/data.isnull().count())*100
missing_data_1=pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)

# code ends here


# --------------

#Code starts here
sns.catplot(x="Category", y="Rating",kind="box", data=data,height=10)
plt.title('Rating vs Category [BoxPlot]')
plt.xticks(rotation=90)


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)


# --------------
#Code starts here

data['Price'].value_counts()
data['Price']=data['Price'].str.replace("$","")
data['Price']=data['Price'].astype(float)
sns.regplot(x="Price",y="Rating",data=data)
plt.title("Rating vs Price [RegPlot]")

#Code ends here


# --------------

#Code starts here

data['Genres'].unique()
data['Genres']=data['Genres'].str.split(";").str[0]
gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()
gr_mean.describe()
gr_mean=gr_mean.sort_values('Rating')


#Code ends here


# --------------

#Code starts here

data['Last Updated']=pd.to_datetime(data['Last Updated'])
max_date=data['Last Updated'].max()
Diff_dates=(pd.to_datetime(max_date)-data['Last Updated'])
data['Last Updated Days']=Diff_dates.dt.days
sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
data['Last Updated Days']


#Code ends here



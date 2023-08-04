import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
import pickle


df = pd.read_csv('./data/_output.csv')

# reorder columns
columns = ['id', 'postalCode', 'province', 'locality', 'type of property', 'subtype of property', 'type of sale', 'state of the building',
           'number of facades', 'number of bedrooms', 'fully equipped kitchen', 'furnished', 'open fire', 'terrace', 'garden', 'swimming pool',
           'terrace area', 'garden area', 'living area', 'total property area', 'total land area', 'price']
df = df[columns]

# convert to desired type
    # for boolean:
        # contvert to string
        # with a lambda function, check if value is equal to 'True', 'true', or '1' and return True or False
        # convert to integer
df['id'] = df['id'].astype(int)
df['postalCode'] = df['postalCode'].astype(int)
df['province'] = df['province'].astype(str)
df['locality'] = df['locality'].astype(str)
df['type of property'] = df['type of property'].astype(str)
df['subtype of property'] = df['subtype of property'].astype(str)
df['type of sale'] = df['type of sale'].astype(str)
df['state of the building'] = df['state of the building'].astype(str)
df['number of facades'] = df['number of facades'].astype(int)
df['number of bedrooms'] = df['number of bedrooms'].astype(int)
df['fully equipped kitchen'] = df['fully equipped kitchen'].astype(str)
df['furnished'] = df['furnished'].astype(str).apply(lambda x: int(x.lower() == 'true' or x.lower() == '1'))
df['open fire'] = df['open fire'].astype(str).apply(lambda x: int(x.lower() == 'true' or x.lower() == '1'))
df['terrace'] = df['terrace'].astype(str).apply(lambda x: int(x.lower() == 'true' or x.lower() == '1'))
df['garden'] = df['garden'].astype(str).apply(lambda x: int(x.lower() == 'true' or x.lower() == '1'))
df['swimming pool'] = df['swimming pool'].astype(str).apply(lambda x: int(x.lower() == 'true' or x.lower() == '1'))
df['terrace area'] = df['terrace area'].astype(int)
df['garden area'] = df['garden area'].astype(int)
df['living area'] = df['living area'].astype(int)
df['total property area'] = df['total property area'].astype(int)
df['total land area'] = df['total land area'].astype(int)
df['price'] = df['price'].astype(int)

# drop duplicates
df = df.drop_duplicates()

for column in columns:
    # check if values are string
    if df[column].dtype == 'object':
         # remove leading and trailing spaces
        df[column] = df[column].str.strip()

# exclude rows where province is '0'
df = df[df['province'] != '0']

# exclude rows where total property area is '0'
df = df[df['total property area'] != 0]


# add provinces binary dummies to df
province_binary= pd.get_dummies(df['province']).astype(int)
df = pd.concat([df, province_binary], axis = 1)

# add subtype binary dummies to df
subtype_binary= pd.get_dummies(df['subtype of property']).astype(int)
df = pd.concat([df, subtype_binary], axis = 1)

# convert state of the building to binary
df['state of the building'] = np.where(df['state of the building'].isin(['just_renovated', 'as_new', 'good']), 1, 0)
    # =df['state of the building'].isin(['just_renovated', 'as_new', 'good']).astype(int)
features = ['total property area','state of the building','number of facades','number of bedrooms','Antwerp','Brussels','East Flanders',
            'Flemish Brabant','Walloon Brabant','Hainaut','Limburg','Liège','Luxembourg','Namur','West Flanders','APARTMENT','APARTMENT_BLOCK',
            'BUNGALOW','CASTLE','CHALET','COUNTRY_COTTAGE','DUPLEX','EXCEPTIONAL_PROPERTY','FARMHOUSE','FLAT_STUDIO','GROUND_FLOOR','HOUSE','KOT',
            'LOFT','MANOR_HOUSE','MANSION','MIXED_USE_BUILDING','OTHER_PROPERTY','PENTHOUSE','SERVICE_FLAT','TOWN_HOUSE','TRIPLEX','VILLA',
            'furnished','open fire','terrace','garden','swimming pool']

### Decisiontree model

regressor = DecisionTreeRegressor(criterion='squared_error',max_depth=100,min_samples_split=5,random_state=5)

X = df[features].values
y = df['price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
regressor.fit(X_train,y_train)

# save model
pickle_out = open("decision_tree.pickle", "wb") # save model in binary (wb: write binary)
pickle.dump(regressor, pickle_out)
pickle_out.close()
#loaded_model = pickle.load(open("decision_tree.pickle", "rb")) # load model in python (rb: read binary)
#y_predicted = loaded_model.predict(X)

# test model
y_pred = regressor.predict(X_test)

from sklearn.metrics import mean_squared_error
print('mse: ' +str(np.sqrt(mean_squared_error(y_test,y_pred))))

from sklearn.model_selection import cross_val_score
print(cross_val_score(regressor,X_train,y_train,cv=10))

# plt.scatter(y_test,y_pred)
# plt.xlabel('test values')
# plt.ylabel('predicted values')
# plt.title('Model Accuracy')
# plt.show()

r2_score_value = r2_score(y_test, y_pred)
print("R² score:", r2_score_value)



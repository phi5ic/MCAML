
import matplotlib.pyplot as pt
import pandas as pd
weather = pd.read_csv("weather.csv", index_col="DATE")
print(weather)
weather.apply(pd.isnull).sum()/weather.shape[0] #calcutes the %of the missing values in each columns of the dataframe.
core_weather = weather[["PRCP", "SNOW", "SNWD", "TMAX", "TMIN"]].copy()
core_weather.columns = ["precip", "snow", "snow_depth", "temp_max", "temp_min"]
core_weather.apply(pd.isnull).sum() #calculates the % of the missing values in each columns of the core_weather
core_weather["snow"].value_counts()
core_weather["snow_depth"].value_counts()
del core_weather["snow"]
del core_weather["snow_depth"] #deletes snow and snow_depth columns from the core_weather
print(core_weather[pd.isnull(core_weather["precip"])]) #rows of core_weather that contains missing values for percipi
print(core_weather.loc["2013-12-15",:])
core_weather["precip"].value_counts() / core_weather.shape[0]#% of empty rows
core_weather["precip"] = core_weather["precip"].fillna(0)#replaces the columns with value 0
core_weather.apply(pd.isnull).sum()#calculates the rest of the missing values
print(core_weather[pd.isnull(core_weather["temp_min"])])# tempmin condition
print(core_weather.loc["2011-12-18":"2011-12-28"])
core_weather = core_weather.fillna(method="ffill") # ffill uses the values of the previous row percipi to replace the missing values
core_weather.apply(pd.isnull).sum()#rechecking whether there is any more missing values
# Check for missing value defined in data documentation
core_weather.apply(lambda x: (x == 9999).sum())
print(core_weather.index)
core_weather.index = pd.to_datetime(core_weather.index)# datetime64 to datetime type
core_weather["target"] = core_weather.shift(-1)["temp_max"]#target is a new column contining the max temp for 1 day in the future
print(core_weather)
core_weather = core_weather.iloc[:-1,:].copy()#last row doesnt have a corresponding row for max temperature 1 day in the future
print(core_weather)
from sklearn.linear_model import Ridge

reg = Ridge(alpha=.1)
predictors = ["precip", "temp_max", "temp_min"]
train = core_weather.loc[:"2020-12-31"]
test = core_weather.loc["2021-01-01":]
print(train)
reg.fit(train[predictors], train["target"])
predictions = reg.predict(test[predictors])
from sklearn.metrics import mean_squared_error

mean_squared_error(test["target"], predictions)
combined = pd.concat([test["target"], pd.Series(predictions, index=test.index)], axis=1)
combined.columns = ["actual", "predictions"]
core_weather["month_max"] = core_weather["temp_max"].rolling(30).mean()

core_weather["month_day_max"] = core_weather["month_max"] / core_weather["temp_max"]

core_weather["max_min"] = core_weather["temp_max"] / core_weather["temp_min"]
core_weather = core_weather.iloc[30:,:].copy()
def create_predictions(predictors, core_weather, reg):
    train = core_weather.loc[:"2020-12-31"]
    test = core_weather.loc["2021-01-01":]
    reg.fit(train[predictors], train["target"])
    predictions = reg.predict(test[predictors])
    error = mean_squared_error(test["target"], predictions)

    combined = pd.concat([test["target"], pd.Series(predictions, index=test.index)], axis=1)
    combined.columns = ["actual", "predictions"]
    return error, combined


predictors1 = ["precip", "month_day_max", "max_min"]
predictors2 = ["temp_max", "temp_min", "month_day_max", "max_min"]
print()
print()
print()
print()
print("select any of the options(1/2/3/4):")
print("1: old temperature")
print("2: precipitation")
print("3: new temperature")
print("4: new precipitation")
choice = input("your choice ? :     ")
if choice == '1':
    pt.plot(core_weather[["temp_max", "temp_min"]])
    pt.show()
elif choice == '2' :
    pt.plot(core_weather[["precip"]])
    pt.show()
elif choice == '4' :
    error, combined = create_predictions(predictors1, core_weather, reg)
    pt.plot(combined)
    pt.show()
elif choice == '3':
    error, combined = create_predictions(predictors2, core_weather, reg)
    pt.plot(combined)
    pt.show()
else:
    print('ending the program.')


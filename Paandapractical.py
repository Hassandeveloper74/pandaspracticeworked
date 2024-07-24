import pandas as pd
import numpy as np

# data={"namd":["syed","Ali","ahmed"],"Age":[12,24,34],"Salary":[233333,540455,495856]}
# df=pd.DataFrame(data)
# print(df)
# df=pd.read_csv("c:/Users/Admin/Desktop/mastersheet.csv")                  //for data load using panda
# print(df)

data=pd.read_excel("book1.xlsx")
# print(df.head(4))                            //from head 4 rowss shown
# print(df.tail(4))                             // from tail 4 rows shown 
# print(df.info())                          //   information of data 
# print(df.describe())                      // describe data behaviour
# print(df.isnull().sum())                //show how much null values in our dataset
# print(data)
# print(data["No of gigs"].duplicated().sum())
# dp=data.drop_duplicates("No of gigs")       //duplicate value in specific colomn

# print(data)
# print(data["salary"].mean())

# print(data.replace(np.nan,mn))
# data["salary"]=data["salary"].replace(np.nan,400)
# print(data)
# print(data.isnull().sum())

# print(data.dropna())

# print(data)
# print(data.fillna(method="bfill"))
# print(data.fillna(method="ffill"))


# data.loc[(data["salary"] == 0),"GetBonus"]="no bonus"           //for creating new colomn
# data.loc[(data["salary"]>0,"GetBonus")]="Bonous"
# print(data)

# data["ag"]=data["name"]+data["gender"]             //for colomn concatination
# print(data)

# data["bonus"]=(data["salary"]/100)*20
# print(data)

# data1={"Months":["January","Febery","March","April"]}            
# a=pd.DataFrame(data1)
# print(a)

print(data.head(4))

gb=data.groupby(["Employeeid","name"]).agg({"gender":"count"})
print(gb)
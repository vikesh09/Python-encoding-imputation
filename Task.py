import pandas as pd
import numpy as np
data ={
    "Name": ["Jethalal", "Daya", "Popatlal", "Dr Hansraj haathi", "Mehta Sahab", "Bhide", "Baapu Ji", "Gogi","Tapu", "Roshan Singh Sodhi","Madhvi","Babita Ji","Iyer","Abdul"],
    "Age": [45, 42, 35, 50, np.nan, 48, 70, 30, 15, 40, 38, 36, 60, np.nan],
    "City": ["Kachh", "Ahmadabad", "Bhopal", "Bihar", "Mumbai", "Mumbai", "Kachh", "Mumbai", "Mumbai", "Mumbai", "Mumbai", "Mumbai", "Mumbai", "Mumbai"],
    "Occupation": ["Shopkeeper", "Housewife", "Journalist", "Doctor", "Job", "Teacher", "Retired", "Student","Student", "Job","Housewife","Housewife","Scientist","Shopkeeper"],
    
}
df=pd.DataFrame(data)
#ordinal Encoding
City_mapping={"Kachh":1,"Ahmadabad":2,"Bhopal":3,"Bihar":4,"Mumbai":5}
df["City_Encoded"] = df["City"].map(City_mapping)
print(df)

#One Hot Encoding
Cities = df["City"].unique()
for city in Cities:
    a=[]
    for c in df["City"]:
        if c==city:
            a.append(1)
        else:
            a.append(0)
    df[f"city_{city}"]=pd.DataFrame(a)
print(df)
#simple Imputer
#mean
mean_age=df["Age"].mean()
df["Age"].fillna(mean_age,inplace=True)
print(df)
#median
median_age=df["Age"].median()
df["Age"].fillna(median_age,inplace=True)
print(df)
#mode
mode_age=df["Age"].mode()
df["Age"].fillna(mode_age,inplace=True)
print(df)


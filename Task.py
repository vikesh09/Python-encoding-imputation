import pandas as pd
import numpy as np
data ={
    "Name": ["Jethalal", "Daya", "Popatlal", "Dr Hansraj haathi", "Mehta Sahab", "Bhide", "Baapu Ji", "Gogi","Tapu", "Roshan Singh Sodhi","Madhvi","Babita Ji","Iyer","Abdul"],
    "Age": [45, 42, 35, 50, np.nan, 48, 70, 30, 15, 40, 38, 36, 60, np.nan],
    "City": ["Kachh", "Ahmadabad", "Bhopal", "Bihar", "Mumbai", "Mumbai", "Kachh", "Mumbai", "Mumbai", "Mumbai", "Mumbai", "Mumbai", "Mumbai", "Mumbai"],
    "Occupation": ["Shopkeeper", "Housewife", "Journalist", "Doctor", "Job", "Teacher", "Retired", "Student","Student", "Job","Housewife","Housewife","Scientist","Shopkeeper"],
    "Education": ["High School", "High School", "Graduation", "PhD", "Graduation", "Graduation", "High School", "High School","High School", "Graduation","Graduation","Graduation","PhD","Graduation"]
}
df=pd.DataFrame(data)
#ordinal Encoding
Education_mapping={"High School":1,"Graduation":2,"PhD":3}
encoded_values=[]
for edu in df["Education"]:
    if edu in Education_mapping:
        encoded_values.append(Education_mapping[edu])
    else:
        encoded_values.append(0)
df["Education_Encoded"]=encoded_values
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


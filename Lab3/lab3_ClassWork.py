import pandas as pd

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

list1 = [['Alice',23,3.5,10],['Bob',24,3.4,6],['Charlie',22,3.9,8]]
df = pd.DataFrame(list1)
df.columns = ['name','age','cgpa','hoursStudied']
print(df.head())

dict1 = {'id':[1,2,3],'name':['alice','bob','charlie'], 'age':[20, 25, 32]}
df1 = pd.DataFrame(dict1)
print(df1)

df2 = pd.read_csv('Z:\EWU Files\EWU course metarials\spring 2022\cse303\lab\lab3\weather.csv')
print(df2)
print(df2.head())
print(df2.tail())
print(df2.count())
df4 = df2.iloc[1::2,[0,1,3]]
print(df4)
df3=df1[['name','age']]
print(df3)

list2 = [['Alice',23,3.5,10],['Bob',24,3.4,6],['Charlie',22,3.9,8]]
df5 = pd.DataFrame(list2)
df5.columns = ['name','age','cgpa','hoursStudied']
list3 = [['Don',21,2.5,2],['Elton',25,2.75,4]]
df6 = pd.DataFrame(list3)
df6.columns = ['name','age','cgpa','hoursStudied']
df7 = df5.append(df6, ignore_index=True)
df7.sort_values(by='age', ascending=False)
print(df7)
cgpa_greater_than_three_point_five1 = df7[df7['cgpa'] > 3.5]
cgpa_greater_than_three_point_five2 = df7.loc[df7['cgpa'] > 3.5]
cgpa_greater_than_three_point_five3 = df7.query('cgpa > 3.5')

print(cgpa_greater_than_three_point_five1)
print(cgpa_greater_than_three_point_five2)
print(cgpa_greater_than_three_point_five3)

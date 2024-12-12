'''
import pandas as pd

file1="file1.csv"
fil2="fil2.csv"

mismatch="mismatches.csv"

a=pd.read_csv(file1)
b=pd.read_csv(fil2)

d=pd.DataFrame(a)
e=pd.DataFrame(b)

x= d != e
print(x)
mismatch_row=x[x.any(axis=1)]
mismatched_data =d[mismatch_row.index]

# Save the mismatched rows to a new CSV file
mismatched_data.to_csv(mismatch, index=False)
print(f"Mismatched rows have been saved to {mismatch}")


t=pd.merge(d,e,on='ID',how='left')
print(t)




import pandas as pd

x=pd.DataFrame({'ID':[3,4,5],
              'Name' :['XYX','YY','ZZ']})

y=pd.DataFrame({'ID':[3,4,5],
              'Name' :['XYNNX','BB','ZLLZ']})

z=x.compare(y)
print(z)

z= x != y
print(z)

V=pd.merge(x,y,on="ID",how='inner')
print(V)

s=[(x['ID']==1) & (['Sak']>200)]
print(s)














# Define file paths
file1 = "file1.csv"
fil2 = "fil2.csv"
#mismatch_file = "mismatches.csv"

# Read the CSV files into pandas DataFrames
a = pd.read_csv(file1)
b = pd.read_csv(fil2)

x=pd.DataFrame(a)
y=pd.DataFrame(b)


result=x[(x['ID'] == 1) & (x['Age'] == 30)]
print(result)
#print(y)


# Compare the two DataFrames element-wise
comparison = a != b  # This will create a DataFrame with True/False values

# Get the rows where there are mismatches (True values in the comparison)
mismatched_rows = comparison[comparison.any(axis=1)]  # Rows with at least one mismatch

# Filter the mismatched data from the original DataFrame (a)
mismatched_data = a[mismatched_rows.index]

# Save the mismatched rows to a new CSV file
mismatched_data.to_csv(mismatch_file, index=False)

# Optionally, print the mismatched rows
print(f"Mismatched rows saved to {mismatch_file}")
print(mismatched_data)

'''
import numpy as np

'''
l1=[1,2,3,4]
l2=[3,4,5,6]
if l1 == l2:
    print("same")
else:
    print("not same")

my_list=[1,2,3,4]
z=my_list.append(5)
my_list.extend([6,7])
my_list.insert(1,4)
print(my_list)
print(my_list[2])
'''
'''
import pandas as pd
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

exam_data =pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
                         },index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

print(exam_data.iloc[:3])

print(exam_data[exam_data['qualify']=="yes"][["name","qualify"]])

'''
import pandas as pd
import csv
import json
d =pd.DataFrame({'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]})
e=pd.DataFrame({'col1': [5, 6, 7, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]})
h=pd.merge(d,e,on="col1",how="outer")
print(h)

df=h.to_json("./file.json")

df=pd.read_csv("./xyx.csv")

df=pd.read_json("./xyx.json")

print(df)

df=d.to_csv("./newfile.csv",sep='\t',index=False)

df1=pd.read_csv("./newfile.csv")
print(df1)





'''
list=[1,2,3]
print(list[1])

list.append(3)
print(list)

list.append([4,5,6])
print(list)

list.extend([7,8,9])
print (list)

list[4].append(9)
print(list)
'''
'''
tuple=(1,2,3)
print(tuple)

print(tuple[2])

''''''
dict={"id":1,"age":34}
print(dict)

print(dict["id"])

import pandas as pd

z=pd.DataFrame({"id":[11,12,13],
               "sal":[100,123,124]
                })
print(z)

y=pd.DataFrame({"id":[13,14,15],"sal":[121,122,123]})
print(y)

s=z.compare(y)

print(s)

s=pd.merge(z,y,on="id",how="left")



class Test:
    def __init__(self,username):
        self.username=username
        print (self.username)

    def try1(self):
        print("test")

class Test1(Test):

    def __init__(self):
        super().__init__("plabani")

    def try2(self):
        print("try2")

obj1=Test1()
obj1.try1()


'''
import pandas as pd
data={"id":[3,4,5],
      "sal":[100,200,300]}

df=pd.DataFrame(data,index=['r1','r2','r3'])
print(df)
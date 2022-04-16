import re

nameList = ["Chan Tai Man", "Lee Lap Man","Cheung Kwok Keung","Li Ho Yan"]
R = []
for x in nameList:
    R.append(re.sub(r'[a-z]','*', x))
print(R)

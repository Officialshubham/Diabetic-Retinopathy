import os
import pandas as pd

test1 = pd.read_csv('test1.csv')
id_list = test1['id_code'].tolist()

names_list=[]

for files in os.listdir("./test_images"):
    names_list.append(files.strip('.png'))






id_list_as_set = set(id_list)
names_list_as_set = set(names_list)

diff = names_list_as_set.difference(id_list_as_set)

diff_as_list = list(diff)

for i in diff_as_list:
    os.remove("./test_images/"+i+".png")
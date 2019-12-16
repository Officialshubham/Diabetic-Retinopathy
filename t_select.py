import os
import pandas as pd

train1 = pd.read_csv('train1.csv')
id_list = train1['id_code'].tolist()

names_list=[]

for files in os.listdir("./train_images"):
    names_list.append(files.strip('.png'))






id_list_as_set = set(id_list)
names_list_as_set = set(names_list)

diff = names_list_as_set.difference(id_list_as_set)

diff_as_list = list(diff)

for i in diff_as_list:
    os.remove("./train_images/"+i+".png")
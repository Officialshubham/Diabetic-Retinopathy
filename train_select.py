import numpy as np
import os
import pandas as pd

train_ = pd.read_csv('train.csv')
train_final = train_.sample(frac=0.5,random_state = 11)
train_final.to_csv('train1.csv', index=False)


#for files in os.listdir("./train_images"):
#    print(files)
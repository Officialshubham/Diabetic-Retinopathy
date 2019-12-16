import numpy as np
import os
import pandas as pd

test_ = pd.read_csv('test.csv')
test_final = test_.sample(frac=0.5,random_state = 11)
test_final.to_csv('test1.csv', index=False)


#for files in os.listdir("./train_images"):
#    print(files)
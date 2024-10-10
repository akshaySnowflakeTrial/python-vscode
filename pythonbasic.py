'''
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from  IPython.display import display
# Loading iris datasets
data = load_iris()
df = pd.DataFrame(data.data,columns= data.feature_names)
# 1 way to display
# display(df.head(20))

# 2 way to display
# display(df.to_string())
# with pd.option_context('display.max_rows',None,
#                        'display.max_columns',None,
#                        'display.precision', 3
#                        ):
#     print(df)

# 3 way to display
# display str objects with formatting
print(df.to_markdown())

'''
import pandas as pd
# Creating dataframe
df = pd.DataFrame({'Names' : [' Sunny','Bunny','Ginny ',' Binny ',' Chinni','Minni'], 
                    'Age' : [23,44,23,54,22,11],
                    'Blood Group' : [' A+',' B+','O+','O-',' A-','B-'],
                   'Gender' : [' M',' M','F','F','F',' F']
                  })
print(df)
df['Names'].str.strip()
df['Blood Group'].str.strip()
df['Gender'].str.strip()
print(df)git 
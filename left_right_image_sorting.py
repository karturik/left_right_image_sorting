import os
import pandas as pd

s3_path =''

# SORTING IMAGES TO LEFT AND RIGHT FOR ML-COMPARING
left = list(filter(lambda x: x[0] !='.', os.listdir('left')))
right = list(filter(lambda x: x[0] !='.', os.listdir('right')))
df = pd.DataFrame(columns = ['INPUT:leftPic','INPUT:rightPic'])
df['f'] = left

# ADDINGG S3-ADRREAS
u = f'https://storage.yandexcloud.net/{s3_path}/left/'
df['INPUT:leftPic'] = u + df['f']
u = f'https://storage.yandexcloud.net/{s3_path}/right/'
df['INPUT:rightPic'] = u + df['f']
del df['f']

df.iloc[-1]

print(df.iloc[-1]['INPUT:rightPic'])

df.iloc[:100].to_csv('data_for_annotation_5k_1_100.tsv',index=None,sep='\t')

df.iloc[100:].to_csv('data_for_annotation_5k_2_4900.tsv',index=None,sep='\t')

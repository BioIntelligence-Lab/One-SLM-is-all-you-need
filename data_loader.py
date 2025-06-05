import pandas as pd
from tqdm import tqdm
from datasets import Dataset 

def harmonize_series():
    df=pd.read_excel('../../Labeled MRI Brain Series Descriptions.xlsx',sheet_name='Sheet2')
    df['index_col'] = df.index
    dataset = Dataset.from_pandas(df)
    full_dataset = dataset.train_test_split(test_size=0.2, shuffle=True, seed=0)
    dataset_train = full_dataset['train']
    dataset_test = full_dataset['test']
    return dataset_train,dataset_test

def response():
    df=pd.read_csv('../../IU-GroundTruth.csv')
    dataset = Dataset.from_pandas(df)
    full_dataset = dataset.train_test_split(test_size=0.2, shuffle=True, seed=0)
    dataset_train = full_dataset['train']
    dataset_test = full_dataset['test']
    return dataset_train,dataset_test

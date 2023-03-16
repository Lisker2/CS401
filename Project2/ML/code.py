from mlxtend.frequent_patterns import association_rules, fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd 
import numpy as np
import os

#data_path = os.environ['data_path']

data = pd.read_csv("/home/datasets/playlist-sample-ds1.csv")

#data = pd.read_csv(data_path)

transactions = [i[1]["track_name"].tolist() for i in list(data.groupby(["name"]))]
en = TransactionEncoder()
matrix = en.fit(transactions).transform(transactions)
matrix = pd.DataFrame(matrix, columns=en.columns_)
rules = fpgrowth(matrix,min_support=0.001,use_colnames=True)
rules["num"] = rules["itemsets"].apply(lambda x:len(x))
rules = association_rules(rules,metric="lift",min_threshold=1)
n = len(rules["antecedents"])
for i in range(n):
    rules["antecedents"][i] = list(rules["antecedents"][i])
    rules["consequents"][i] = list(rules["consequents"][i])
rules.to_csv("data/test.csv")
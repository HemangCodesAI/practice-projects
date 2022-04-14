# importing stuff
from __future__ import absolute_import, division, print_function, unicode_literals
from dataclasses import dataclass
from hashlib import algorithms_available
from tkinter import Variable
from attr import define
import numpy as np
import pandas as pd
import tensorflow as tf


#getting data
train = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')
test = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')
y_train =train.pop('survived')
y_test =test.pop('survived')


# previewing data
# train.head()
# test.head()
# train.shape()
# y_train.head()
# y_test.head()


 # defineing function
def feed( data_df, label_df,epochs=10,shuffle=True,batch=32):
        def input():
            ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
            if shuffle:
                ds=ds.shuffel()
            ds=ds.batch(batch).repeat(epochs)
            return ds
        return input
trainer = feed(train, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
evaluator = feed(test, y_test, epochs=1, shuffle=False)
    
# defineing Variables
CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = train[feature_name].unique()  # gets a list of all unique values from given feature column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)


# passing to algorithm
algo = tf.estimator.LinearClassifier(feature_columns=feature_columns)


# training and testing
algo.train(trainer)  # train
result = algo.evaluate(evaluator)  # get model metrics/stats by testing on tetsing data

# clear_output()  # clears console output
print(result['accuracy'])  # the result variable is simply a dict of stats about our model
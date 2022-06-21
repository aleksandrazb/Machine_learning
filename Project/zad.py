#!/usr/bin/python

#
# Woźniak Marcin
# 434812
#

import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from sklearn import model_selection

# Dane pochodzą ze strony
# https://archive.ics.uci.edu/ml/datasets/banknote+authentication
data = pd.read_csv("data.csv")
x = data.iloc[:, 0:-1]
y = data.iloc[:, -1]

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

model = keras.Sequential(
    [
        layers.Dense(15, activation="relu"),
        layers.Dense(9, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(x_train, y_train, epochs=1600, batch_size=200, validation_split=0.2)

score = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy:", score[1])
print("Loss:", score[0])

# Accuracy: 1.0 Loss: 1.3936358300270513e-05
# Accuracy: 1.0 Loss: 1.3100921023578849e-05
# Accuracy: 1.0 Loss: 1.039111793943448e-05
# Accuracy: 1.0 Loss: 2.8891838155686855e-05

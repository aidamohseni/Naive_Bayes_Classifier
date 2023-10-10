# importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def accuracy(y_tes, y_pred):
    correct = 0
    for i in range(len(y_pred)):
        if y_tes[i] == y_pred[i]:
            correct += 1
    return (correct / len(y_tes)) * 100

def breastCancerPreparation():
    # Importing the dataset
    dataset = pd.read_csv('breastCancer2.csv')
    dataset.replace('?', 0, inplace=True)
    dataset = dataset.applymap(np.int64)
    X = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    y_new = []
    for i in range(len(y)):
        if y[i] == 2:
            y_new.append(0)
        else:
            y_new.append(1)
    y_new = np.array(y_new)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    from sklearn.naive_bayes import GaussianNB
    NB = GaussianNB()
    NB.fit(X_train, y_train)

    final_pred = NB.predict(X_test)

    print("Naive Bayes Classifier Accuracy =: ", accuracy(y_test, final_pred), "%")


breastCancerPreparation()


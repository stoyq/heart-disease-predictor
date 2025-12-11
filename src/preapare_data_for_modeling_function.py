from sklearn.model_selection import train_test_split
import pandas as pd

def split_data(X,y):
     #Data Splitting

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,   
        random_state=522 
    )

    return X_train, X_test, y_train, y_test
    
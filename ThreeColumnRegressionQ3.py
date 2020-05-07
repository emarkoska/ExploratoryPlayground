import pandas as pd
import numpy as np
from MultipleRegressionQ3 import OrdinaryLeastSquares

#Defining root mean square error as a function to evaluate the model
def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

#Defining mean average percentage error as a function to evaluate the model
def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

if __name__ == '__main__':
    """
    We'll assign column names and read the data from the csv format.
    We create two objects, a dataframe (containing columns A and B) and a series, containing column C.
    We make an object of the OrdinaryLeastSquares implementation
    We fit the data to the model and get the coefficients for our function
    """
    col_names = ['A','B','C']
    df = pd.read_csv("Data/three_column_regression.csv", names=col_names, header=None)

    X = df.drop('C',1).values
    y = df['C'].values

    model = OrdinaryLeastSquares()
    model.fit(X,y)

    print("Coefficients for our multiple regression model")
    print(model.coefficients) #Coefficients

    y_preds = []
    for row in X: y_preds.append(model.predict(row))

    print("RMSE: %f" % rmse(y, y_preds))
    print("MAPE: %f" % mape(y, y_preds))


    pylab.scatter(df['C'].index, df['C'])
    plt.show()
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score

def model_info(df):
    '''
    model_info will take in a dataframe with actual and predicted values, and print
    an accuracy score, confusion matrix, and classification report
    '''
    print('Accuracy: {:.2%}'.format(accuracy_score(df.actual, df.predicted)))
    print('---')
    print('Confusion Matrix')
    print(pd.crosstab(df.predicted, df.actual))
    print('---')
    print(classification_report(df.actual, df.predicted))
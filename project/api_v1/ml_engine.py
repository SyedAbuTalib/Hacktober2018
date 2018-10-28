from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split
from . import data

dtree_model = False


def runEngine(users):
    if dtree_model:
        X_test = extractX(users)
        dtree_predictions = dtree_model.predict(X_test) 
        return dtree_predictions
    else:
        mlModel()

def runEngineSingle(user):
    if dtree_model:
        X_test = extractX(users)
        dtree_predictions = dtree_model.predict(X_test) 
        return dtree_predictions
    else:
        mlModel()



def mlModel():      
    # training a DescisionTreeClassifier 
    from sklearn.tree import DecisionTreeClassifier 
    X_train = data.getXData()
    y_train = data.getYData()
    dtree_model = DecisionTreeClassifier(max_depth = 20).fit(X_train, y_train) 
    # dtree_predictions = dtree_model.predict(X_test) 
    
    # creating a confusion matrix 
    # cm = confusion_matrix(y_test, dtree_predictions) 
    return

def extractX(users):
    return users
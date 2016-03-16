from sklearn.cross_validation import cross_val_score,train_test_split
from sklearn.tree import DecisionTreeClassifier

def decision_tree_process(x_data,y_data):
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(X_train,y_train)
    scores = cross_val_score(decision_tree,X_test,y_test)
    return decision_tree,decision_tree.score(X_test,y_test)

from sklearn.neighbors import KNeighborsClassifier

def knn_process(x_data,y_data):
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.4, random_state=0)
    knn = DecisionTreeClassifier()
    knn.fit(X_train,y_train)
    scores = cross_val_score(knn,X_test,y_test)
    return knn,knn.score(X_test,y_test)
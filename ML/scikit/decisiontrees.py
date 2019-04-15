from sklearn.datasets import load_iris
from sklearn import tree, metrics
import graphviz 

iris = load_iris()
clf = tree.DecisionTreeClassifier(max_depth=2)
clf = clf.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 

# Predict the full data set
expected = iris.target
predicted = clf.predict(iris.data)

# Display metrics
# Precision measures the impact of false positives: TP/(TP+FP)
# Recall measures the impact of false negatives : TP/(TP+FN)
# F1 is the weighted average of precision and recall: (2*Recall*Precision)/(Recall+Precision)
print(metrics.classification_report(expected, predicted))

# Display confusion matrix
print(metrics.confusion_matrix(expected, predicted))

# Display feature importance
print(clf.feature_importances_)

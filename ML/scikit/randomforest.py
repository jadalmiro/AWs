from sklearn.datasets import load_iris
from sklearn import tree, ensemble, metrics
import graphviz 

iris = load_iris()
clf = ensemble.RandomForestClassifier(max_depth=3)
clf = clf.fit(iris.data, iris.target)

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

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

train, test = tf.keras.datasets.mnist.load_data()
mnist_images, mnist_labels = train
mnist_test_images, mnist_test_labels = test

print(mnist_images.shape)
print(mnist_test_images.shape)

mnist_images = mnist_images.flatten().reshape(60000,784)
mnist_test_images = mnist_test_images.flatten().reshape(10000,784)

mnist_images = mnist_images / 255
mnist_test_images = mnist_test_images / 255

print(mnist_images.shape)
print(mnist_test_images.shape)

plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(mnist_images[0:5], mnist_labels[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (28,28)), cmap=plt.cm.gray)
    plt.title('Training: %s\n' % label, fontsize = 20)
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn import metrics

logisticRegr = LogisticRegression(solver='lbfgs', multi_class='auto', verbose=1, max_iter=100)
logisticRegr.fit(mnist_images, mnist_labels)

#logisticRegr.predict(mnist_test_images[0].reshape(1,-1))
#logisticRegr.predict(mnist_test_images[0:10])

predictions = logisticRegr.predict(mnist_test_images)
score = logisticRegr.score(mnist_test_images,mnist_test_labels)
print(score)

# Display metrics
# Precision measures the impact of false positives: TP/(TP+FP)
# Recall measures the impact of false negatives : TP/(TP+FN)
# F1 is the weighted average of precision and recall: (2*Recall*Precision)/(Recall+Precision)
print(metrics.classification_report(mnist_test_labels, predictions))

# Display confusion matrix
print(metrics.confusion_matrix(mnist_test_labels, predictions))

index = 0
misclassifiedIndexes = []
misclassifiedLabels = []
for label, predict in zip(mnist_test_labels, predictions):
    if label != predict: 
        misclassifiedIndexes.append(index)
        misclassifiedLabels.append(predict)
    index +=1

plt.figure(figsize=(20,4))
for plotIndex, badIndex in enumerate(misclassifiedIndexes[0:5]):
    plt.subplot(1, 5, plotIndex + 1)
    plt.imshow(np.reshape(mnist_test_images[badIndex], (28,28)), cmap=plt.cm.gray)
    plt.title('Prediction: %s\n' % misclassifiedLabels[badIndex], fontsize = 20)
plt.show()



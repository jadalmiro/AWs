import tensorflow as tf

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
print(mnist_labels.shape)

from sklearn.decomposition import PCA
pca = PCA(n_components=10)
mnist_images_pca = pca.fit(mnist_images).transform(mnist_images)
mnist_test_images_pca = pca.transform(mnist_test_images)

print(mnist_images_pca.shape)
print('explained variance ratio: %s' % str(pca.explained_variance_ratio_))

from sklearn.linear_model import LogisticRegression

logisticRegr = LogisticRegression(solver='lbfgs', multi_class='auto', verbose=1, max_iter=500)
logisticRegr.fit(mnist_images_pca, mnist_labels)

predictions = logisticRegr.predict(mnist_test_images_pca)
score = logisticRegr.score(mnist_test_images_pca,mnist_test_labels)
print(score)


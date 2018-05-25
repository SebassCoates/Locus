from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, train_test_split
import numpy as np

features = open('features.txt', 'r').read().split('\n')
features = features[0:len(features) - 1]
for i,feature in enumerate(features):
    split = features[i].split(',')
    features[i] = split[0:len(split) - 1]
features = np.array(features, dtype='int32')

labels = open('labels.txt', 'r').read().split(',')
labels = np.array(labels[0:len(labels) - 1], dtype='int32')

print("Testing MultinomialNB")
alphas = [1]#[.1, .2, .5, 1, 2, 5, 10, 100]
for alpha in alphas:
    X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=.2)
    classifier = MultinomialNB(alpha = alpha)
    classifier.fit(X_train, Y_train)
    print(classifier.score(X_test, Y_test))
    #print(len(set(Y_test)&set(result)) / float(len(set(Y_test) | set(result))) * 100)
    #classifier = MultinomialNB(alpha=alpha)
    #scores = cross_val_score(classifier, features, labels, cv=1)
    #print("Error: %0.3f (+/- %0.3f) for alpha=%0.3f" % (1 - scores.mean(), scores.std() * 2, alpha))
print()

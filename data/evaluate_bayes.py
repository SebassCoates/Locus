from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
import numpy as np

features = open('features.txt', 'r').read().split('\n')
print(features)


print("Testing MultinomialNB")
alphas = 1#[.1, .2, .5, 1, 2, 5, 10, 100]
for alpha in alphas:
    classifier = MultinomialNB(alpha=alpha)
    scores = cross_val_score(classifier, features, labels, cv=5)
    print("Error: %0.3f (+/- %0.3f) for alpha=%0.3f" % (1 - scores.mean(), scores.std() * 2, alpha))
print()

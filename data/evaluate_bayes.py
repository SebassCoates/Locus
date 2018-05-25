<<<<<<< HEAD
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, train_test_split
import numpy as np

=======
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np

############################# READ AND PARSE DATA ##############################
print("Reading features and label data")
>>>>>>> 8afcbdb25f5acc054ffa71db731d286c161e2c88
features = open('features.txt', 'r').read().split('\n')
features = features[0:len(features) - 1]
for i,feature in enumerate(features):
    split = features[i].split(',')
    features[i] = split[0:len(split) - 1]
features = np.array(features, dtype='int32')

labels = open('labels.txt', 'r').read().split(',')
labels = np.array(labels[0:len(labels) - 1], dtype='int32')

<<<<<<< HEAD
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
=======
X_train, X_test, Y_train, Y_test = train_test_split(features, labels, test_size=.1, random_state=0)

#Bad guess when correct answer is not in the top 10 guesses
def evaluate(guesses, correctLabels):
    NUM_GUESSES = 10
    correctGuessCount = 0
    for i, guess in enumerate(guesses):
        for bestGuess in sorted(list(guess), reverse=True)[0:NUM_GUESSES]:
            #Note, because labels are ordered ascending by parser, no need to use classifier.classes_
            labelGuess = list(guess).index(bestGuess)
            if labelGuess == correctLabels[i]:
                correctGuessCount += 1
                break

    print("Best Guess Accuracy: " + str(correctGuessCount / len(correctLabels)))


############################### EVALUATE RESULTS ###############################
print("Testing Random Forest")
depths = [1,3,7,13,21,40,75,100]
for d in depths:
    classifier = RandomForestClassifier(max_depth=d, random_state=0)
    print("Fitting model")
    classifier.fit(X_train, Y_train)
    print("Evaluating best guess accuracy for depth = " + str(d))
    print(classifier.score(X_test, Y_test))
    #print("Evaluating top-n guess accuracy")
    #evaluate(classifier.predict_log_proba(X_test), Y_test)
    print()

#Test KKN of various k values with cross validation
print("Testing KNN")
Ks = [101]
for K in Ks:
    classifier = KNeighborsClassifier(K)
    print("Fitting model")
    classifier.fit(X_train, Y_train)
    print("Evaluating best guess accuracy for K = " + str(K))
    print(classifier.score(X_test, Y_test))
    print("Evaluating top-n guess accuracy")
    evaluate(classifier.predict_log_proba(X_test), Y_test)
    print()


print("Testing GaussianNB")
classifier = GaussianNB()
print("Fitting model")
classifier.fit(X_train, Y_train)
print("Evaluating best guess accuracy")
print(classifier.score(X_test, Y_test))
print("Evaluating top-n guess accuracy")
evaluate(classifier.predict_log_proba(X_test), Y_test)
print()

#Test gradient boosting of varied number of estimators with cross validation
print("Gradient Boosting")
numEstimators = [i for i in range(25, 39, 1)]
for num in numEstimators:
    classifier = GradientBoostingClassifier(n_estimators=num) 
    scores = cross_val_score(classifier, features, labels, cv=5)
    print("Error: %0.3f (+/- %0.3f) for num_estimators=%d" % (1 - scores.mean(), scores.std() * 2, num))
print()
>>>>>>> 8afcbdb25f5acc054ffa71db731d286c161e2c88

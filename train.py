from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from take_data import train_test_split_data, k_fold, get_x_y
import pickle, os, json


skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=87)

clf = list()
clf += [('Decision_Tree', GridSearchCV(Pipeline([('scaler', StandardScaler()), ('DT', DecisionTreeClassifier(random_state=88))]), param_grid={'DT__max_depth': list(range(5,50,2))}, cv=skf, n_jobs=-1))]
clf += [('Random_Forest', GridSearchCV(Pipeline([('scaler', StandardScaler()), ('RF', RandomForestClassifier(random_state=88))]), param_grid={'RF__max_depth': list(range(5,50,2))}, cv=skf, n_jobs=-1))]
clf += [('KNN', GridSearchCV(Pipeline([('scaler', StandardScaler()), ('Knn', KNeighborsClassifier())]), param_grid={'Knn__n_neighbors': list(range(3,20,2))}, cv=skf, n_jobs=-1))]
clf += [('SVM', Pipeline([('scaler', StandardScaler()), ('SVM', SVC())]))]
clf += [('Gaussian_Naive_Bayes', Pipeline([('scaler', StandardScaler()), ('GNB', GaussianNB())]))]

clf += [('Neural_Network', GridSearchCV(Pipeline([('scaler', StandardScaler()), ('MLP', MLPClassifier(random_state=88))]), param_grid={'MLP__hidden_layer_sizes': [(3,), (6,), (9,3)], 'MLP__max_iter': list(range(2000,10000,1000))}, cv=skf, n_jobs=-1))]

accuracy = list()
for name, classifier in clf:
    print(name)
    ac = list()
    for train_x, train_y, test_x, test_y in k_fold():
        classifier.fit(train_x, train_y)
        ac.append(classifier.score(test_x, test_y))
    print(ac)
    accuracy.append((name, ac))
    
    x, y = get_x_y()
    classifier.fit(x, y)
    with open(os.path.join('model', f'{name}.pkl'), 'wb') as f:
        pickle.dump(classifier, f)

with open('accuracy.json', 'w') as file:
    json.dump([[name, accuracy] for name, accuracy in accuracy], file, indent=4)

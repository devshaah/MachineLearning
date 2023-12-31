
#HOW TO CHOOSE THE BEST MODEL
#THE PROCESS OF CHOOSING OPTIMAL MODEL IS CALLED HYPERPARAMETER TUNING

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df= pd.DataFrame(iris.data, columns = iris.feature_names)
df['flower'] = iris.target
df

from sklearn.model_selection import train_test_split

xt,xtst,yt,ytst = train_test_split(df.drop(["flower"],axis = 'columns'),df['flower'],test_size=0.2)

from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import numpy as np

kernels = ['rbf','linear']
c = [1,10,20]
avg = {}
for i in kernels:
  for cval in c:
    cv_score = cross_val_score(SVC(kernel=i,C=cval,gamma='auto'),iris.data,iris.target,cv=5)
    avg[i + "_" + str(cval)] = np.average(cv_score)
avg

#GRIDSEARCHCV DOES EXACTLY WHAT IS DONE IN ABOVE BLOCK
from sklearn.model_selection import GridSearchCV

clf = GridSearchCV(SVC(gamma='auto'),{
    'C' : [1,10,20],
    'kernel': ['rbf','linear']
},cv=5, return_train_score=False)

clf.fit(iris.data,iris.target)
result = pd.DataFrame(clf.cv_results_)
result

#RandomizedSearchCV works the same but for larger sets and takes random values of parameters, with one more parameter
#n_iter to define the iterations

#HYPERTUNING, HOW TO CHOOSE THE BEST MODEL FOR DATASET
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

model_params = {
    'svm' : {
        'model' : SVC(gamma='auto'),
        'params': {
            'C' : [1,10,20],
            'kernel' : ['rbf','linear']
        }
    },
    'random_forest' : {
        'model' : RandomForestClassifier(),
        'params': {
            'n_estimators' : [1,5,10]
        }
    },
    'logistic_regression' : {
        'model' : LogisticRegression(solver='liblinear',multi_class='auto'),
        'params': {
            'C' : [1,5,10]
        }
    },
}

scores = []

for model, mp in model_params.items():
  clf = GridSearchCV(mp['model'], mp['params'], cv=5 , return_train_score=False)
  clf.fit(iris.data, iris.target)
  scores.append({
      'model' : model,
      'best_score' : clf.best_score_,
      'best_params' : clf.best_params_
  })

df = pd.DataFrame(scores)
df

#HENCE BEST MODEL IS SVM

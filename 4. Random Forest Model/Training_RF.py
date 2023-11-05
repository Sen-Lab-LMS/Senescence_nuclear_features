## Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import shap
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import roc_curve, roc_auc_score, precision_score, confusion_matrix
from sklearn.metrics import (precision_recall_curve, PrecisionRecallDisplay)

## Reading data 
df = pd.read_csv('INPUT', header=None)
df.columns = ['class', 'area', 'Formfactor', 'Elongation', 'Compactness', 'ChordRatio', 'Gyration', 'Displacement']

## Separate features and labels
names = ['area', 'Formfactor', 'Elongation', 'Compactness', 'ChordRatio', 'Gyration', 'Displacement']
X = df.drop('class', axis=1).copy()
y = df['class'].copy()

## Train Random Forest Classifier 
clf = RandomForestClassifier(max_depth=None, n_estimators=100, random_state=42)
clf.fit(X, y)

## k-fold cross-validation
k = 5
cv_scores = cross_val_score(clf, X, y, cv=k, scoring='accuracy')

# Cross-validation scores
print(f'Cross-Validation Scores (Accuracy): {cv_scores}')
print(f'Mean Accuracy: {np.mean(cv_scores):.2f}')
print(f'Standard Deviation: {np.std(cv_scores):.2f}')

## Split the data into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

## Train Random Forest Classifier 
clf.fit(X_train, y_train)

## Evaluate the model on the test set
y_pred = clf.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f' Accuracy: {accuracy:.2f}')

## Visualize feature importance
feature_imp = pd.Series(clf.feature_importances_, index=names).sort_values(ascending=False)
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel("Feature Importance Score")
plt.ylabel('Features')
plt.title("Visualizing Important Features")
plt.show()

## ROC Curve
y_score1 = clf.predict_proba(X_test)[:, 1]
false_positive_rate1, true_positive_rate1, threshold1 = roc_curve(y_test, y_score1)
print('roc_auc_score for Random Forest:', roc_auc_score(y_test, y_score1))

## Plotting ROC Curve
plt.subplots(1, figsize=(10, 10))
plt.title('Receiver Operating Characteristic - Random Forest')
plt.plot(false_positive_rate1, true_positive_rate1)
plt.plot([0, 1], ls="--")
plt.plot([0, 0], [1, 0], c=".7"), plt.plot([1, 1], c=".7")
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()

## Compute precision scores
micro_precision = precision_score(y_test, y_pred, average='micro')
print('Micro-averaged precision score: {0:0.2f}'.format(micro_precision))

macro_precision = precision_score(y_test, y_pred, average='macro')
print('Macro-averaged precision score: {0:0.2f}'.format(macro_precision))

per_class_precision = precision_score(y_test, y_pred, average=None)
print('Per-class precision score:', per_class_precision)

## Develop a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:')
print(cm)

## Precision-Recall Curve
precision, recall, _ = precision_recall_curve(y_test, y_score1)
disp = PrecisionRecallDisplay(precision=precision, recall=recall)
disp.plot()
plt.show()

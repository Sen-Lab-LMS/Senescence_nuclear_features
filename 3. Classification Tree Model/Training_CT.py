import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import roc_curve, auc, average_precision_score, precision_recall_curve
import seaborn as sns
from sklearn.metrics import plot_confusion_matrix
from sklearn import tree
import graphviz

# Load the data 
df = pd.read_csv('INPUT', header=None)
df.columns = ['type', 'area', 'FormFactor', 'Elongation', 'Compactness', 'ChordRatio', 'Gyration', 'Displacement']

# Split features and target variable
X = df.drop('type', axis=1)
y = df['type']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Create DecisionTreeClassifier with specified parameters
clf = DecisionTreeClassifier(max_depth=5, min_samples_split=2, random_state=1)

# Fit classifier on the training data
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# accuracy
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)

# Calculate ROC curve and AUC
y_prob = clf.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
print('ROC AUC:', roc_auc)

# ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='royalblue', label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='darkorange', linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()

# Calculate Precision-Recall curve + average precision
precision, recall, _ = precision_recall_curve(y_test, y_prob)
average_precision = average_precision_score(y_test, y_prob)
print('Average Precision:', average_precision)

# Precision-Recall curve
plt.figure(figsize=(8, 6))
plt.step(recall, precision, color='b', where='post', alpha=0.8)
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall Curve (Average Precision = %0.2f)' % average_precision)
plt.show()

# Cross-validation for finding the best parameters
clf = DecisionTreeClassifier(random_state=1)
cv_scores = cross_val_score(clf, X_train, y_train, cv=5)
print('Cross-validation Mean Accuracy:', np.mean(cv_scores))

"""
ccp_alphas = []
path = clf.cost_complexity_pruning_path(X_train, y_train)
ccp_alphas = path.ccp_alphas
ccp_alphas = ccp_alphas[:-1]

print (ccp_alphas)
#print (clf)

clf_dts = []
alpha_loop_values = []

for ccp_alpha in ccp_alphas:
	clf = DecisionTreeClassifier(random_state=1, ccp_alpha=ccp_alpha)
	scores = cross_val_score(clf, X_train, y_train, cv=5)
	alpha_loop_values.append([ccp_alpha, np.mean(scores), np.std(scores)])

alpha_results = pd.DataFrame(alpha_loop_values, columns=['alpha', 'mean_accuracy', 'std'])
alpha_results.plot(x='alpha', y='mean_accuracy', yerr='std', marker='o', linestyle='--')
#plt.show()

#Using cross validation, we can see that, over all, instead of setting our alpha, we need to set it 
#to the higher point we obtain: Me lo he saltado yikes.

"""
ideal_ccp_alpha = 0.005

clf_pruned = DecisionTreeClassifier(random_state=0, ccp_alpha=ideal_ccp_alpha)
clf_pruned = clf_pruned.fit(X_train, y_train)

plot_confusion_matrix(clf_pruned, X_test, y_test, display_labels=["Prolif", "Senescent"])
plt.show()
print ("Done")

dot_data = tree.export_graphviz(clf_pruned, out_file=None, class_names=["Prolif", "Senescent"], filled=True, rounded=True, special_characters=True)  
graph = graphviz.Source(dot_data)  
print(graph)

text_representation = tree.export_text(clf_pruned)
print(text_representation)
from joblib import dump
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingClassifier
import os


X, y = load_iris(return_X_y=True)


clf_pipeline = [('scaling', MinMaxScaler()), ('clf', GradientBoostingClassifier())]
pipeline = Pipeline(clf_pipeline)

pipeline.fit(X, y)

# Ensure the directory exists before saving
#os.makedirs('.models/ml', exist_ok=True)
dump(pipeline, 'models/ml/iris_dt_v1.joblib')

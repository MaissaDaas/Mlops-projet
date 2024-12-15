import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Charger les données
data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['TARGET'] = data.target

# Diviser les données en ensembles d'entraînement et de test
X = df.drop('TARGET', axis=1)
y = df['TARGET']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Configurer l'URI MLflow (sur la VM)
mlflow.set_tracking_uri("http://192.168.1.100:5000")  # Remplacez par l'IP de votre VM
mlflow.set_experiment("california-housing-prediction")

# Enregistrer l'expérience avec MLflow
with mlflow.start_run():
    # Entraîner le modèle
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prédire et évaluer les performances
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    # Loguer les paramètres et métriques avec MLflow
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("mse", mse)

    # Loguer le modèle directement avec MLflow sans utiliser Joblib
    mlflow.sklearn.log_model(model, "model")  # Loguer le modèle directement avec MLflow

    print(f"Model MSE: {mse}")
# Función para entrenar el modelo
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def train_model(X_train, y_train):
    # Crear un pipeline para preprocesar los datos
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", SimpleImputer(strategy="median"), ["feature1", "feature2"]),
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["feature3", "feature4"]),
        ]
    )

    # Crear un pipeline para entrenar el modelo
    model = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(n_estimators=100)),
    ])

    # Entrenar el modelo
    model.fit(X_train, y_train)

    return model
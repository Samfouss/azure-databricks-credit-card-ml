# Pipeline ML end-to-end pour la détection de fraude avec pratiques MLOps complètes. Inclut feature engineering avancé, gestion de données déséquilibrées, tracking MLflow et gouvernance Unity Catalog.

## Système de Détection de Fraude avec Pipeline MLOps

Un pipeline de machine learning production-ready pour la détection de fraude sur cartes de crédit, gérant des datasets hautement déséquilibrés (0,17% de fraude) avec MLOps et gouvernance complètes.

## 🎯 Fonctionnalités Clés
- **Feature Engineering Avancé** : 30+ features créées avec window functions PySpark
- **Gestion des Données Déséquilibrées** : SMOTE, pondération de classes et stratégies d'échantillonnage stratifié
- **MLOps avec MLflow** : Tracking d'expériences, optimisation d'hyperparamètres (Hyperopt), registre de modèles
- **Gouvernance Unity Catalog** : Traçabilité complète des données brutes aux prédictions du modèle
- **Monitoring en Production** : Détection de data drift, suivi de performance, retraining automatisé

## 🛠️ Stack Technique
Databricks ML Runtime • PySpark • MLflow • Delta Lake • Unity Catalog • XGBoost • SHAP

## 📊 Résultats
- **Performance du Modèle** : 96% précision, 85% rappel, 0,97 AUC-ROC
- **Scalabilité** : Scoring de 100K transactions en 5 minutes
- **Impact** : Réduction de 80% de la fraude détectable

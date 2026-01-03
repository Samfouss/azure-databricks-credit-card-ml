# Plateforme d'analyse de transactions end-to-end traitant 284K+ transactions de cartes de crédit avec détection d'anomalies, frameworks de qualité des données et dashboards Power BI temps réel. Construite sur Azure Databricks avec Delta Lake.


## Plateforme d'Analyse de Transactions & Détection d'Anomalies
Une solution d'ingénierie de données scalable pour l'analyse de transactions financières avec détection automatisée d'anomalies et monitoring de la qualité des données.

## Pipeline ETL
### Phase 1 : Ingestion (Bronze Layer)
Objectif : Charger les données brutes dans Delta Lake avec métadonnées

### Phase 2 : Transformation (Silver Layer)
Objectif : Nettoyer, valider et enrichir les données

### Phase 3 : Analytics (Gold Layer)
Objectif : Créer des tables agrégées pour analyses métier

## 🎯 Fonctionnalités Clés
- **Pipeline Médaillon** : Architecture Bronze-Silver-Gold avec merges incrémentaux Delta Lake
- **Framework de Qualité des Données** : Tests de validation automatisés (nullité, plages, intégrité référentielle)
- **Optimisé pour la Performance** : Réduction de 35% du temps de traitement (45min → 29min) via optimisation Spark
- **Détection d'Anomalies** : Méthodes basées sur des règles métier et statistiques pour identifier les transactions suspectes

## 🛠️ Stack Technique
Azure Databricks • Delta Lake • PySpark • Spark SQL • Azure Data Lake Gen2

## 📊 Résultats
- Traitement de 284K transactions en 29 minutes
- Identification de 450+ transactions anomales (0,16%)

## Amélioration
- **Dashboards Interactifs** : Power BI / RShiny pour monitoring en temps réel

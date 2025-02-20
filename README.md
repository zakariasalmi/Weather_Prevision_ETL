# 🌦️ Moroccan Weather Prevision ETL

## 📌 Description  
Ce projet met en place un pipeline **ETL (Extract, Transform, Load)** pour récupérer, nettoyer et stocker des prévisions météorologiques. Il utilise **Apache Airflow**, **PestgreSql** et **Docker** pour orchestrer et traiter les données de manière efficace, avec l'integration du flask pour la visualisation des données.

## 🚀 Fonctionnalités  
- Extraction des données météorologiques à partir d'une API externe "OpenWeatherApi".  
- Transformation des données (nettoyage, conversion d'unités, gestion des valeurs manquantes).  
- Chargement des données transformées dans une base de données **PostgreSql**.  
- Orchestration avec **Apache Airflow** pour l'automatisation du pipeline.  
- Conteneurisation avec **Docker** pour une exécution flexible.
- Visualisation des données avec Flask

  <img width="562" alt="image" src="https://github.com/user-attachments/assets/7cd32cb8-055d-4379-b639-7eab70f98f38" />

  
## Visualisation des données dans une interface web 
![flask_webapp](https://github.com/user-attachments/assets/06dabbf7-65ea-47e6-aede-9c933c10580d)
![flask_webapp2](https://github.com/user-attachments/assets/c19e17d6-a265-4d92-a162-e52fc6d0f9d0)



## 🛠️ Technologies utilisées  
- **Python 3.9**  
- **Apache Airflow**  
- **PostgreSql**   
- **Docker & Docker Compose**  
- **Flask**
## 📂 Structure du projet  
```bash
Weather_Prevision_ETL/
│── dags/                    # Script Airflow DAGs
    |__previsions_dag.py
│── scripts/                     # Scripts ETL
│   ├── fetch_weather.py           # Extraction des données depuis l'API
│   ├── process_weather.py         # Transformation des données
│   ├── store_weather.py           # stockage des données dans la base de données postgres
|__ data/
    |__ Weather_data.json
    |__ Processed_Weather_data.csv       # chargement des données traitées dans un fichier csv
|__ templates/
    |__ index.html           l'interface web pour afficher les données.
|__ app.py                   # app flask backend pour récuperer les données de l'api
│── docker-compose.yml       # Configuration des services (Airflow, postgres)
│── requirements.txt         # Dépendances Python
```


## ⚙️ Installation et exécution
### 1️⃣ Prérequis 
Avant de commencer, assure-toi d’avoir installé :  
- **Docker & Docker Compose**  
- **Python 3.9+**
- **flask 3.0.2**

Cloner le projet :  
```bash
git clone https://github.com/ZakariaSalmi/Weather_Prevision_ETL.git
cd Weather_Prevision_ETL
```
- pip install -r requirement.txt

### 1️⃣ Démarrer le projet
docker-compose up -d
### 2 Démarrer le script app.py pour l'interface de visualisation web
python app.py

## 🛠️ Auteur
👤 Zakaria Salmi
🔗 |[ LinkedIn](https://www.linkedin.com/in/zakaria-salmi-a467a619a/)



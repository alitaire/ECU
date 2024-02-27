<<<<<<< HEAD
# SPEED TUNE MOTOR ECU
=======
# Speed Tune Motor ECU
>>>>>>> 1a74440df701c3b31df2359c1aa2c57afe0ba63c

![logo](img/logo.png)

## Auteurs

- Alexandre MINGANT
- Bastien DELAUNAY

## Présentation

Ce projet vise à mettre en place une gestion moteur programmé sur carte électronique, communement appeler ECU (Electronic Control Unit ou Engine Control Unit), l'architecture moteur à gérer est un moteur thermique essence atmosphérique 4 temps, la carte électronique sera controler par un microcontroleur stm32. 

### Fonctionnement d'un moteur essence 4 temps
 
Il est important de rappeler le fonctionnement d'un moteur thermique essence à 4 temps:

chatgpt

![schema]()

[video]()

### Les périphériques moteurs

afin de pouvoir connaitre les paramètres optimales permettant une injection et un allumage optimale, résultant d'une combustion optimale, les moteurs sont équipées de divers périphériques, dont voici une liste des plus important avec leurs fonctions: 

- Sonde PMH (Point Mort Haut):
- Sonde lambda (Sonde O2):
- Sonde MAP (Manifold Air Pressure / Pression de l'air dans l'admission):
- Sonde TPS (Throttle Position Sensor):
- Sonde IAT (Intake Air Temperature):

et les 2 actionneurs:

- bobine d'allumage:
- Injecteur de carburant:

![scheam]()

[video]()

### Objectifs du projet

Les objectifs visé pour ce projets sont réparties en 2 parties:

- Electronique :
  - Comprendre le fonctionnement des divers capteurs et leurs méthode d'acquisition de données et comprendre le fonctionnements des actionneurs. 
  - Concevoir une carte électronique ECU permettant la gestion des périphériques moteurs
  
- Programme : 
  - Concevoir un programme pour l'ECU permettant l'acquisition des données et la gestion des actionneurs sur base d'architecture stm32
  - Concevoir un programme de monitoring des données sur PC connecté en temps réel à l'ECU afin de collecter les données pertinantes et les analyser (dans le futur pouvoir modifier les données du calculateur).

### Structure du projet

définir la structure du git

## Partie électronique

intro

### Les périphériques moteurs

![schema](img/)
(schema avec les capteurs/actionneurs)

description des capteurs/actionneurs, fonctionnements et acquisition

### L'ECU (Engine Control Unit / Electronic Control Unit)


## Partie programme

intro

### Monitoring des données sur PC

### Gestion moteur sur ECU

## Etat du projet et suite

## Ressources
- Speeduino
- TunerStudio
- Megasquirt (check nom)
- Autres [ressources](/docs/autres/ressources.md)
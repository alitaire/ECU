<center>

# SPEED TUNE MOTOR ECU

![logo](img/logo.png)

</center>

## Auteurs

- Alexandre MINGANT
- Bastien DELAUNAY

## Présentation

Ce projet vise à développer une gestion moteur programmée sur une carte électronique, également connue sous le nom d'ECU (Unité de Contrôle Électronique ou Engine Control Unit). L'objectif principal est d'optimiser le fonctionnement d'un moteur thermique essence atmosphérique à 4 temps. La carte électronique sera contrôlée par un microcontrôleur STM32.

L'ECU est un composant crucial dans un moteur moderne, chargé de surveiller et de contrôler divers aspects du fonctionnement du moteur en temps réel. Il reçoit des données provenant de capteurs tels que la sonde lambda, la sonde de température, la sonde de pression, etc., et utilise ces informations pour ajuster le mélange air-carburant, le moment de l'allumage, le régime moteur et d'autres paramètres afin d'optimiser les performances du moteur et de réduire les émissions polluantes.

Dans ce projet, l'ECU sera conçu pour interpréter les données des capteurs et prendre des décisions de contrôle en fonction d'un programme conçu au préalable. Le microcontrôleur STM32 offrira une plateforme robuste et flexible pour exécuter le code et gérer les interactions avec les différents composants du moteur.

En somme, ce projet vise à créer une solution de gestion moteur avancée et personnalisable, offrant des performances optimales et une efficacité accrue pour le moteur thermique à essence.

### Fonctionnement d'un moteur essence 4 temps
 
Voici une explication simplifiée du fonctionnement d'un moteur thermique à essence à 4 temps :

1. **Admission** : Le premier temps, appelé temps d'admission, commence avec l'aspiration d'un mélange air-carburant dans le cylindre lorsque le piston descend. La soupape d'admission s'ouvre et le mélange est aspiré dans le cylindre.

2. **Compression** : Pendant le temps de compression, le piston remonte et compresse le mélange air-carburant dans le cylindre. Les soupapes d'admission et d'échappement sont fermées pour éviter toute fuite de pression.

3. **Combustion** : L'étincelle produite par la bougie d'allumage déclenche la combustion du mélange air-carburant comprimé. Cette explosion pousse le piston vers le bas, ce qui génère de l'énergie mécanique.

4. **Échappement** : Enfin, lors du temps d'échappement, le piston remonte à nouveau et pousse les gaz brûlés hors du cylindre par la soupape d'échappement ouverte. Ce processus libère les gaz d'échappement et prépare le cylindre pour un nouveau cycle.

Ces quatre temps (admission, compression, combustion et échappement) constituent un cycle complet. Dans un moteur à plusieurs cylindres, ces cycles se produisent simultanément dans différents cylindres pour maintenir un fonctionnement fluide et fournir de la puissance constante.

![cycle 4 temps](/img/cycle_4_temps.png)

Voici une animation complémentaire d'un [moteur essence 4 temps](https://www.youtube.com/watch?v=VP13eYbCtAc).

### Les périphériques moteurs

Pour garantir une injection et un allumage optimal, essentiels à une combustion efficace, les moteurs sont pourvus de divers périphériques. Voici une liste des plus importants, accompagnée de leurs fonctions :

- **Sonde PMH (Point Mort Haut)** : Cette sonde détecte la position du piston dans le cylindre, généralement utilisée pour synchroniser l'allumage et l'injection.

- **Sonde lambda (Sonde O2)** : Mesure la quantité d'oxygène dans les gaz d'échappement, permettant au système de contrôle du moteur de réguler le mélange air-carburant pour une combustion optimale.

- **Sonde MAP (Manifold Air Pressure / Pression de l'air dans l'admission)** : Mesure la pression de l'air entrant dans le collecteur d'admission, ce qui aide le calculateur du moteur à ajuster le débit de carburant en fonction de la charge du moteur.

- **Sonde TPS (Throttle Position Sensor)** : Surveille la position de la manette des gaz, permettant au calculateur de déterminer la demande de puissance du conducteur et d'ajuster en conséquence le mélange air-carburant.

- **Sonde IAT (Intake Air Temperature)** : Mesure la température de l'air entrant dans le moteur, aidant le calculateur à ajuster le mélange air-carburant en fonction des conditions ambiantes.

Explication en anglais de l'utilité et fonctionnement de chacuns de ces [capteurs](https://www.youtube.com/watch?v=dK4mb1yS0dY).

Et les 2 actionneurs :

- **Bobine d'allumage** : Transforme la basse tension de la batterie en haute tension nécessaire pour créer l'étincelle dans la chambre de combustion, déclenchant ainsi la combustion du mélange air-carburant.

- **Injecteur de carburant** : Vaporise le carburant dans la chambre de combustion, contrôlé par le calculateur moteur pour fournir la bonne quantité de carburant nécessaire à une combustion efficace.

![schema](/img/sensors_scheme.png)

### Objectifs du projet

Les objectifs de ce projet sont divisés en deux parties :

- Partie électronique :
  - Comprendre le fonctionnement des différents capteurs, leurs méthodes d'acquisition de données et le fonctionnement des actionneurs.
  - Concevoir une carte électronique ECU permettant de gérer les périphériques moteurs.

- Partie programmation :
  - Élaborer un programme pour l'ECU permettant d'acquérir des données et de gérer les actionneurs basé sur l'architecture STM32.
  - Développer un programme de surveillance des données sur un PC connecté en temps réel à l'ECU, permettant de collecter les données pertinentes et de les analyser (avec la capacité future de modifier les données du calculateur).

![schema projet](img/schema_projet.png)

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

Afin de pouvoir lire les données en temps réel, analyse d'une app existance (TunerStudio) utilisé pour speeduino ou encore Megasquirt, après analyse de la doc, conclusion que cela prendrais trop de temps dans les 6 mois pour son utilisation, a la place conception d'une petite application PC en python car rapide à mettre en place et compétence acquise ulérieure, utilisation d'une structure MCV (Modele Controller View) et communication en UART avec l'ECU

![schema MCV]()
Description d'un MCV

![vue application]()
Description des fonctionnalité de l'application

Retour sur idée de base, utilisation de TunerStudio carapplication maintenue dans le temps et un gros dev derrière, prendrais plus de temps pour dev une appli équivalente (aussi complète).

### Gestion moteur sur ECU

Analyse d'un projet similaire (speeduino)

Suite à cette analyse, une structure choisi:
- Main : Determiner les besoins du moteur et Gérer l'allumage et l'injection
- Globals : Définition des varibales/fonctions utiles pour tous les modules
- Inits : Initilise les données et modules du calculateur 
- Sensors : Gestion de l'acquisition des données des capteurs
- Decoders : Décodage des valeurs de certains capteurs
- Comms : Gestion de la communication entre la carte et l'extérieur
- Log : Archivage des activitées (Optionel)

Pour plus de détails, consulter [structure_code.md](/docs/autres/structure_code.md)

#### Main
Détails
#### Globals
Détails
#### Inits
Détails
#### Sensors
Détails
#### Decoders
Détails
#### Comms
Détails
#### Logs
Détails

## Etat du projet et suite

## Ressources
- Speeduino
- TunerStudio
- Megasquirt (check nom)
- Autres [ressources](/docs/autres/ressources.md)
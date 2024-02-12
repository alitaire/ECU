# STM32 ENGINE CONTROL UNIT (ECU)

## Authors

- Alexandre MINGANT
- Bastien DELAUNAY

## Essais

- Utiliser carte Nucleo pour simuler valeurs analogiques + page interface PC parametrage simulation
- Lecture données temps-réel honda pour utiliser comme valeurs d'essai

## Codes

- Main : Determiner les besoins du moteur et Gérer l'allumage et l'injection
  - Vérifiez s'il y a une demande dans le tampon série à traiter.
  - Vérifiez si le moteur tourne en regardant la dernière fois qu'une dent de manivelle a été vue.
  - Lisez les valeurs de tous les capteurs analogiques (TPS, IAT, CLT, MAP, O2, tension de la batterie). Tous les capteurs ne sont pas lus à chaque boucle car ils ne changent pas assez fréquemment pour le justifier.
  - Les fonctions suivantes ne se produisent que si le moteur est 'synchronisé':
    - Vérifiez si le RPM est au-dessus ou en dessous du seuil de démarrage (les valeurs de carburant et d'allumage sont ajustées lorsque le moteur démarre).
    - Exécutez toutes les fonctions de correction (voir la section corrections.ino ci-dessous). Le résultat est un % par lequel la largeur d'impulsion sera ajustée (100 % = aucun ajustement, 110 % = 10 % de carburant en plus, 90 % = 10 % de carburant en moins).
    - Recherchez VE dans la table de carburant principale.
    - Convertissez VE en une valeur de largeur d'impulsion en µs.
    - Recherchez l'avance désirée dans la table d'allumage.
    - Calculez l'angle de manivelle actuel.
    - Calculez l'angle de manivelle auquel chaque injecteur doit s'ouvrir en fonction de la vitesse actuelle du moteur.
    - Calculez l'angle de pause en fonction du temps de pause souhaité et de la vitesse actuelle du moteur.
    - Calculez l'angle de début d'allumage pour chaque cylindre en soustrayant l'angle d'avance et l'angle de pause de l'angle de PMH.
    - Définissez un 'planning' pour chaque injecteur en convertissant les angles de début calculés ci-dessus en un nombre de µs dans le futur (par exemple, si l'injecteur doit commencer à s'ouvrir à 45° après le PMH et que l'angle de manivelle est actuellement de 10° avant le PMH, combien de temps faudra-t-il pour parcourir ces 55°).
  - Effectuez le même réglage de planning pour chaque sortie d'allumage.

- Globals :
  - Définition des varibales/fonction utiles pour tous les sous-programmes
  - ...
  
- Inits :
  - Initilisation des capteurs
  - ...

- Sensors :
  - Dans le main, Utilisation d'un compteur pour effectuer les lectures à une certaines fréquence
  - Fonctions de lecture des capteurs
  - ...

- Decoders : Permet de décoder les valeurs de certains capteurs
  - getRPM
  - getCrankAngle
  - ...


- Comms : Communication avec PC et commandes (voir comms_legacy.h/.cpp de Speeduino)
  - Machine d'état avec switch sur la commande reçu du PC
  - Utilisation d'une struct "Status" pour stocker les infos à communiquer (RPM, temp, O2,...)
  - Ajout d'un status de la commiunication (SERIAL_INACTIVE, SERIAL_TRANSMIT, SERIAL_RECEIVE,...)

- Log : Archivage des activitées (Optionel)
  - ...
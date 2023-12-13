# Engine mapping

## Definitions

AFR = Air Fuel Ratio 
VE = Volumetric Efficiency

## How to setup the VE map

1. Setup a AFR (Lambda) target map based on lambda sensor feedback values.

2. Use a basic VE map based on engine specifications (number of cylinder, total volum, bore and stroke of cylinder,...).

3. Proceed to tests and use an algorythms to automatically change VE map bases on AFR target map and current lambda value.

## Helps for setup

1. ECU read VE map and calculate the amount of fuel required
2. Inject fuel according to AFR target map
3. Wideband sensor tell to the ECU if the real value match with the AFR target and if not the ECU adjust the VE map value
4. Do the process again until reaching the AFR target value with the wideband sensor.

# Engine Knock and Pre-ignition Phenomena

## Definitions

- TDC (Top Dead Center) marks the highest point in the piston's motion within the cylinder.
- BDC (Bottom Dead Center) denotes the lowest point in the piston's motion within the cylinder.

Normal Combustion: Also referred to as deflagration, it is the controlled combustion process initiated by the spark plug.

Knocking Combustion: This type of combustion involves an explosion that occurs after the spark plug has fired, resulting in self-ignition. This can lead to engine damage.

Pre-ignition Combustion: Involving an explosion before the spark plug fires, pre-ignition can also cause engine damage due to the untimely ignition of the air-fuel mixture.

## Insights

Knocking and pre-ignition arise due to excessive temperatures within the cylinder, which prompt the air-fuel mixture to auto-ignite or cause glowing hot spots to ignite the mixture before the intended spark plug ignition (pre-ignition).

To mitigate these issues, utilizing higher octane fuel is a straightforward approach. Higher octane fuel offers greater resistance to knocking, reducing the chances of spontaneous combustion within the combustion chamber. Alternatively, maintaining an appropriate compression ratio for the engine can also be effective. The compression ratio is the ratio of the combustion chamber volume at BDC to that at TDC (BDC:TDC = compression ratio). The introduction of forced induction, such as turbochargers or other compressors, can elevate air temperatures due to compression, increasing the likelihood of knocks. Some turbocharged vehicles incorporate intercoolers to cool the incoming air, enhancing engine performance and diminishing knock potential. Lower compression ratios contribute to reduced air temperatures, facilitating the compatibility of a turbocharger.

Another strategy involves implementing a knock sensor, acting as a microphone to detect knocking. Following detection, the Engine Control Unit (ECU) analyzes specific frequencies, subsequently retarding the ignition timing of the spark plug in the subsequent cycle. The knock sensor, coupled with crankshaft angle data, determines the engine's pressure peak, inducing an ignition timing delay as a countermeasure.

## GUI FUTURE

Description d'une interface graphique (GUI) de surveillance moteur en cours de développement :

1. **Interface Intuitive :** Concevoir une interface conviviale et intuitive pour faciliter la compréhension des données du moteur, permettant aux utilisateurs de naviguer aisément.

2. **Visualisation Graphique :** Implémenter des représentations visuelles, telles que des graphiques et des tableaux dynamiques, pour afficher de manière claire les paramètres moteur, les performances et les tendances.

3. **Personnalisation des Widgets :** Offrir la possibilité de personnaliser les widgets et les panneaux d'affichage, permettant aux utilisateurs de configurer l'interface selon leurs préférences.

4. **Alertes en Temps Réel :** Intégrer des fonctionnalités d'alerte en temps réel pour informer les utilisateurs des conditions anormales ou des alarmes liées au fonctionnement du moteur.

5. **Historique des Données :** Mettre en place un système d'enregistrement des données pour permettre aux utilisateurs de consulter l'historique des performances du moteur et d'analyser les tendances passées.

6. **Surveillance des Capteurs :** Intégrer une fonction de surveillance des capteurs en temps réel, avec des indicateurs visuels pour signaler les variations de paramètres importants.

7. **Commandes à Distance :** Inclure des fonctionnalités permettant aux utilisateurs d'envoyer des commandes à distance pour ajuster certains paramètres du moteur, favorisant une gestion proactive.

8. **Compatibilité Multi-Plateforme :** Assurer la compatibilité avec différentes plates-formes, notamment PC, tablettes et smartphones, pour permettre un accès flexible à l'interface de monitoring.

9. **Sécurité des Données :** Mettre en œuvre des mesures de sécurité robustes pour protéger les données sensibles du moteur et assurer la confidentialité des informations.

10. **Documentation Intégrée :** Intégrer une documentation interactive directement dans l'interface, fournissant des informations contextuelles sur les paramètres et les fonctions disponibles.

11. **Analyse en Temps Réel :** Intégrer des outils d'analyse en temps réel pour permettre aux utilisateurs de prendre des décisions informées en fonction des données du moteur en évolution constante.

12. **Compatibilité avec Systèmes d'Émulation :** Assurer la compatibilité avec des systèmes d'émulation pour faciliter le développement, les tests et la simulation sans nécessiter une connexion physique au moteur.

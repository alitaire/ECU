/*
 * globals.h
 *
 *  Created on: Feb 22, 2024
 *      Author: Bastien DELAUNAY
 */

#ifndef INC_GLOBALS_H_
#define INC_GLOBALS_H_

// includes
#include "stm32f4xx_hal.h"


// Definition des types
typedef uint8_t byte;


// Définition de macros
#define BIT_SET(a,b) ((a) |= (1U<<(b)))
#define BIT_CLEAR(a,b) ((a) &= ~(1U<<(b)))
#define BIT_CHECK(var,pos) !!((var) & (1U<<(pos)))
#define BIT_TOGGLE(var,pos) ((var)^= 1UL << (pos))
#define BIT_WRITE(var, pos, bitvalue) ((bitvalue) ? BIT_SET((var), (pos)) : bitClear((var), (pos)))


// Définition de la PIN MAP
#define PIN_INJ1		"PE15"
// TODO


// Position des bits pour l'état du moteur
#define BIT_ENGINE_RUN      0   // Engine running
#define BIT_ENGINE_CRANK    1   // Engine cranking
#define BIT_ENGINE_WARMUP   2   // Engine in warmup
#define BIT_ENGINE_ACC      3   // in acceleration mode
#define BIT_ENGINE_DCC      4   // in deceleration mode
#define BIT_ENGINE_UNUSED5  5
#define BIT_ENGINE_UNUSED6  6
#define BIT_ENGINE_UNUSED7  7

// Position des bits pour l'état des injecteurs
#define BIT_INJ_1     	0   // Injecteur 1
#define BIT_INJ_2    	1   // Injecteur 2
#define BIT_INJ_3     	2   // Injecteur 3
#define BIT_INJ_4     	3   // Injecteur 4
#define BIT_INJ_5     	4   // Injecteur 5
#define BIT_INJ_6     	5   // Injecteur 6
#define BIT_INJ_7     	6   // Injecteur 7
#define BIT_INJ_8     	7   // Injecteur 8

// Position des bits pour l'état des bobines
#define BIT_SPARK_1		0	// Bobine 1
#define BIT_SPARK_2		1	// Bobine 2
#define BIT_SPARK_3		2	// Bobine 3
#define BIT_SPARK_4		3	// Bobine 4
#define BIT_SPARK_5		4	// Bobine 5
#define BIT_SPARK_6		5	// Bobine 6
#define BIT_SPARK_7		6	// Bobine 7
#define BIT_SPARK_8		7	// Bobine 8


/* Structure utilisé pour stockées les valeurs "temps réel"
 * la taille de la structure est de 4 + 6 + 2x8 + 9 = 35 octets
 */

struct status {
	byte inits;			// etats de l'initialisation
	byte engine;		// etats du moteur (voir BIT_ENGINE_*)
	byte inj;			// etats des injecteurs (voir BIT_INJ_*)
	byte spark;			// etats des bobines (voir BIT_SPARK_*)

	byte idle;			// etats du ralenti (voir BIT_IDLE_*)
	byte boost;			// etats du boost (voir BIT_BOOST_*)
	byte fuel;			// etats du carburant (voir BIT_FUEL_*)
	byte fan;			// etats du ventilateur (voir BIT_FUEL_*)
	byte clutch;		// etats de l'embreyage (voir BIT_CLUTCH_*)
	byte lsu;			// etats de la sonde Lambda (voir BIT_LSU_*)

	uint16_t rpm;		// vitesse du moteur en tr/min
	uint16_t pwm1;		// temps d'injection 1 en uS
	uint16_t pwm2;		// temps d'injection 2 en uS
	uint16_t pwm3;		// temps d'injection 3 en uS
	uint16_t pwm4;		// temps d'injection 4 en uS
	uint16_t pwm5;		// temps d'injection 5 en uS
	uint16_t pwm6;		// temps d'injection 6 en uS
	uint16_t pwm7;		// temps d'injection 7 en uS
	uint16_t pwm8;		// temps d'injection 8 en uS

	uint8_t map_ext;	// valeur du map (Manifold Absolute Pressure)
	uint8_t oil_p;		// valeur de la pression d'huile moteur
	uint8_t fuel_p;		// valeur de la pression du carburant
	uint8_t tps;		// valeur du TPS (Throttle Position Sensor)
	uint8_t o2_ext;		// valeur de la sonde lambda
	uint8_t coolant;	// valeur de la temperature de liquide de reffroidissement
	uint8_t iat;		// valeur de l'IAT (Intake Air Temperature)
	uint8_t tacho;		// valeur du régime moteur
	uint8_t baro;		// valeur du baromètre

};

struct config {
	byte todo;			// TODO
};


// Définition des variable en externe pour utiliser dans les autres fichiers sources
extern struct status currentStatus;
extern struct config config1;


#endif /* INC_GLOBALS_H_ */

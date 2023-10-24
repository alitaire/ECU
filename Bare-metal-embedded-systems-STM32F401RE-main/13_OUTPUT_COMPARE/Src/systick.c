/*
 * systick.c
 *
 *  Created on: Feb 8, 2023
 *      Author: emasi
 */


#include "stm32f4xx.h"

#define SYSTICK_LOAD_VAL 			(16000)
#define CTRL_ENABLE					(1U << 0)
#define CTRL_CLK_SRC				(1U << 2)
#define CTRL_COUNTFLAG				(1U << 16)


void systickDelayMs(int delay) {
	/* Reload with number of clocks per millisec */
	SysTick->LOAD = SYSTICK_LOAD_VAL;

	/* Clear SysTick current value register */
	SysTick->VAL = 0;

	/* Enable SysTick and select internal clock source */
	SysTick->CTRL = CTRL_ENABLE | CTRL_CLK_SRC;

	for (int i = 0; i < delay; i++) {
		/* Wait until the COUNTFLAG is set */
		while ((SysTick->CTRL & CTRL_COUNTFLAG) == 0);
	}

	/* Reset the SysTick value */
	SysTick->CTRL = 0;
}

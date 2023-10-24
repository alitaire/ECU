/*
 * tim.c
 *
 *  Created on: Feb 16, 2023
 *      Author: emasi
 */

#include "stm32f4xx.h"

#define TIM2EN			(1U << 0)
#define CR1_CEN			(1U << 0)
#define OC_TOGGLE		((1U << 4) | (1U << 5))
#define CCER_CC1E		(1U << 0)

#define GPIOAEN			(1U << 0)

#define AFR5_TIM		(1U << 20)

void tim2_1hz_init(void) {
	// Enable clock access to TIM2
	RCC->AHB1LPENR |= TIM2EN;

	// Set pre-scaler value
	TIM2->PSC = 1600 - 1;	/* 16 000 000 / 1 600 = 10 000 */

	// Set auto-reload value
	TIM2->ARR = 10000 - 1;	/* 10 000 / 10 000 = 1 */

	// Clear counter
	TIM2->CNT = 0;

	// Enable timer
	TIM2->CR1 = CR1_CEN;
}

void tim2_PA5_output_compare(void) {
	// Enable clock access t GPIOA
	RCC->AHB1ENR |= GPIOAEN;

	// Set PA5 to alternate function
	GPIOA->MODER &=!(1U << 10);
	GPIOA->MODER |= (1U << 11);

	// Set alternate function type to TIM2_CH1
	GPIOA->AFR |= AFR5_TIM;

	// Enable clock access to TIM2
	RCC->AHB1LPENR |= TIM2EN;

	// Set pre-scaler value
	TIM2->PSC = 1600 - 1;	/* 16 000 000 / 1 600 = 10 000 */

	// Set auto-reload value
	TIM2->ARR = 10000 - 1;	/* 10 000 / 10 000 = 1 */

	// Set output compare toggle mode
	TIM2->CCMR1 = OC_TOGGLE;

	// Enable TIM2 Channel 1 in compare mode
	TIM2->CCER |= CCER_CC1E;

	// Clear counter
	TIM2->CNT = 0;

	// Enable timer
	TIM2->CR1 = CR1_CEN;
}

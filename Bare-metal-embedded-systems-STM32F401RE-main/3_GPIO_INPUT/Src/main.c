#include "stm32f4xx.h"

/*
 * B1 USER: the user button is connected to the I/O PC13 (pin 2) of the STM32 microcontroller.
 * B2 RESET: this push-button is connected to NRST, and is used to RESET the STM32 microcontroller.
 */

#define	GPIOAEN				(1U << 0)
#define GPIOCEN				(1U << 2)

#define PIN13				(1U << 13)
#define PIN5				(1U << 5)

#define LED_PIN				(PIN5)
#define BTN_PIN				(PIN13)

int main(void){
	// Enable clock to bus AHB1 GPIOA and GPIOC
	RCC->AHB1ENR |= GPIOAEN;
	RCC->AHB1ENR |= GPIOCEN;

	// Set PA5 as OUTPUT pin
	GPIOA->MODER |= (1U << 10);
	GPIOA->MODER &=~(1U << 11);

	// Set PC13 as INPUT pin
	GPIOC->MODER &=~(1U << 26);
	GPIOC->MODER &=~(1U << 27);

	while (1){
		// Check if button (BTN) is pressed
		if (GPIOC->IDR & BTN_PIN){
			// Turn LED on by assigning 1 to bit 5 (Setting)
			GPIOA->BSRR = (1U << 5);
		} else {
			// Turn of LED by assigning 1 to bit 21 (Resetting)
			GPIOA->BSRR = (1U << 21);
		}
	}

	return 0;
}

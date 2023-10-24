#include <stdint.h>

// Address of start of peripheral memory block
#define PERIPH_BASE				(0x40000000UL)
// Offset from peripheral memory block to AHB1 bus address
#define AHB1_PERIPH_OFFSET		(0x00020000UL)
// Address of the AHB1 memory block
#define AHB1_PERIPH_BASE		(PERIPH_BASE + AHB1_PERIPH_OFFSET)
// Offset to the GPIOA from the peripheral memory block
#define GPIOA_OFFSET			(0x0000UL)
// Address of start of the GPIOA memory block
#define GPIOA_BASE				(AHB1_PERIPH_BASE + GPIOA_OFFSET)

// RCC (Reseting Clock Control) module to enable bus to transport clock to GPIOA
#define RCC_OFFSET				(0x3800UL)
#define RCC_BASE				(AHB1_PERIPH_BASE + RCC_OFFSET)

// Set Pin 5 to HIGH
#define PIN5					(1U << 5)
#define LED_PIN					(PIN5)

// Set bit 0 to HIGH to enable clock access to the GPIOA
#define GPIOAEN					(1U << 0)

typedef struct {
	volatile uint32_t MODER;
	volatile uint32_t DUMMY[4];
	volatile uint32_t ODR;
} GPIO_TypeDef;

typedef struct {
	volatile uint32_t DUMMY[12];
	volatile uint32_t AHB1ENR;
} RCC_TypeDef;

#define RCC					((RCC_TypeDef*) RCC_BASE)
#define GPIOA				((GPIO_TypeDef*) GPIOA_BASE)

void ms_delay(int time);

int main(void){
	// 1. Enable clock access to GPIOA
	RCC->AHB1ENR |= GPIOAEN;

	// 2. Set PA5 as output pin
	GPIOA->MODER |= (1U << 10);
	GPIOA->MODER &=~(1U << 11);

	while (1){
		// 3. Set PA5 HIGH
		GPIOA->ODR ^= LED_PIN;
		// 4. Delay
		ms_delay(1000);
	}
}

void ms_delay(int time){
	unsigned int i, j;

	for (i = 0; i < time; i++){
		for (j = 0; j < 513; j++);
	}
}


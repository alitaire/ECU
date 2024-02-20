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
// Address offset of the RCC register from the RCC base address
#define RCC_AHB1EN_R_OFFSET		(0x30UL)
// Address of the RCC register
#define RCC_AHB1EN_R			(*(volatile unsigned int *)(RCC_BASE + RCC_AHB1EN_R_OFFSET))

// Address offset of the GPIO mode register from the GPIO Base address
#define MODE_R_OFFSET			(0x00UL)
// Address of the GPIOx mode register
#define GPIOA_MODE_R			(*(volatile unsigned int *)(GPIOA_BASE + MODE_R_OFFSET))

// Address offset to the output data register from the GPIOA base address
#define OD_R_OFFSET				(0x14UL)
// Address to the GPIOA output register
#define GPIOA_OD_R				(*(volatile unsigned int *)(GPIOA_BASE + OD_R_OFFSET))

// Set Pin 5 to HIGH
#define PIN5					(1U << 5)
#define LED_PIN					(PIN5)

// Set bit 0 to HIGH to enable clock access to the GPIOA
#define GPIOAEN					(1U << 0)

void ms_delay(int time);

int main(void){
	// 1. Enable clock access to GPIOA
	RCC_AHB1EN_R |= GPIOAEN;
	// 2. Set PA5 as output pin
	GPIOA_MODE_R |= (1U << 10);
	GPIOA_MODE_R &=~(1U << 11);

	while (1){
		// 3. Set PA5 HIGH
		GPIOA_OD_R ^= LED_PIN;
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


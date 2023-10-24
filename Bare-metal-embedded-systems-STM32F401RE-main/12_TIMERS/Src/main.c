#include <stdio.h>
#include "stm32f4xx.h"
#include "uart.h"
#include "adc.h"
#include "tim.h"

uint32_t sensor_value;

int main(void) {
	uart2_rxtx_init();
	pa1_adc_init();
	start_conversion();
	tim2_1hz_init();

	while (1) {
		/* Wait for UIF */
		while (!(TIM2->SR & SR_UIF));

		/* Clear UIF */
		TIM2->SR &=~ 1;

		sensor_value = adc_read();
		printf("Sensor value: %lu\n\r", sensor_value);
	}
}



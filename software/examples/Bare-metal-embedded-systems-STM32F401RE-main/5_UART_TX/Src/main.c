#include <stdint.h>
#include "stm32f4xx.h"

// Enables GPIOA
#define GPIOAEN				(1U << 0)
// Enables UART2 module from the APB1ENR
#define UART2EN				(1U << 17)
// Define symbolic name for the control register 1
#define CR1_TE				(1U << 3)
// Define symbolic name for UART enable
#define CR1_UE				(1U << 13)
// Define symbolic name for Status register TX empty
#define SR_TXE				(1U << 7)
// Defines the system frequency
#define SYS_FREQ			(16000000)
// No clock tree defined so using the default SYS_FREQ
#define APB1_CLK			(SYS_FREQ)
// Defines the UART baudrate
#define UART_BAUDRATE		(115200)

// Function declarations
static void uart_set_baudrate(USART_TypeDef * USARTx, uint32_t PeriphClk, uint32_t BaudRate);
static uint16_t compute_uart_bd(uint32_t PeriphClk, uint32_t BaudRate);
void uart2_tx_init(void);
void uart2_write(int ch);


int main(void) {
	uart2_tx_init();

	while (1) {
		uart2_write('Y');
	}
}

// TODO
//************ Configure UART GPIO pins *************
// 1. Enable clock access to GPIOA
// 2. Set PA2 mode to alternate function mode
// 3. Set PA2 alternate function type to UART_TX (AF07)

//************ Configure UART modules *************
// 1. Enable clock access to UART2
// 2. Configure baudrate
// 3. Configure the transfer direction
// 4. Enable UART module

void uart2_tx_init(void) {
	//************ Configure UART GPIO pins *************
	// 1. Enable clock access to GPIOA
	RCC->AHB1ENR |= GPIOAEN;

	// 2. Set PA2 mode to alternate function mode
	GPIOA->MODER &=~(1U << 4);
	GPIOA->MODER |= (1U << 5);

	// 3. Set PA2 alternate function type to UART_TX (AF07)
	GPIOA->AFR[0] |= (1U << 8);
	GPIOA->AFR[0] |= (1U << 9);
	GPIOA->AFR[0] |= (1U << 10);
	GPIOA->AFR[0] &=~(1U << 11);

	//************ Configure UART modules *************
	// 1. Enable clock access to UART2
	RCC->APB1ENR |= UART2EN;

	// 2. Configure baudrate
	uart_set_baudrate(USART2, APB1_CLK, UART_BAUDRATE);

	// 3. Configure the transfer direction (by using '=' deliberately)
	// 		- Sets 1 start bit, 8 data bits
	// 		- Disable hardware flow control
	// 		- Parity selection is even parity
	// 		- CR2 is already 00 so stop bit is 1 by default
	USART2->CR1 = CR1_TE;

	// 4. Enable UART module
	USART2->CR1 |= CR1_UE;
}

void uart2_write(int ch) {
	// Make sure transmit data is register is empty
	while(!(USART2->SR & SR_TXE));
	// Write to transmit data register
	USART2->DR = (ch & 0xFF);
}

static void uart_set_baudrate(USART_TypeDef * USARTx, uint32_t PeriphClk, uint32_t BaudRate) {
	USARTx->BRR = compute_uart_bd(PeriphClk, BaudRate);
}

static uint16_t compute_uart_bd(uint32_t PeriphClk, uint32_t BaudRate) {
	return ((PeriphClk + (BaudRate/2U))/BaudRate);
}

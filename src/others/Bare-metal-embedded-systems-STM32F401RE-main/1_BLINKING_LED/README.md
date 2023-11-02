# STM32F401RE Onboard LED Blink

This repository contains a C code driver for the STM32F401RE microcontroller to blink the onboard LED. The STM32F401RE is a Cortex-M4 based microcontroller with a wide range of features and peripheral options. 

## Getting Started

These instructions will guide you through the process of creating and uploading the code to blink the onboard LED on the STM32F401RE microcontroller.

### Prerequisites

Before getting started, you will need to have the following reference documents:
- [STM32F41x Datasheet](https://www.st.com/resource/en/datasheet/stm32f401re.pdf)
- [STM32F401xB/C Reference Manual](https://www.st.com/resource/en/reference_manual/dm00096844-stm32f401xb-c-and-stm32f401xd-e-advanced-arm-based-32-bit-mcus-stmicroelectronics.pdf)
- [STM32 Nucleo-64 Board User Manual](https://www.st.com/resource/en/user_manual/um1724-stm32-nucleo64-boards-mb1136-stmicroelectronics.pdf)

Also, you will need to have the following software installed on your computer:

- A GCC toolchain for ARM Cortex-M (such as [GNU Arm Embedded Toolchain](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm))
- An Integrated Development Environment (IDE) for ARM Cortex-M (such as [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html) or [Eclipse](https://www.eclipse.org/downloads/))
- A programmer/debugger for STM32F401RE (such as [ST-Link](https://www.st.com/en/development-tools/st-link-v2.html))

### Setting up the development environment

1. Install the GCC toolchain and the IDE of your choice on your computer.
2. Connect the programmer/debugger to your computer and to the STM32F401RE board.
3. Open the IDE and create a new project for the STM32F401RE microcontroller. 
4. Configure the project settings, such as the target microcontroller, the compiler, and the linker.
5. Create a new file in the project and name it "led_blink.c"

### Building and Uploading

1. Build the project by clicking on the "Build" button in the IDE.
2. Connect the programmer/debugger to the STM32F401RE board and power it on.
3. Upload the built code to the microcontroller using the programmer/debugger.

### Testing

Once the code is uploaded to the microcontroller, the onboard LED should start blinking. You can change the blink rate of the LED by modifying the delay time in the code.

## Contributing

We welcome contributions to this repository! If you have any improvements or bugfixes, please open a pull request.

## Contact

If you have any questions or feedback, please contact me at emasicollins@gmail.com

Please

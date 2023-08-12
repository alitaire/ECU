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
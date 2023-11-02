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

# Engine Knock and Pre-ignition Phenomena

## Definitions

- TDC (Top Dead Center) marks the highest point in the piston's motion within the cylinder.
- BDC (Bottom Dead Center) denotes the lowest point in the piston's motion within the cylinder.

Normal Combustion: Also referred to as deflagration, it is the controlled combustion process initiated by the spark plug.

Knocking Combustion: This type of combustion involves an explosion that occurs after the spark plug has fired, resulting in self-ignition. This can lead to engine damage.

Pre-ignition Combustion: Involving an explosion before the spark plug fires, pre-ignition can also cause engine damage due to the untimely ignition of the air-fuel mixture.

## Insights

Knocking and pre-ignition arise due to excessive temperatures within the cylinder, which prompt the air-fuel mixture to auto-ignite or cause glowing hot spots to ignite the mixture before the intended spark plug ignition (pre-ignition).

To mitigate these issues, utilizing higher octane fuel is a straightforward approach. Higher octane fuel offers greater resistance to knocking, reducing the chances of spontaneous combustion within the combustion chamber. Alternatively, maintaining an appropriate compression ratio for the engine can also be effective. The compression ratio is the ratio of the combustion chamber volume at BDC to that at TDC (BDC:TDC = compression ratio). The introduction of forced induction, such as turbochargers or other compressors, can elevate air temperatures due to compression, increasing the likelihood of knocks. Some turbocharged vehicles incorporate intercoolers to cool the incoming air, enhancing engine performance and diminishing knock potential. Lower compression ratios contribute to reduced air temperatures, facilitating the compatibility of a turbocharger.

Another strategy involves implementing a knock sensor, acting as a microphone to detect knocking. Following detection, the Engine Control Unit (ECU) analyzes specific frequencies, subsequently retarding the ignition timing of the spark plug in the subsequent cycle. The knock sensor, coupled with crankshaft angle data, determines the engine's pressure peak, inducing an ignition timing delay as a countermeasure.
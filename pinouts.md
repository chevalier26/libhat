# Pin Allocations for Each Module Team

Refer to https://pinout.xyz/pinout/wiringpi for arrangement. The project uses the Broadcom pin numbering.

## User Statistics Module
    None currently allocated pending final solution, tentatively GPIO 12
  
## Noise Level Response Module
    MCP 3008 - CH 7 (SPI) with logic level shifter

## Environmental Monitoring Modules
  
###  Temperature and Humidity Monitor 
    1-wire via GPIO 04 - DS18B20 Digital temperature sensor
    GPIO 17 - DHT 11 Digital Temperature and Humidity sensor

###  Light Level Monitor
    SPI using MCP 3008 - CH 2 through logic level shifter
  
###  Shock sensing
    I2C via SDA1 and SCL1 - MPU-6050 accelerometer and gyroscope

###  Gas detection
    SPI using MCP 3008 - CH 4 through logic level shifter - MQ 135 air quality sensor
    SPI using MCP 3008 - CH 5 through logic level shifter - MQ 2 methane, butane, LPG, smoke se
    
## Outputs
    GPIO 05 - relay output
    GPIO 06 - buzzer output
    GPIO 13 - Red of RGB LED
    GPIO 19 - Green of RGB LED
    GPIO 26 - Blue of RGB LED

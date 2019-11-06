# libhat
This is a project of the UP School of Library and Information Studies LIS 131 (Media Materials) course.

The code is meant for a Raspberry Pi and interfaces with external sensors using the GPIO to gather environmental and user data used for service improvement in heritage organisations.

*This project is still undergoing development and not suitable for beta, much less rollout.*

## Modules

### 1. User statistics module - Arvin Jason Aquino, Aldrin Ken Ong
   * Monitors monthly user figures (entering the main doors of the library)

### 2. Noise level response module
   * Monitors the noise level in a reading room and delivers a warning above threshold.

### 3. Environmental monitoring modules
####   3.1. Temperature and Humidity monitor - Dustin & Winston
   * Monitors temperature and humidity for preservation planning. Delivers a warning when exceeding set threshold.

####   3.2. Light level monitor - Marven Manzano
   * Triggers light fixtures to maintain a comfortable reading level in response to changes in natural lighting.
   * Monitors light levels for preservation planning. Delivers a warning when exceeding set threshold.

####   3.3. Shock sensing - Kyle Jemino, Lea Lite
   * Monitors occasional shocks and tremors for preservation planning, such as users bumping into bookshelves or a large book being slammed.
   *  Triggers an evacuation alarm or duck-cover-hold warning upon detection of continuous shocks.

####   3.4. Smoke detection - irisB., ltj., mcotiong
   *  Triggers an alarm upon detection of smoke.

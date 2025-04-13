# Safinity ESP32 MicroPython Code

This directory contains MicroPython code for ESP32 devices that work with the Safinity Android app via Bluetooth.

## Files

- `boot.py` - Initialization code that runs on ESP32 boot
- `main.py` - Main application code that handles Bluetooth communication with the Safinity app

## Hardware Requirements

- ESP32 development board
- Push button connected to GPIO0 (with pull-up resistor)
- LED connected to GPIO2 (optional, built-in LED on most ESP32 boards)

## Installation Instructions

1. Install [MicroPython on your ESP32](https://micropython.org/download/esp32/)
2. Upload these files to your ESP32 using a tool like [Thonny IDE](https://thonny.org/) or [ampy](https://github.com/scientifichackers/ampy)
3. Reset your ESP32 to start the Bluetooth service

## Usage

Once the code is running on your ESP32:

1. The ESP32 will advertise itself as "ESP32-Safinity" via Bluetooth
2. Pair the ESP32 with your Android device in the Bluetooth settings
3. Open the Safinity app and navigate to the Bluetooth screen
4. The app should automatically connect to the ESP32

## Button Functions

The code supports three types of button presses:

- **Single Press**: Sends a check-in message to the app
- **Double Press**: Sends a warning message to the app
- **Triple Press**: Sends an emergency message to the app

## Troubleshooting

- If the ESP32 is not connecting, make sure it's paired in your Android Bluetooth settings
- Check that the button is properly connected to GPIO0 with a pull-up resistor
- The LED on GPIO2 will blink to indicate connection status and button presses

## Customization

You can modify the code to change:

- Button pin (currently GPIO0)
- LED pin (currently GPIO2)
- Device name (currently "ESP32-Safinity")
- Button press timeout (currently 500ms)
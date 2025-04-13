# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)     # turn off vendor O/S debugging messages

# Connect to WiFi if needed
# import network
# station = network.WLAN(network.STA_IF)
# station.active(True)
# station.connect('SSID', 'PASSWORD')

# Disable automatic garbage collection for better performance
import gc
gc.collect()
gc.disable()
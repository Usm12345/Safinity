# Safinity ESP32 MicroPython Bluetooth Controller
import bluetooth
from machine import Pin, Timer
import time

# Configure the built-in LED
led = Pin(2, Pin.OUT)

# Configure button pins
button = Pin(0, Pin.IN, Pin.PULL_UP)  # Using GPIO0 as button input

# Button press tracking variables
last_press_time = 0
press_count = 0
press_timeout = 500  # ms to wait for additional presses

# Bluetooth setup
name = "ESP32-Safinity"  # Device name that will appear in Bluetooth scan
ble = bluetooth.BLE()
ble.active(True)
ble.config(gap_name=name)

# Service and characteristic UUIDs
SERVICE_UUID = bluetooth.UUID('1101')
CHAR_UUID = bluetooth.UUID('2101')

# Create service
service = ble.Service(SERVICE_UUID)

# Create characteristic for sending messages
char = service.characteristic(CHAR_UUID, bluetooth.NOTIFY | bluetooth.READ | bluetooth.WRITE)

# Register service
ble.add_service(service)

# Connection status
connected = False
conn_handle = None

# Bluetooth event callback
def bt_callback(event, data):
    global connected, conn_handle
    
    if event == bluetooth.IRQ_CENTRAL_CONNECT:
        conn_handle = data[0]
        connected = True
        print("Connected to:", conn_handle)
        # Blink LED to indicate connection
        blink_led(3, 100)
        # Send connected message
        send_message("connected")
        
    elif event == bluetooth.IRQ_CENTRAL_DISCONNECT:
        connected = False
        conn_handle = None
        print("Disconnected")
        # Restart advertising
        start_advertising()
        
    elif event == bluetooth.IRQ_GATTS_WRITE:
        # Handle incoming messages from the app
        handle, data = data
        message = data.decode().strip()
        print("Received:", message)
        
        # Process commands from the app
        if message == "led_on":
            led.on()
        elif message == "led_off":
            led.off()

# Register callback
ble.irq(bt_callback)

# Start advertising
def start_advertising():
    adv_data = bytearray(b'\x02\x01\x06') + bytearray([len(name) + 1, 0x09]) + name.encode()
    ble.gap_advertise(100, adv_data)
    print("Advertising as", name)

# Send message to connected device
def send_message(message):
    if connected and conn_handle is not None:
        try:
            char.write(message.encode())
            print("Sent:", message)
            return True
        except Exception as e:
            print("Error sending message:", e)
    return False

# Blink LED function
def blink_led(times, delay_ms):
    for _ in range(times):
        led.on()
        time.sleep_ms(delay_ms)
        led.off()
        time.sleep_ms(delay_ms)

# Button press handler
def handle_button_press():
    global press_count, last_press_time
    
    current_time = time.ticks_ms()
    
    # If it's been too long since the last press, reset counter
    if time.ticks_diff(current_time, last_press_time) > press_timeout and press_count > 0:
        # Process the completed press sequence
        if press_count == 1:
            print("Single press detected")
            send_message("button_press_1")
            blink_led(1, 100)
        elif press_count == 2:
            print("Double press detected")
            send_message("button_press_2")
            blink_led(2, 100)
        elif press_count == 3:
            print("Triple press detected")
            send_message("button_press_3")
            blink_led(3, 100)
        
        press_count = 0
    
    # Increment press count
    press_count += 1
    last_press_time = current_time

# Button debounce timer
debounce_timer = None

# Button interrupt handler
def button_callback(pin):
    global debounce_timer
    
    # Debounce logic
    if pin.value() == 0:  # Button pressed (active low)
        if debounce_timer is None:
            # Start debounce timer
            debounce_timer = Timer(0)
            debounce_timer.init(period=20, mode=Timer.ONE_SHOT, callback=lambda t: process_button())

# Process button press after debounce
def process_button():
    global debounce_timer
    debounce_timer = None
    handle_button_press()

# Set up button interrupt
button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

# Start advertising
start_advertising()

# Main loop
while True:
    # Check for timeout on button press sequence
    current_time = time.ticks_ms()
    if press_count > 0 and time.ticks_diff(current_time, last_press_time) > press_timeout:
        # Process the completed press sequence
        if press_count == 1:
            print("Single press detected")
            send_message("button_press_1")
            blink_led(1, 100)
        elif press_count == 2:
            print("Double press detected")
            send_message("button_press_2")
            blink_led(2, 100)
        elif press_count == 3:
            print("Triple press detected")
            send_message("button_press_3")
            blink_led(3, 100)
        
        press_count = 0
    
    # Small delay to prevent CPU hogging
    time.sleep_ms(10)
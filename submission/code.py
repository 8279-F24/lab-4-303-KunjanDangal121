"""
Student name: Kunjan Dangal
Date: 2024-10-08 
Description: This code allows the user to choose a color
(red, green, or blue) and gradually dims the LEDs on the
Circuit Playground by reducing their brightness until they
turn off. The program continuously asks for the user's input
and quits when the user presses 'q'.
"""

import time
from adafruit_circuitplayground import cp

# Function to gradually dim the LEDs
def dim_leds(color):
    max_value = 255
    while max_value > 0:
        for i in range(10):
            cp.pixels[i] = color
        cp.pixels.show()
        time.sleep(0.3)
        max_value -= 1
        color = (max_value if color[0] > 0 else 0,
                 max_value if color[1] > 0 else 0,
                 max_value if color[2] > 0 else 0)

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

# Loop for asking the user for color choices or quitting the program
while True:
    print("\nOption:")
    print("1. Red")      # Option 1 for red color
    print("2. Green")    # Option 2 for green color
    print("3. Blue")     # Option 3 for blue color
    print("Press 'q' to quit.")  # Option to quit the program

    user_input = input("Choose a color (1-3) or press 'q' to quit: ")

    # To check if the user wants to quit
    if user_input.lower() == 'q':
        print("Exiting the program.")  # Message before quitting
        break  # Exit the loop

    # Try to get a valid number from the user
    try:
        choice = int(user_input)  # Convert the input to an integer
        if choice == 1:
            print("Dimming Red LEDs...")  # Let the user know which color is selected
            dim_leds((255, 0, 0))  # Dim red color
        elif choice == 2:
            print("Dimming Green LEDs...")  # Notify user of the selection
            dim_leds((0, 255, 0))  # Dim green color
        elif choice == 3:
            print("Dimming Blue LEDs...")  # Notify user of the selection
            dim_leds((0, 0, 255))  # Dim blue color
        else:
            print("Invalid option. Please choose 1, 2, or 3.")  # Error for invalid choice
    except ValueError:
        print("Invalid input. Please enter a number (1-3) or 'q' to quit.")  # Handle non-numeric input

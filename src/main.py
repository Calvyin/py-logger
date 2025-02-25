from pynput import keyboard
import func as f


with keyboard.Listener(on_press=f.on_press) as listener:
    listener.join()

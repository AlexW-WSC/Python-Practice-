from pynput import keyboard
import random
import time
import asyncio





def empty_line():
    return {1: "-", 2: "-", 3: "-"}

line_1_index = empty_line()
line_2_index = empty_line()
line_3_index = empty_line()
line_4_index = empty_line()
line_5_index = empty_line()



catcher_position = 0


def on_press(key):
    global catcher_position
    if key == keyboard.Key.left:
        
        if catcher_position > 0:
            catcher_position -= 1
    
    if key == keyboard.Key.right:
        if catcher_position < 2:
            catcher_position += 1



listener = keyboard.Listener(on_press=on_press)
listener.start()


playing = True
while playing:
    
    time.sleep(1)
    print("-------------------------")

    
    print("", line_1_index[1], "  ", line_1_index[2], "  ", line_1_index[3])
    print("", line_2_index[1], "  ", line_2_index[2], "  ", line_2_index[3])
    print("", line_3_index[1], "  ", line_3_index[2], "  ", line_3_index[3])
    print("", line_4_index[1], "  ", line_4_index[2], "  ", line_4_index[3])
    print("", line_5_index[1], "  ", line_5_index[2], "  ", line_5_index[3])

    
    line_5_index = line_4_index
    line_4_index = line_3_index
    line_3_index = line_2_index
    line_2_index = line_1_index

  
    line_1_index = empty_line()
    line_1_index[random.randint(1, 3)] = "o"

    print(catcher_position)


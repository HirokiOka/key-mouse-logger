import time
import csv
from pynput import mouse, keyboard

dump_mouse_data = []
dump_key_data = []


# Mouse Event Handler
def on_mouse_move(x, y):
    str_time = time.strftime("%H:%M:%S")
    rounded_x = round(x, 2)
    rounded_y = round(y, 2)
    dump_mouse_data.append((str_time, "move", rounded_x, rounded_y))


def on_mouse_click(x, y, button, pressed):
    if (pressed):
        str_time = time.strftime("%H:%M:%S")
        rounded_x = round(x, 2)
        rounded_y = round(y, 2)
        dump_mouse_data.append((str_time, "click", rounded_x, rounded_y))


def on_mouse_scroll(x, y, dx, dy):
    str_time = time.strftime("%H:%M:%S")
    rounded_x = round(x, 2)
    rounded_y = round(y, 2)
    dump_mouse_data.append((str_time, "scroll", rounded_x, rounded_y))


# Key Event Handler
def on_key_pressed(key):
    str_time = time.strftime("%H:%M:%S")
    dump_key_data.append((str_time, key))


# Init Listeners
mouse_listener = mouse.Listener(
        on_move=on_mouse_move,
        on_click=on_mouse_click,
        on_scroll=on_mouse_scroll
        )
mouse_listener.start()

keyboard_listener = keyboard.Listener(
        on_press=on_key_pressed,
        )
keyboard_listener.start()


if __name__ == '__main__':

    while(True):
        try:
            pass
        except KeyboardInterrupt:
            mouse_listener.stop()
            keyboard_listener.stop()

            mouse_out_file = open('data/mouse_log.csv', 'w', newline='')
            mouse_out_writer = csv.writer(mouse_out_file)
            mouse_out_writer.writerow(["timestamp", "event", "mouseX", "mouseY"])
            for data_row in dump_mouse_data:
                mouse_out_writer.writerow(data_row)
            mouse_out_file.close()

            key_out_file = open('data/key_log.csv', 'w', newline='')
            key_out_writer = csv.writer(key_out_file)
            key_out_writer.writerow(["timestamp", "key"])
            for data_row in dump_key_data:
                key_out_writer.writerow(data_row)
            key_out_file.close()

            break

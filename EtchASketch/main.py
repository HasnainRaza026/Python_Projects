from turtle import Turtle, Screen
import keyboard

# t = Turtle()
# s = Screen()

# s.setup(width=600, height=600)


def on_key_event(event):
    event_type = event.event_type  # 'down' or 'up'
    key_name = event.name  # Name of the key, e.g., 'a', 'space', 'enter'
    print(f"Key {key_name} {event_type}")


keyboard.hook(on_key_event)
keyboard.wait('esc')

# s.mainloop()

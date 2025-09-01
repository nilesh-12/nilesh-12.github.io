import pyautogui
import time
import sys

def write_after_delay(d, sec):
    time.sleep(sec)
    pyautogui.write(d)

# Define coordinates (these will vary based on your screen and browser)

# Open browser and navigate (example, adjust as needed)
# pyautogui.hotkey('win', 'r')
# pyautogui.write('chrome')
# pyautogui.press('enter')
# time.sleep(3) # Wait for browser to open
# pyautogui.write('https://example.com/form')
# pyautogui.press('enter')
# time.sleep(5) # Wait for page to load

date_field_coords = (342, 358)
intime_field_coords = (755, 365)
outtime_button_coords = (879, 360)

coords = [
    date_field_coords,
    intime_field_coords,
    outtime_button_coords
]
d = [
    ("05082025","10:10","19:20"),
    ("06082025","10:10","19:20"),
    ("07082025","10:20","20:20"),
    ("08082025","10:10","19:20"),
    ("11082025","10:15","19:20"),
    ("12082025","10:10","19:20"),
    ("13082025","10:10","19:20"),
    ("19082025","10:10","21:00"),
    ("20082025","10:10","19:20"),
    ("21082025","10:10","19:20"),
    ("22082025","10:10","19:30"),
    ("23082025","10:10","19:15"),
    ("25082025","10:10","19:15"),
    ("26082025","10:25","19:35"),
    ("27082025","10:15","19:40"),
    ("28082025","10:00","19:20"),
    ("29082025","10:10","19:30"),
]

hist = {}

def print_position(user_input):
    if user_input.startswith('pos'):
        print("move your cursor to the position in 2 seconds")
        time.sleep(2)
        print(pyautogui.position())

def reset_coords(user_input):
    if user_input.startswith('reset co'):
        print("0 - date_field_coords")
        print("1 - intime_field_coords")
        print("2 - outtime_field_coords")
        coord_index = int(input("which one is needed to reset: "))
        print("move your cursor to the position in 2 seconds")
        time.sleep(2)
        point = pyautogui.position()
        print(point.x, point.y)
        print(f"Above point will set instead of {coords[coord_index]}")
        coords[coord_index] = (point.x, point.y)

while (user_input := input("Enter something (or 'q' to quit): ")) != 'q':
    if not user_input.startswith("print"):
        print_position(user_input)
        reset_coords(user_input)
        continue
    print(hist.keys())
    for i in range(len(d)):
        print(f"{i}: {d[i]} {f":{hist[i]}" if i in hist.keys() else ""}")
    index = int(input("Choose Record: "))

# Fill the form
# pyautogui.click(name_field_coords)
#pyautogui.hotkey("alt",'tab')
    time.sleep(2)
    for i, s in enumerate(d[index]):
        x,y = coords[i]
        print(f"Click: {x} {y}")
        pyautogui.click(x,y)
        time.sleep(0.5)
        pyautogui.click(x,y)
        # pyautogui.moveTo(x,y)
        # pyautogui.click()
        print(f"Write: {s}")
        pyautogui.press("home")
        write_after_delay(s, 1)
    print("Save")
    hist[index] = time.ctime()
# pyautogui.hotkey("ctrl",'s')
# after 2 seconds write 14082025 wait 2 seconds write 10:10 wait 2 seconds write 19:20 finish
# pyautogui.click(email_field_coords)
# pyautogui.write('john.doe@example.com')
#
# # Submit the form
# pyautogui.click(submit_button_coords)



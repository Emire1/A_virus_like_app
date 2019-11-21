import Multi_Object_Detect_Function as mod
from browsers_detector import open_link
from pyautogui import *
from time import sleep

testlist = ['chrome', 'firefox', 'edge', 'opera']

result_dict = mod.recieve_object(testlist)
print(result_dict)
for key, value in result_dict.items():
    left = value[0]
    right = value[1]
    top = value[2]
    bottom = value[3]
    print(key, value)
    if key == "chrome":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
    elif key == "firefox":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
    elif key == "edge":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
    elif key == "opera":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
sleep(2)
moveTo(average_width, average_height, duration=1)
doubleClick()
open_link("brockport.open.suny.edu")
press("enter")

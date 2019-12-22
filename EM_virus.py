from browsers_detector import *
from pyautogui import *
from time import sleep
url = "brockport.open.suny.edu"
message = "This is just a test so don't panic!"
detection = auto_detect_desktop()
if detection is False:
    # pyautogui.hotkey("win", "d")
    detection = auto_detect_desktop()
    if detection is False:
        detection = auto_detect_taskbar()
        if detection is False:
            open_with_start(url)
            send_email(message)
        else:
            keyDown("shift")
            click()
            sleep(.3)
            keyUp("shift")
            hotkey("ctrl", "tab")
            open_link(url)
            send_email(message)
    else:
        doubleClick()
        open_link(url)
        send_email(message)
else:
    doubleClick()
    open_link(url)
    send_email(message)

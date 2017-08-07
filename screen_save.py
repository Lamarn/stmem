import pyscreenshot as ImageGrab
import os.path
import datetime as dt
import time
import signal

exit_flag = False


def screenshot_loop(path):
    print("Entered screen loop. Taking picture every 10 seconds.")
    while (True):
        if exit_flag:
            print("Exiting screenshot loop.")
            return
        # Take screenshot
        im = ImageGrab.grab()
        # Save screenshot
        path_pic = path + str(dt.datetime.now()) + ".jpeg"
        im.save(open(path_pic, "w"))
        print("Saved picture: " + path_pic)
        # Wait 10 seconds
        time.sleep(10)


def signal_handler(signal, frame):
    global exit_flag
    exit_flag = True
    return


if __name__ == "__main__":
    print("shortTimeMemory started.")
    # Signal handeling
    signal.signal(signal.SIGINT, signal_handler)
    # Create path for pictures
    path = os.getcwd() + "/pics/"
    if not os.path.exists(path):
        os.makedirs(path)
    # Take screenshots
    screenshot_loop(path)
    print("Closing application.")

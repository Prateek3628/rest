from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
           title = "----Take Rest----",
           message = "Take rest or else you will rest in piece",
           app_icon = "C:\Users\APEX\Downloads\rest.png",
           timeout = 5)
        time.sleep(5)

import pyperclip
import datetime
import time

def add_to_clipboard():
    time = '{0:%m-%d %H:%M}'.format(datetime.datetime.now())
    pyperclip.copy(time)
    

if __name__ == '__main__':
    
    add_to_clipboard()
    second_time = int(time.time())
    delta_minute = 60 - (second_time % 60)
    time.sleep(delta_minute)
    
    while True:
        add_to_clipboard()
        time.sleep(60)
        
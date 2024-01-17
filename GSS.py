import psutil
import time
import sys

if len(sys.argv) < 2:
    print("Bitte einen Integer beim Starten mitgeben.")
else:
    s = int(sys.argv[1])
    print(f"Prozess wird für {s} Sekunden angehalten.")
    process_name = 'GTA5.exe'
    pid = 0

    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
            break

    if pid != 0:
        proc = psutil.Process(pid)
        proc.suspend()
        print ("Prozess pausiert")
        time.sleep(s)
        print ("Prozess fortgeführt")
        proc.resume()
    else:
        print("Prozess nicht gefunden")

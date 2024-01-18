import psutil
import time
import sys

s = 10

if len(sys.argv) >= 2:
    try:
        s = int(sys.argv[1])
    except ValueError:
        print("input is not a valid integer, time set to 10")
    
    
print(f"process will be paused for {s} seconds.")
process_name = 'GTA5.exe'
pid = 0

for proc in psutil.process_iter():
    if process_name in proc.name():
        pid = proc.pid
        break

if pid != 0:
    proc = psutil.Process(pid)
    proc.suspend()
    print ("process paused")
    time.sleep(s)
    print ("process continued")
    proc.resume()
else:
    print("process not found")

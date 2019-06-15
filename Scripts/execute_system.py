import subprocess
import os
while True:
    try:
        print("{0}~$: ".format(os.getcwd()))
        command = raw_input()
        subprocess.Popen(command, shell=True)
    except KeyboardInterrupt:
        break
        print("Program complete.")
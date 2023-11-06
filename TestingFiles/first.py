import subprocess
import os

print(os.getpid())
subprocess.run(["python3", "child.py"])
print(os.getpid())

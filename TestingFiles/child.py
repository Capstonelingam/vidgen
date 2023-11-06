import time
import os
start=time.time()
count=0
while True:
    end=time.time()
    if end-start>5:
        break
    count+=1

print(count)
print(os.getpid())


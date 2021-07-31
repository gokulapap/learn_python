# Progress bar with Python

## Progress bar 1

```
import time
import sys

toolbar_width = 30

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in range(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n")
# this ends the progress bar
```

## Progress bar 2

```
from time import sleep
from tqdm import tqdm
for i in tqdm(range(8)):
    sleep(0.4)
```

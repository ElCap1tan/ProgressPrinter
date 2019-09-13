# ProgressPriner

## Progress Bar:

![Code Examples](https://raw.githubusercontent.com/ElCap1tan/ProgressPrinter/master/docs/static/ProgressPrinterDemo_v0.1.1.gif)

### For the full example see examples.py
#### This will be edited in the next days to make things clearer.

```Python
from time import sleep
import requests

from ProgressBar import ProgressBar
```
```Python
def ex1():
    pb1 = ProgressBar(100, '%', pre='Downloading file', post='Download finished', length=25)
    pb1.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 101):
        pb1.print_progress(mb)
        sleep(0.15)
```
```
Downloading file
[========================>] - Finished 100 % of 100 %
Download finished
```
```Python
def ex2():
    pb2 = ProgressBar(500, 'MB', pre='Downloading file', post='Download finished', head='#')
    pb2.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 501):
        pb2.print_progress(mb)
        sleep(0.02)
```
```
Downloading file
[=================================================#] - Finished 500 MB of 500 MB
Download finished
```
```Python
def ex3():
    pb3 = ProgressBar(1000.12, 'MB', pre='Downloading file', post='Download finished', length=100)
    pb3.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 1001):
        if mb != 1000 and mb % 2 == 0:
            mb = mb + 0.5
        elif mb != 1000:
            mb = mb + 0.25
        else:
            mb = mb + 0.12
        pb3.print_progress(mb)
        sleep(0.025)
```
```
Downloading file
[===================================================================================================>] - Finished 1000.12 MB of 1000.12 MB
Download finished
```
```Python
def ex4():
    pb4 = ProgressBar(5, 'files', pre='Deleting files', post='Finished!', length=25, empty='*', fill='#')
    pb4.print_progress()  # Prints the initial empty progress bar
    for file in range(1, 6):
        pp4.print_progress(file, pre="Deleting file file{}.txt".format(file))
        sleep(1)
```
```
Deleting files
Deleting file file1.txt
Deleting file file2.txt
Deleting file file3.txt
Deleting file file4.txt
Deleting file file5.txt
[########################>] - Finished 5 files of 5 files
Finished!
```
```Python
def ex5():
    with open('example.txt', 'r') as f:
        pb5 = ProgressBar(len(f.readlines()), 'lines', pre="Reading lines from file {}".format(f.name), post='Finished reading file!')
        f.seek(0)  # Return to start of line after obtaining line count
        pb5.print_progress()  # Prints the initial empty progress bar
        for lineno, line in enumerate(f, start=1):
            pb5.print_progress(lineno, pre=line.replace('\n', ''))
            sleep(1)
```
```
Reading lines from file example.txt
Line 1
Line 2
Line 3
Line 4
...
[=================================================>] - Finished 5 lines of 5 lines
Finished reading file!
```
```Python
def ex6():
    link = 'https://speed.hetzner.de/100MB.bin'
    file_name = '100MB.bin'
    with open(file_name, 'wb') as f:
        response = requests.get(link, stream=True)
        total_length = int(response.headers.get('content-length'))
        if total_length is None:
            f.write(response.content)
        else:
            pb6 = ProgressBar(total_length, 'Bytes', pre='Downloading {} from {}'.format(file_name, link),
                                  post='Finished download!')
            pb6.print_progress()
            progress = 0
            for chunk in response.iter_content(chunk_size=int(total_length/100)):
                progress += len(chunk)
                f.write(chunk)
                pb6.print_progress(progress)
```
```
Downloading 100MB.bin from https://speed.hetzner.de/100MB.bin
[=================================================>] - Finished 104857600 Bytes of 104857600 Bytes  
Finished download!
```

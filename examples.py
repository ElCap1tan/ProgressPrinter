from time import sleep
import requests

from ProgressPrinter import ProgressPrinter


def main():
    # Choose the examples to run here
    ex1()
    ex2()
    ex3()
    ex4()
    ex5()
    # ex6()  # This will start a real download of 100 MB. If you want to save space make sure to delete the file after this


def ex1():
    pp1 = ProgressPrinter(100, '%', pre='Downloading file', post='Download finished', length=25)
    pp1.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 101):
        pp1.print_progress(mb)
        sleep(0.15)


def ex2():
    pp2 = ProgressPrinter(500, 'MB', pre='Downloading file', post='Download finished', head='#')
    pp2.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 501):
        pp2.print_progress(mb)
        sleep(0.02)


def ex3():
    pp3 = ProgressPrinter(1000.12, 'MB', pre='Downloading file', post='Download finished', length=100)
    pp3.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 1001):
        if mb != 1000 and mb % 2 == 0:
            mb = mb + 0.5
        elif mb != 1000:
            mb = mb + 0.25
        else:
            mb = mb + 0.12
        pp3.print_progress(mb)
        sleep(0.025)


def ex4():
    pp4 = ProgressPrinter(5, 'files', pre='Deleting files', post='Finished!', length=25, empty='*', fill='#')
    pp4.print_progress()  # Prints the initial empty progress bar
    for file in range(1, 6):
        pp4.print_progress(file, pre="Deleting file file{}.txt".format(file))
        sleep(1)


def ex5():
    with open('example.txt', 'r') as f:
        pp5 = ProgressPrinter(len(f.readlines()), 'lines', pre="Reading lines from file {}".format(f.name), post='Finished reading file!')
        f.seek(0)  # Return to start of line after obtaining line count
        pp5.print_progress()  # Prints the initial empty progress bar
        for lineno, line in enumerate(f, start=1):
            pp5.print_progress(lineno, pre=line.replace('\n', ''))
            sleep(1)


def ex6():
    link = 'https://speed.hetzner.de/100MB.bin'
    file_name = '100MB.bin'
    with open(file_name, 'wb') as f:
        response = requests.get(link, stream=True)
        total_length = int(response.headers.get('content-length'))
        if total_length is None:
            f.write(response.content)
        else:
            pp6 = ProgressPrinter(total_length, 'Bytes', pre='Downloading {} from {}'.format(file_name, link),
                                  post='Finished download!')
            pp6.print_progress()
            progress = 0
            for chunk in response.iter_content(chunk_size=int(total_length/100)):
                progress += len(chunk)
                f.write(chunk)
                pp6.print_progress(progress)


if __name__ == '__main__':
    main()

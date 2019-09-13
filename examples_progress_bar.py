#!/usr/bin/env python

from time import sleep

from ProgressPrinter import ProgressBar


def main():
    """
    Choose which examples to run in this method
    """

    ex1()
    ex2()
    ex3()
    ex4()
    ex5()


def ex1():
    """
    **Example 1**
    ::
        pb1 = ProgressBar(100, '%', pre='Downloading file', post='Download finished', length=25)
        pb1.print_progress()  # Prints the initial empty progress bar
        for mb in range(1, 101):
            pb1.print_progress(mb)
            sleep(0.15)

    **Output:**
    ::
        Downloading file

        [========================>] - Finished 100 % of 100 %

        Download finished

    """

    pb1 = ProgressBar(100, '%', pre='Downloading file', post='Download finished', length=25)
    pb1.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 101):
        pb1.print_progress(mb)
        sleep(0.15)


def ex2():
    """
    **Example 2**
    ::
        pb2 = ProgressBar(500, 'MB', pre='Downloading file', post='Download finished', head='#')
        pb2.print_progress()  # Prints the initial empty progress bar``
        for mb in range(1, 501):
            pb2.print_progress(mb)
            sleep(0.02)

    **Output:**
    ::
        Downloading file
        [=================================================#] - Finished 500 MB of 500 MB
        Download finished

    """

    pb2 = ProgressBar(500, 'MB', pre='Downloading file', post='Download finished', head='#')
    pb2.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 501):
        pb2.print_progress(mb)
        sleep(0.02)


def ex3():
    """
    **Example 3**
    ::
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


    **Output:**
    ::
        Downloading file
        [===================================================================================================>] - Finished 1000.12 MB of 1000.12 MB
        Download finished

    """

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


def ex4():
    pb4 = ProgressBar(5, 'files', pre='Deleting files', post='Finished!', length=25, empty='*', fill='#')
    pb4.print_progress()  # Prints the initial empty progress bar
    for file in range(1, 6):
        pb4.print_progress(file, pre="Deleting file file{}.txt".format(file))
        sleep(1)


def ex5():
    with open('example.txt', 'r') as f:
        pb5 = ProgressBar(len(f.readlines()), 'lines', pre="Reading lines from file {}".format(f.name), post='Finished reading file!')
        f.seek(0)  # Return to start of line after obtaining line count
        pb5.print_progress()  # Prints the initial empty progress bar
        for lineno, line in enumerate(f, start=1):
            pb5.print_progress(lineno, pre=line.replace('\n', ''))
            sleep(1)


if __name__ == '__main__':
    main()

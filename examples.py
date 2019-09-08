from time import sleep

from ProgressPrinter import ProgressPrinter


def ex1():
    pp1 = ProgressPrinter(10, 'MB', pre='Downloading file', post='Download finished', length=25, head='#')
    pp1.print_progress()  # Prints the initial empty progress bar
    for mb in range(1, 11):
        pp1.print_progress(mb)
        sleep(0.3)


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
        sleep(0.05)


def ex4():
    pp4 = ProgressPrinter(5, 'files', pre='Deleting files', post='Finished!', length=25, empty='*', fill='#')
    pp4.print_progress()  # Prints the initial empty progress bar
    for file in range(1, 6):
        pp4.print_progress(file, pre="Deleting file file{}.txt".format(file))
        sleep(1)


def main():
    ex1()
    ex2()
    ex3()
    ex4()


if __name__ == '__main__':
    main()

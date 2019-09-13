#!/usr/bin/env python

import requests

from ProgressPrinter import ByteProgressBar


def main():
    ex1()


def ex1():
    # The ByteProgressBar is a extension of the normal progress bar that supports automatic unit conversion
    # from bytes, the base unit you will work with most of the time, to KB, MB, etc.
    # This for example is useful when downloading or working with a file (see example below)
    #
    # UNCOMMENT THE LINK YOU WANT TO USE FOR THE TEST DOWNLOAD
    # -------------------------------------------------------
    # 100MB.bin [100 MB] - Auto conversion to MB
    link = 'https://speed.hetzner.de/100MB.bin'
    # -------------------------------------------------------------------------------------------
    # Linux Mint Cinnamon x64.iso [ca. 1.87 GB] - Auto conversion to GB
    # link = 'http://mirrors.evowise.com/linuxmint/stable/19.2/linuxmint-19.2-cinnamon-64bit.iso'
    # -------------------------------------------------------------------------------------------

    file_name = link.split('/')[-1]
    with open(file_name, 'wb') as f:
        response = requests.get(link, stream=True)
        byte_size = int(response.headers.get('content-length'))
        if byte_size is None:
            f.write(response.content)
        else:
            # Set to ByteProgressBar.UNITS.AUTO to automatically interfere a fitting unit from the byte size
            # -----------------------------------------------------------------------------------------------
            # Supported values: ByteProgressBar.UNITS.{BYTES, KILOBYTES, MEGABYTES, GIGABYTES, TERABYTES, AUTO}

            bpb1 = ByteProgressBar(byte_size, ByteProgressBar.UNITS.AUTO, pre='Downloading {} from {}'
                                   .format(file_name, link), post='Finished download!')
            bpb1.print_progress()
            loaded_bytes = 0
            for chunk in response.iter_content(chunk_size=1048576):  # 1 MB
                loaded_bytes += len(chunk)
                f.write(chunk)
                bpb1.print_progress(loaded_bytes)


if __name__ == '__main__':
    main()

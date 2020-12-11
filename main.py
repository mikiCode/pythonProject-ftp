import ftplib
from time import time

from ftp_threading import GetFilesFromFTP

# FTP_HOST = "217.153.206.237"
# FTP_USER = "Canalplus"
# FTP_PASS = "Canalplus2012"
# FTP_CWD = "/home/Canalplus"
# FILE_EXT = ".mxf"

FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser@dlptest.com"
FTP_PASS = "eUj8GeW55SvYaswqUyDSm5v6N"
FTP_CWD = "/"
FILE_EXT = ".jpg"

FTP_CHDIR = "C:\\Users\\Miko\\PycharmProjects\\pythonProject"


def multi_input():
    try:
        while True:
            data = input()
            if not data:
                break
            yield data
    except KeyboardInterrupt:
        return


files = list(multi_input())
files = [file + FILE_EXT for file in files]

threads = list()

if __name__ == '__main__':
    t = []
    start = time()
    try:
        for file in files:
            t = GetFilesFromFTP(file, name=file)
            threads.append(t)
            # print("Starting thread to download {}".format(file))
            t.start()

        for thread in threads:
            t.join()
            # print("Thread {} is finished, joining back to main thread...".format(thread.name))
        print("All threads finished, total {} seconds...".format(round(time() - start), 2))

    except ftplib.all_errors as e:
        print('FTP error:', e)

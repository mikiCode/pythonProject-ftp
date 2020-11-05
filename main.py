import ftplib
from os import chdir
from threading import Thread
from time import time

FTP_HOST = "217.153.206.237"
FTP_USER = "Canalplus"
FTP_PASS = "Canalplus2012"
FTP_CWD = "/home/Canalplus"
FTP_CHDIR = "C:\\Users\\Miko\\PycharmProjects\\pythonProject"

threads = list()


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
files = [file + '.mxf' for file in files]
print(files)


class GetFilesFromFTP(Thread):
    def __init__(self, file, name=None):
        super().__init__()
        self.file = file
        self.name = name

    def run(self):
        print(f"Downloading {self.file}")
        with open(self.file, 'wb') as file_download:
            ftp.retrbinary(f"RETR {file_download}", file_download.write)


if __name__ == '__main__':
    start = time()
    with ftplib.FTP(FTP_HOST) as ftp:
        try:
            ftp.login(FTP_USER, FTP_PASS)
            ftp.cwd(FTP_CWD)
            chdir(FTP_CHDIR)
            for file in files:
                t = GetFilesFromFTP(file, name=file)
                threads.append(t)
                print(f"Starting thread to download{file}")
                t.start()

            for thread in threads:
                t.join()
                print("Thread {} is finished, joining back to main thread...".format(thread.name))
                print("All threads finished, total {} seconds...".format(time() - start))

        except ftplib.all_errors as e:
            print('FTP error:', e)

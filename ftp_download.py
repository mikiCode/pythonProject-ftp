import ftplib
import sys
from ftplib import FTP
from os import chdir




FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser@dlptest.com"
FTP_PASS = "eUj8GeW55SvYaswqUyDSm5v6N"
FTP_CWD = "/"
FILE_EXT = ".jpg"
FTP_CHDIR = "C:\\Users\\Miko\\PycharmProjects\\pythonProject"


def ftp_downloader(filename):
    with FTP(FTP_HOST, FTP_USER, FTP_PASS) as ftp_client:
        ftp_client.cwd(FTP_CWD)
        try:
            # Checks for file size, else it quits the thread
            if ftp_client.size(filename) >= 0:
                print(f'File `{filename}` has {round(ftp_client.size(filename) / 1048576, 2)} MB')
            else:
                sys.exit()
        except ftplib.error_perm:
            print(f"Brak pliku `{filename}` na ftp")
            sys.exit()
        except ftplib.error_temp:
            pass
        # save the downloads to the specified windows directory.
        chdir(FTP_CHDIR)

        with open(filename, "wb") as file:
            # write the binary to the file.
            # note that file.write is not file.write().
            ftp_client.retrbinary(f"RETR {filename}", file.write)

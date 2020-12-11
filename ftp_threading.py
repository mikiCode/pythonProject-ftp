from threading import Thread

from ftp_download import ftp_downloader


# sub class of Thread
class GetFilesFromFTP(Thread):
    def __init__(self, filename, name=None):
        super().__init__()

        self.filename = filename
        self.name = name

    # overriding the run method of Thread class
    def run(self):
        ftp_downloader(self.filename)

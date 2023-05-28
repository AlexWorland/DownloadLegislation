import os
from multiprocessing import Pool


def main():
    with open('legislationWebsites.txt', 'r') as f:
        # download every line in the file using multithreading
        with Pool(100) as p:
            p.map(download, f.readlines())
        
def download(line):
    os.system('wget -l inf -r -np -k -p -nc --no-check-certificate -P /Volumes/NetBackup/legislation/ ' + line)        

if __name__ == '__main__':
    main()

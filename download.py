import os
import threading

def main():
    with open('legislationWebsites.txt', 'r') as f:
        # download every line in the file using multithreading
        threads = []
        for line in f:
            t = threading.Thread(target=download, args=(line,))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

def download(line):
    os.system('wget -l inf -r -np -k -p -nc --no-check-certificate ' + line)        

if __name__ == '__main__':
    main()

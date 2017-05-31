import requests
import os
from threading import Thread

def startWebsite():
    print ("got it")
    if __name__ == "__main__":
        cwd = os.path.join(os.getcwd(), "website.py")
        os.system('{} {}'.format('python', cwd))


websiteThread = Thread(target=startWebsite)
websiteThread.start()
# DO stuff here
print ("kom hit")
#
websiteThread.join()

import threading
import IO
import StringHandler as sh
import time

from time import ctime, sleep


def multiDownload(date):
    threads = []
    path = 'DataBase_' + date.__str__()
    for x in sh.lists:
        threads.append(threading.Thread(target=IO.write, args=(path + '\\' + x + '.xlsx', x)))
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("Download finished\n")


if __name__ == '__main__':
    print("timer started:%s" % time.clock())
    multiDownload(20151127)
    print("timer ended:\nTotal time:%s" % time.clock())

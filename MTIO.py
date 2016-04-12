import threading
import time
import IO
import StringHandler as Sh


def multi_download(date):
    threads = []
    path = 'DataBase_' + date.__str__()
    for x in Sh.lists:
        threads.append(threading.Thread(target=IO.download, args=(path + '\\' + x + '.xlsx', x)))
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()
    print("Download finished\n")


if __name__ == '__main__':
    print("timer started:%s" % time.clock())
    multi_download(20151203)
    print("timer ended:\nTotal time:%s" % time.clock())

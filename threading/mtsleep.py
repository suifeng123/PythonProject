#!/usr/bin/env python
import threading
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args
    def __call__(self):
        self.func(*self.args)
def loop(nloop,nsec):
        self.func(*self.args)
def loop(nloop,nsec):
        self.func(*self.args)
#!/usr/bin/env python
import threading
#!/usr/bin/env python
import threading
from time import sleep,ctime

loops = [4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name = name
        self.func = func
        self.args = args
    def __call__(self):
        self.func(*self.args)
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'end loop',nloop,'at:',ctime()
def main():
    print 'starting at:',ctime()
    threads =[]
    nloops = range(lens(threads))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)
    for i in loops:#start all thread
        threads[i].start()
    for i in nloops: #wait for completion
        threads[i].join()
    print 'all Done at:',ctime()
if __name__=="__main__":
    main()
#!/usr/bin/env python
import thread
from time import sleep,ctime

def loop0():
    print 'start loop 0 at:',ctime()
    sleep(4)
    print 'end loop 0 at:',ctime()
def looo1():
    print 'start loop1 at',ctime()
    sleep(2)
    print 'end loop1 at',ctime()
    
def main():
    print 'start at',ctime()
    thread.start_new_thread(loop0, ())
    thread.start_new_thread(looo1, ())
    sleep(6)
    print 'all done at',ctime()
    
if __name__=='main':
    main()
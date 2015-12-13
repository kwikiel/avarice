#!/usr/bin/env python2.7
#coding: utf-8

import gevent
import gevent.pool
from gevent import monkey
from getloans import loan_byid

monkey.patch_all()
class TestPool(object):

    def __init__(self, maxsize=2):
        self.pool = gevent.pool.Pool(maxsize)

    def run(self):
        for i in xrange(20000):
            gworker = gevent.spawn(self._worker, i)
            self.pool.add(gworker)
            print('sizeof pool is %d' % (len(self.pool),))
            print('worker %d in? %r' % (i, gworker in self.pool))

        # The only thing I added
        self.pool.join()
        print('All tasks done.')


    def _worker(self, pid):
        print('My pid is %d' % (pid,))
        loan_byid(pid)
        print('%d has done.' % (pid,))



if __name__ == '__main__':
    test = TestPool()
    test.run()

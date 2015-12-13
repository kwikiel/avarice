from gevent.pool import Pool
from gevent import monkey
from getinvestments import investment_byloan
monkey.patch_all()


def papiez(uid):
    print 'start', uid
    investment_byloan(uid)
    print 'finish', uid
pool = Pool(200)


for u in range(20000,22000):
    pool.spawn(papiez, u)

print 'joining...'
pool.join()

#Import proper function
#Get latest ID from DB
#Start getting consecutive IDs

from getinvestments import investment_byloan

for i in range(20000, 22000):
    try:
        investment_byloan(i)
        print "[{0}] Parsing".format(str(i))
    except ValueError:
        print "[{1}] Failed".format(str(i))


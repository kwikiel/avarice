import requests
import datetime

from models import Investment
from models import db


def parse_date(datestr):
    '''
    Helper function for parsing dates
    '''
    try:
        datetime.datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S').date()
    except:
        datetime.datetime.strptime(datestr[:-10], '%Y-%m-%dT%H:%M:%S').date()


def investment_byloan(lid):
    '''
    Get investment by loan ID
    '''
    try:
        r = requests.get("https://api.loanbase.com/api/investments/"+str(lid))
    except:
        print("Cannot get data from API")
    if r.json()['investments']:
        try:
                for i in r.json()['investments']:
                    inv = Investment(
                        id=int(i['id']),
                        amount=float(i['amount']),
                        dateInvested=parse_date(i['dateInvested']),
                        rate=float(i['rate']),
                        loanId=int(i['loanId']),
                        investorId=int(i['investorId']))
                    try:
                        db.session.add(inv)
                        db.session.commit()
                    except:
                        db.session.rollback()
        except:
            print("Prolly empty {0}".format(lid))

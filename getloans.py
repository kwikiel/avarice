# Parse loans into loans database
import datetime
import requests

from models import Loan
from models import db
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

def parse_date(datestr):
    try:
        datetime.datetime.strptime(datestr, '%Y-%m-%dT%H:%M:%SZ').date()
    except:
        datetime.datetime.strptime(datestr[:-10], '%Y-%m-%dT%H:%M:%S').date()

def loan_byid(lid):
    try:
        raw = requests.get("https://api.loanbase.com/api/loan/"+str(lid))
        pl = raw.json()['loans'][0]
        l = Loan(
            id=pl['id'],
            type=pl['type'],
            title=pl['title'],
            description=pl['description'],
            amount=float(pl['amount']),
            term=int(pl['term']),
            frequency=int(pl['frequency']),
            status=pl['status'],
            paymentStatus=pl['paymentStatus'],
            createdAt=parse_date(pl['createdAt']),
            expirationDate=parse_date(pl['expirationDate']),
            denomination=pl['denomination'],
            percentFunded=float(pl['percentFunded']),
            votes=int(pl['votes']),
            borrower=int(pl['borrower']))
        db.session.add(l)
        db.session.commit()
    except:
        db.session.rollback()
        logger.exception("Cannot get ID")

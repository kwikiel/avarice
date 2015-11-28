# Parse loans into loans database
import datetime
import requests
from models import Loan
from models import db

DATAFORMAT = "%Y-%m-%dT%H:%M:%SZ"


def loan_byid(lid):
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
        createdAt=datetime.datetime.strptime(pl['createdAt'], DATAFORMAT)
        .date(),
        expirationDate=datetime.datetime.strptime(pl['expirationDate'], DATAFORMAT)
        .date(),
        denomination=pl['denomination'],
        percentFunded=float(pl['percentFunded']),
        votes=int(pl['votes']),
        borrower=int(pl['borrower']))

    db.session.add(l)
    db.session.commit()

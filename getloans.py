# Parse loans into loans database

import requests
from models import Loan
from models import db


def loan_byid(lid):
    raw = requests.get("https://api.loanbase.com/api/loan/"+str(lid))
    pl = raw.json()['loans'][0]
    l = Loan(
        id=pl['id'],
        type=pl['type'],
        description=pl['description'],
        amount=float(pl['amount']),
        term=int(pl['amount'])
    )
    db.session.add(l)
    db.session.commit()

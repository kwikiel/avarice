from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kacper:password@localhost/ostr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Globus(db.Model):
    __tablename__ = 'globuses'

    id = db.Column(db.Integer, primary_key=True)
    bitbond = db.Column(db.String(140))
    loanbase = db.Column(db.String(140))
    btcjam = db.Column(db.String(140))
    getline = db.Column(db.String(140))




class User(db.Model):


    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    social_facebook = db.Column(db.Integer())
    social_linkedin = db.Column(db.Integer())
    social_google = db.Column(db.Integer())
    trusted_paypal = db.Column(db.Integer())
    trusted_amazon = db.Column(db.Integer())
    trusted_localbitcoins = db.Column(db.Integer())
    trusted_ebay = db.Column(db.Integer())
    countryId = db.Column(db.String(140))
    salary = db.Column(db.String(140))
    activeToRepaid = db.Column(db.Float())
    image = db.Column(db.String(430))  # URL for image or file

    def __init__(self, social_facebook,
                 social_linkedin,
                 social_google,
                 trusted_paypal,
                 trusted_amazon,
                 trusted_localbitcoins,
                 trusted_ebay,
                 countryId, salary, image):
        self.social_facebook = social_facebook
        self.social_linkedin = social_linkedin
        self.trusted_paypal = trusted_paypal
        self.trusted_amazon = trusted_amazon
        self.trusted_localbitcoins = trusted_localbitcoins
        self.trusted_ebay = trusted_ebay
        self.countryId = countryId
        self.salary = salary
        self.image = image

    def __repr(self):
        return "<user {0}>".format(self.social_facebook)


class Loan(db.Model):
    __tablename__ = 'loans'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(1200))
    title = db.Column(db.String(1200))
    description = db.Column(db.String(9000))
    amount = db.Column(db.Float())
    term = db.Column(db.Integer())
    frequency = db.Column(db.Integer())
    status = db.Column(db.String(140))
    paymentStatus = db.Column(db.String(140))
    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    expirationDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    denomination = db.Column(db.String(40))
    percentFunded = db.Column(db.Float())
    votes = db.Column(db.Integer())
    borrower = db.Column(db.Integer)

    def __init__(self,
                 id,
                 type,
                 title,
                 description,
                 amount,
                 term,
                 frequency,
                 status,
                 paymentStatus,
                 createdAt,
                 expirationDate,
                 denomination,
                 percentFunded,
                 votes,
                 borrower,
                 ):
                    self.id = id
                    self.type = type
                    self.title = title
                    self.description = description
                    self.amount = amount
                    self.term = term
                    self.frequency = frequency
                    self.status = status
                    self.paymentStatus = paymentStatus
                    self.createdAt = createdAt
                    self.expirationDate = expirationDate
                    self.denomination = denomination
                    self.percentFunded = percentFunded
                    self.borrower = borrower

    def __repr__(self, id):
        return '<Loan %r>' % self.id


class Investment(db.Model):
    __tablename__ = 'investments'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    dateInvested = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    investorId = db.Column(db.Integer())
    rate = db.Column(db.Float())
    loanId = db.Column(db.Integer())

    def __repr__(self):
        return '<Investment {0.id} {0.loanId}>'.format(self)

import requests
import logging
from time import gmtime, strftime
# secret = 'uhmm secret? xD'
LOG_FILENAME = 'history.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)


class Investor:

    def __init__(self, secret, investor_id):
        self.secret = secret
        self.investor_id = investor_id

    def list():
        '''
        Listing own investments (may be slow due to no api for that)
        '''
        # Query list of investments where investor invested
        pass

    def details():
        '''
        Details on given investment
        '''
        pass

    def create(self, lid, amount, rate):
        '''
        Investing in given loans

        '''
        url = "https://api.loanbase.com/api/investment"
        params = {'loan_id': lid, 'amount': amount, 'rate': rate}
        headers = {
            'Authorization': 'Bearer ' + self.secret,
            'Accept': 'application/vnd.blc.v1+json',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        resp = requests.post(url, data=params, headers=headers)
        info = "Investing LID: {0}, Amount: {1}, Rate: {2}"\
            .format(lid, amount, rate)
        logging.info(strftime("%Y-%m-%d %H:%M:%S", gmtime())+info)
        print(resp.text)

    def modify():
        '''
        Modify investment (have to know id)
        '''
        pass

    def delete(self,id):
        '''
        To delete investment
        '''

        url = "https://api.loanbase.com/api/investment/"+str(id)
        params = {'id': id}
        headers = {
            'Authorization': 'Bearer ' + self.secret,
            'Accept': 'application/vnd.blc.v1+json',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        resp = requests.delete(url, data=params, headers=headers)
        info = "Deleting ID: {0}"\
            .format(id)
        logging.info(strftime("%Y-%m-%d %H:%M:%S", gmtime())+info)
        print(resp.text)


def brfl(lid):
    r = requests.get("https://api.loanbase.com/api/investments/"+str(lid))
    raw = requests.get("https://api.loanbase.com/api/loan/"+str(lid))
    solist = sorted(r.json()['investments'], key=lambda x: float(x['rate']))
    max_rate = 1.0
    investments = 0.0
    requested = float(raw.json()['loans'][0]['amount'])
    for idx, i in enumerate(solist):
        investments = investments + float(solist[idx]['amount'])
        if investments >= requested:
            max_rate = float(solist[idx-1]['rate'])
            return max_rate

import requests
import logging
from time import gmtime, strftime
# secret = 'uhmm secret? xD'
LOG_FILENAME = 'history.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)



class Investor:

    def __init__(self, secret):
        self.secret = secret

    def list():
        '''
        Listing own investments (may be slow due to no api for that)
        '''
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

    def delete():
        '''
        To delete investment
        '''
        pass


def brfl(lid):
    r = requests.get("https://api.loanbase.com/api/investments/"+str(lid))
    solist = sorted(r.json()['investments'], key=lambda x: float(x['rate']))
    max_rate = 1.0
    investments = 0.0
    requested = 6
    for idx, i in enumerate(solist):
        investments = investments + float(solist[idx]['amount'])
        if investments >= requested:
            max_rate = float(solist[idx-1]['rate'])
            return max_rate


print(brfl(21428))

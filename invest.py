import requests
import logging
from time import gmtime, strftime
#secret = 'uhmm secret? xD'
LOG_FILENAME = 'history.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

class Investor:

    def __init__(self,secret):
        self.secret = secret


    def invest(self,lid,amount,rate):
        '''
        Investing in given loan
        '''
        url = "https://api.loanbase.com/api/investment"
        params = {'loan_id': lid, 'amount': amount, 'rate': rate}
        headers = {
            'Authorization': 'Bearer ' + self.secret,
            'Accept': 'application/vnd.blc.v1+json',
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        resp = requests.post(url, data=params, headers=headers)
        info = " Investing LID: {0}, Amount: {1}, Rate: {2}".format(lid,amount,rate)
        logging.info(strftime("%Y-%m-%d %H:%M:%S", gmtime())+info)
        print(resp.text)



i = Investor("secret")


i.invest(21216,0.01,3)



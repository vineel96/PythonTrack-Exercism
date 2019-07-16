import json
from collections import defaultdict

class RestAPI(object):
    def __init__(self, database=None):
        self.data=defaultdict(int,database)

    def get(self, url, payload=None):
        output={'users':[]}
        if payload:
            parse_payload = json.loads(payload)
            for i in self.data['users']:
                if i['name'] in parse_payload['users']:
                    output['users'].append(i)
            return json.dumps(output)
        else:
            return  json.dumps(self.data)


    def post(self, url, payload=None):
        if url=='/add':
            parse_payload=json.loads(payload)
            user={
                'name':parse_payload['user'],
                'owes':{},
                'owed_by':{},
                'balance':0
            }
            self.data['users'].append(user)
            return json.dumps(user)
        if url=='/iou':
            output={'users':[]}
            parse_payload=json.loads(payload)
            for i in self.data['users']:
                if i['name']==parse_payload['lender']:
                    self.update_amount(i,parse_payload,'lender')
                    output['users'].append(i)
                if i['name']==parse_payload['borrower']:
                    self.update_amount(i, parse_payload, 'borrower')
                    output['users'].append(i)

            return json.dumps(output)

    def update_amount(self,i,parse_payload,type):
        if type=='lender':
            if parse_payload['borrower'] in i['owes'].keys():
                if i['owes'][parse_payload['borrower']]>parse_payload['amount']:
                    i['owes'][parse_payload['borrower']] -= parse_payload['amount']
                else:
                    print('bye')
                    if parse_payload['amount']-i['owes'][parse_payload['borrower']]:
                        i['owed_by'][parse_payload['borrower']] =parse_payload['amount']-i['owes'][parse_payload['borrower']]
                    i['owes'].pop(parse_payload['borrower'])
            else:
                i['owed_by'][parse_payload['borrower']] = parse_payload['amount']

        if type=='borrower':
            if parse_payload['lender'] in i['owed_by'].keys():
                if i['owed_by'][parse_payload['lender']]>parse_payload['amount']:
                    i['owed_by'][parse_payload['lender']] -= parse_payload['amount']
                else:
                    print('haii')
                    if parse_payload['amount']-i['owed_by'][parse_payload['lender']]:
                        i['owes'][parse_payload['lender']]=parse_payload['amount']-i['owed_by'][parse_payload['lender']]
                    i['owed_by'].pop(parse_payload['lender'])
            else:
                i['owes'][parse_payload['lender']] = parse_payload['amount']
        i['balance'] = sum([values for values in i['owed_by'].values()]) - sum([values for values in i['owes'].values()])





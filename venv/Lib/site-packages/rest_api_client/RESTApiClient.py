# *** IMPORTS *** #
import requests


# *** CLASS *** #
class RESTApiClient(object):

    # *** INIT *** #
    def __init__(self,
                 url,
                 params):

        self.url = url
        self.params = params

    # *** API *** #
    def get(self,
            verify):

        return requests.get(url=self.url,
                            params=self.params,
                            verify=verify)

    def post(self,
             verify,
             headers,
             data):

        return requests.get(url=self.url,
                            params=self.params,
                            verify=verify,
                            headers=headers,
                            data=data)

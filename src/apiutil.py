__author__ = 'Rich Pearce'

import urllib
import urllib.request
import urllib.error
import json
import logging
import config
import loggerutil

# example from the documentation: https://erikberg.com/account/token
class apiutil():

    #setup logger
    logger = logging.getLogger('NBA API logger')

    #header setup
    headers = {'Authorization': "Bearer " + config.accessToken, 'User-agent': config.user_agent}

    def callAPI(self, url):
        responseDict = {'data': 'test', 'debug': 'true'}

        try:
            # add headers and req
            req = urllib.request.Request(url, headers = self.headers)
            response = urllib.request.urlopen(req)
            jsonResponse = response.read()
            response = jsonResponse.decode('utf-8')
        except urllib.error.URLError as e:
            self.logger.info (e.reason)
            self.logger.info ('Oops no service available at ' + str(url))
            exit()
        except urllib.error.HTTPError:
            self.logger.info ('Oops not a valid operation from the service ' + str(url))
            exit()

        responseDict = json.loads(response)

        self.logger.info ("Call Request : " + str(url))
        print("Call Request : " + str(url))
        self.logger.info ("Call Response: " + str(responseDict))

        return responseDict
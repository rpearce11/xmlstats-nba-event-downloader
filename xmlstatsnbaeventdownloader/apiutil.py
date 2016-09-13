import urllib
import urllib.request
import urllib.error
import json
import logging
import io
import gzip

__author__ = 'Rich Pearce'


# example from the documentation: https://erikberg.com/account/token
class ApiUtil:

    logger = None
    headers = None

    def __init__(self, access_token, user_agent):
        # setup logger
        self.logger = logging.getLogger('NBA API logger')

        # header setup
        self.headers = {'Authorization': "Bearer " + access_token,
                        'User-agent': user_agent,
                        'Accept-encoding': 'gzip'}

    def request(self, url):

        response_dict = {'data': 'test', 'debug': 'true'}

        try:
            # add headers and req
            req = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(req)
            if response.info().get('Content-encoding') == 'gzip':
                buf = io.BytesIO(response.read())
                f = gzip.GzipFile(fileobj=buf)
                json_response = f.read()
            else:
                json_response = response.read()
            response = json_response.decode('utf-8')
        except urllib.error.HTTPError as e:
            self.logger.info(e.reason)
            self.logger.info('Oops not a valid operation from the service ' +
                             str(url))
            exit()
        except urllib.error.URLError as e:
            self.logger.info(e.reason)
            self.logger.info('Oops no service available at ' + str(url))
            exit()

        response_dict = json.loads(response)

        self.logger.info("Call Request : " + str(url))
        print("Call Request : " + str(url))
        self.logger.info("Call Response: " + str(response_dict))

        return response_dict

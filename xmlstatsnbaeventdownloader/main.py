import datetime
import argparse
from xmlstatsnbaeventdownloader import endpoints, downloadbydaterange, \
                                    apiutil, loggerutil

__author__ = 'Rich Pearce'


def main():

    parser = argparse.ArgumentParser(description="Get access_token and "
                                                 "user_agent")

    parser.add_argument('access-token',
                        help='The access token available here: '
                             'https://erikberg.com/account/token')
    parser.add_argument('user-agent',
                        help='The user agent as defined here: '
                             'https://erikberg.com/api#ua')

    args = parser.parse_args()

    access_token = getattr(args, 'access-token')
    user_agent = getattr(args, 'user-agent')

    print(access_token)
    print(user_agent)

    # force logger setup
    loggerutil.LoggerUtil()

    # check my details and log them
    api_util = apiutil.ApiUtil(access_token, user_agent)
    api_util.request(endpoints.me)

    '''
    NBA 2014 - 2015 Season
    October 28, 2014 – April 15, 2015
    April 18, 2015 – May 27, 2015 (Playoffs)
    June 4, 2015 – June 16, 2015 (Finals)
    '''

    from_date = datetime.date(2014, 10, 28)
    to_date = datetime.date(2014, 10, 29)

    # download a date range of NBA game
    download_controller = downloadbydaterange.DownloadByDateRange(api_util)
    download_controller.get_nba_data(from_date, to_date)

if __name__ == "__main__":
    main()

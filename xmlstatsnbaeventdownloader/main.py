import datetime
from xmlstatsnbaeventdownloader import endpoints, downloadbydaterange, \
                                    apiutil, loggerutil

__author__ = 'Rich Pearce'

if __name__ == "__main__":

    # force logger setup
    logger = loggerutil.LoggerUtil()
    # check my details and log them
    apiutil = apiutil.ApiUtil()
    apiutil.request(endpoints.me)

    '''
    NBA 2014 - 2015 Season
    October 28, 2014 – April 15, 2015
    April 18, 2015 – May 27, 2015 (Playoffs)
    June 4, 2015 – June 16, 2015 (Finals)
    '''

    fromDate = datetime.date(2014, 10, 28)
    toDate = datetime.date(2014, 10, 29)

    # download a date range of NBA game
    downloadController = downloadbydaterange.DownloadByDateRange()
    downloadController.get_nba_data(fromDate, toDate)

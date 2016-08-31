__author__ = 'Rich Pearce'

import datetime
import apiutil
import endpoints
import downloadbydaterange

if __name__ == "__main__":
    # check my details and log them
    apiUtil = apiutil.apiutil()
    apiUtil.callAPI(endpoints.me)

    '''
    NBA 2014 - 2015 Season
    October 28, 2014 – April 15, 2015
    April 18, 2015 – May 27, 2015 (Playoffs)
    June 4, 2015 – June 16, 2015 (Finals)
    '''

    fromDate = datetime.date(2014,10,28)
    toDate   = datetime.date(2014,10,29)

    # download a date range of NBA game
    downloadController = downloadbydaterange.downloadbydaterange()
    downloadController.getNBAData( fromDate, toDate )
__author__ = 'Rich Pearce'

import writeformattedcsv
import datetime
import time
import endpoints
import apiutil
import logging
import loggerutil

class downloadbydaterange():

    #setup logger
    logger = logging.getLogger('NBA API logger')
    csvWriter = None
    apiUtil = None

    def __init__(self):
        self.csvWriter = writeformattedcsv.writeformattedcsv( '../data/data.csv')
        self.apiUtil = apiutil.apiutil()

    def getNBAData( self, fromDate, toDate ):

        self.csvWriter.writeHeader()

        startDate = fromDate
        endDate   = toDate
        dayCount = ( endDate - startDate).days + 1

        # estimate time to complete based on the 15 sec pause below, thats 4 per second
        print( "Will take approx.: " + str(dayCount / 4) + " mins" )

        for singleDate in [d for d in ( startDate +  datetime.timedelta(n) for n in range( dayCount )) if d <= endDate]:
            dateString = datetime.datetime.strftime(singleDate,"%Y%m%d")
            url = endpoints.nbaEventReqByDate + str(dateString)
            eventDetails = self.apiUtil.callAPI( url )
            self.csvWriter.writeEventDetails( eventDetails )
            # The api can only be hit 6 times per minute: https://erikberg.com/api I've just been more prudent
            time.sleep(15)

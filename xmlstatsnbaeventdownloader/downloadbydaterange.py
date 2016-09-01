from xmlstatsnbaeventdownloader import writeformattedcsv, endpoints, apiutil
import datetime
import time
import logging
import os

__author__ = 'Rich Pearce'


class DownloadByDateRange():

    # setup logger
    logger = logging.getLogger('NBA API logger')
    csvWriter = None
    apiUtil = None

    def __init__(self):
        if not os.path.exists('../data/'):
            os.makedirs('../data/')
        self.csvWriter = \
            writeformattedcsv.WriteFormattedCsv('../data/data.csv')
        self.apiUtil = apiutil.ApiUtil()

    def get_nba_data(self, from_data, to_date):

        self.csvWriter.write_header()

        start_date = from_data
        end_date = to_date
        day_count = (end_date - start_date).days + 1

        # estimate time to complete based on the 15 sec pause below
        # thats 4 per second
        print("Will take approx.: " + str(day_count / 4) + " mins")

        for singleDate in \
                [d for d in (start_date + datetime.timedelta(n)
                             for n in range(day_count)) if d <= end_date]:
            date_string = datetime.datetime.strftime(singleDate, "%Y%m%d")
            url = endpoints.nbaEventReqByDate + str(date_string)
            event_details = self.apiUtil.request(url)
            self.csvWriter.write_event_details(event_details)
            # The api can only be hit 6 times per minute, see:
            # https://erikberg.com/api I've just been more prudent
            time.sleep(15)

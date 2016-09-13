import writeformattedcsv
import endpoints
import datetime
import time
import logging
import os

__author__ = 'Rich Pearce'


class DownloadByDateRange():

    # setup logger
    logger = logging.getLogger('NBA API logger')
    csv_writer = None
    api_util = None

    def __init__(self, api_util):
        if not os.path.exists('../data/'):
            os.makedirs('../data/')
        self.csv_writer = \
            writeformattedcsv.WriteFormattedCsv('../data/data.csv')
        self.api_util = api_util

    def get_nba_data(self, from_data, to_date):

        self.csv_writer.write_header()

        start_date = from_data
        end_date = to_date
        day_count = (end_date - start_date).days + 1

        # estimate time to complete based on the 15 sec pause below
        # that's 4 per second
        print("Will take approx.: " + str(day_count / 4) + " mins")

        for singleDate in \
                [d for d in (start_date + datetime.timedelta(n)
                             for n in range(day_count)) if d <= end_date]:
            date_string = datetime.datetime.strftime(singleDate, "%Y%m%d")
            url = endpoints.nbaEventReqByDate + str(date_string)
            event_details = self.api_util.request(url)
            self.csv_writer.write_event_details(event_details)
            # The api can only be hit 6 times per minute, see:
            # https://erikberg.com/api I've just been more prudent
            time.sleep(15)

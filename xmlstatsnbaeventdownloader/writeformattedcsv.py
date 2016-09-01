import datetime
import codecs
import logging

__author__ = 'Rich Pearce'


class WriteFormattedCsv():

    file_name = 'errorNoFileName'
    # setup logger
    logger = logging.getLogger('NBA API logger')

    def __init__(self, name):
        self.logger.info(name)
        self.file_name = name

    def write_header(self):
        data_file = codecs.open(self.file_name, 'a', "utf-8")
        data_file.write("date,home,away,homescore,awayscore,homeq1,homeq2," +
                        "homeq3,homeq4,awayq1,awayq2,awayq3,awayq4," +
                        "pointspreadhome,pointspreadaway,seasonType\n")
        data_file.close()

    def write_event_details(self, event_details):
        # write to file appending
        data_file = codecs.open(self.file_name, 'a', "utf-8")

        self.logger.info(event_details)

        date = event_details['events_date']
        the_date_time = datetime.datetime.strptime(date[:10], "%Y-%m-%d")
        the_date = datetime.datetime.strftime(the_date_time, "%Y%m%d")

        # Loop through each Event (https://erikberg.com/api/objects/event)
        for evt in event_details['event']:
            # Get team objects (https://erikberg.com/api/objects/team)

            self.logger.info(evt)

            # break the data down into the home team and
            # away team for ease of handling
            away_team = evt['away_team']
            home_team = evt['home_team']

            home_team_abbr = evt['home_team']['abbreviation']
            away_team_abbr = evt['away_team']['abbreviation']

            season_type = evt['season_type']
            event_status = evt['event_status']

            self.logger.info(away_team['full_name'] + " abb:" +
                             away_team_abbr + " @ " +
                             home_team['full_name'] + " abb:" +
                             home_team_abbr + " " + event_status)

            if(event_status == "completed"):

                home_points_scored = evt['home_points_scored']
                away_points_scored = evt['away_points_scored']
                home_period_scored = evt['home_period_scores']
                away_period_scored = evt['away_period_scores']

                concat_event_details = the_date \
                    + "," + home_team_abbr \
                    + "," + away_team_abbr \
                    + "," + str(home_points_scored) \
                    + "," + str(away_points_scored) \
                    + "," + str(home_period_scored[0]) \
                    + "," + str(home_period_scored[0] +
                                home_period_scored[1]) \
                    + "," + str(home_period_scored[0] + home_period_scored[1] +
                                home_period_scored[2])\
                    + "," + str(home_period_scored[0] + home_period_scored[1] +
                                home_period_scored[2] +
                                home_period_scored[3]) \
                    + "," + str(away_period_scored[0]) \
                    + "," + str(away_period_scored[0] +
                                away_period_scored[1]) \
                    + "," + str(away_period_scored[0] + away_period_scored[1] +
                                away_period_scored[2]) \
                    + "," + str(away_period_scored[0] + away_period_scored[1] +
                                away_period_scored[2]+away_period_scored[3]) \
                    + "," + str(home_points_scored - away_points_scored) \
                    + "," + str(away_points_scored - home_points_scored) \
                    + "," + season_type

                self.logger.info(concat_event_details)
                data_file.write(concat_event_details + "\n")
            # else log the status
            else:
                data_file.write(the_date + "," +
                                home_team_abbr + "," +
                                away_team_abbr + "," +
                                evt['event_status'] + "," +
                                season_type + "\n")

        data_file.close()

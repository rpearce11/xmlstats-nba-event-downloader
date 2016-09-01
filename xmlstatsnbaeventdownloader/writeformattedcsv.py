import datetime
import codecs
import logging

__author__ = 'Rich Pearce'


class writeformattedcsv():

    fileName = 'errorNoFileName'
    # setup logger
    logger = logging.getLogger('NBA API logger')

    def __init__(self, name):
        self.logger.info(name)
        self.fileName = name

    def writeHeader(self):
        dataFile = codecs.open(self.fileName, 'a', "utf-8")
        dataFile.write("date,home,away,homescore,awayscore,homeq1,homeq2,"
                       "homeq3,homeq4,awayq1,awayq2,awayq3,awayq4,"
                       "pointspreadhome,pointspreadaway,seasonType\n")
        dataFile.close()

    def writeEventDetails(self, eventDetails):
        # write to file appending
        dataFile = codecs.open(self.fileName, 'a', "utf-8")

        self.logger.info(eventDetails)

        date = eventDetails['events_date']
        theDateTime = datetime.datetime.strptime(date[:10], "%Y-%m-%d")
        theDate = datetime.datetime.strftime(theDateTime, "%Y%m%d")

        # Loop through each Event (https://erikberg.com/api/objects/event)
        for evt in eventDetails['event']:
            # Get team objects (https://erikberg.com/api/objects/team)

            self.logger.info(evt)

            # break the data down into the home team and
            # away team for ease of handling
            away_team = evt['away_team']
            home_team = evt['home_team']

            homeTeamAbbr = evt['home_team']['abbreviation']
            awayTeamAbbr = evt['away_team']['abbreviation']

            seasonType = evt['season_type']
            eventStatus = evt['event_status']

            self.logger.info(away_team['full_name'] + " abb:" + awayTeamAbbr +
                             " @ " + home_team['full_name'] + " abb:" +
                             homeTeamAbbr + " " + eventStatus)

            if(eventStatus == "completed"):

                homePointsScored = evt['home_points_scored']
                awayPointsScored = evt['away_points_scored']
                homePeriodScored = evt['home_period_scores']
                awayPeriodScored = evt['away_period_scores']

                concatEventDetails = theDate \
                    + "," + homeTeamAbbr \
                    + "," + awayTeamAbbr \
                    + "," + str(homePointsScored) \
                    + "," + str(awayPointsScored) \
                    + "," + str(homePeriodScored[0]) \
                    + "," + str(homePeriodScored[0] + homePeriodScored[1]) \
                    + "," + str(homePeriodScored[0] + homePeriodScored[1] +
                                homePeriodScored[2])\
                    + "," + str(homePeriodScored[0] + homePeriodScored[1] +
                                homePeriodScored[2] + homePeriodScored[3]) \
                    + "," + str(awayPeriodScored[0]) \
                    + "," + str(awayPeriodScored[0] + awayPeriodScored[1]) \
                    + "," + str(awayPeriodScored[0] + awayPeriodScored[1] +
                                awayPeriodScored[2]) \
                    + "," + str(awayPeriodScored[0] + awayPeriodScored[1] +
                                awayPeriodScored[2]+awayPeriodScored[3]) \
                    + "," + str(homePointsScored - awayPointsScored) \
                    + "," + str(awayPointsScored - homePointsScored) \
                    + "," + seasonType

                self.logger.info(concatEventDetails)
                dataFile.write(concatEventDetails + "\n")
            # else log the status
            else:
                dataFile.write(theDate + "," + homeTeamAbbr + "," +
                               awayTeamAbbr + "," + evt['event_status'] +
                               "," + seasonType + "\n")

        dataFile.close()

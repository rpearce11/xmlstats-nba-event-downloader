from unittest import TestCase
from xmlstatsnbaeventdownloader import writeformattedcsv as csv
import codecs
from tests import mockdata
from os import remove

__author__ = 'Rich Pearce'


class TestWriteformattedcsv(TestCase):

    formattedcsvwritter = None
    fileName = 'testCSV.csv'

    def test_writeHeader(self):

        # Setup the file in the test case, so tests are isolated, as the
        # writeformattedcsv functionality is appending writes
        self.formattedcsvwritter = csv.writeformattedcsv(self.fileName)

        self.formattedcsvwritter.writeHeader()

        header = "date,home,away,homescore,awayscore,homeq1,homeq2,homeq3," \
                 "homeq4,awayq1,awayq2,awayq3,awayq4,pointspreadhome," \
                 "pointspreadaway,seasonType\n"

        dataFile = codecs.open(self.fileName, 'r', "utf-8")
        string = dataFile.readline()

        self.assertEqual(header, string)

        # remove the file
        remove(self.fileName)

    def eventDetailsWriter(self, eventDetails, listOfTestStrings):
        # Setup the file in the test case, so tests are isolated, as the
        # writeformattedcsv functionality is appending writes
        self.formattedcsvwritter = csv.writeformattedcsv(self.fileName)

        self.formattedcsvwritter.writeEventDetails(eventDetails)

        dataFile = codecs.open(self.fileName, 'r', "utf-8")
        testDataIndex = 0
        for line in dataFile.readlines():
            self.assertEqual(line, listOfTestStrings[testDataIndex])
            testDataIndex = testDataIndex + 1

        # remove the file
        remove(self.fileName)

    def test_writeSingleEventDetails(self):

        eventStrings = list()
        eventStrings.append("20130131,OKC,MEM,106,89,32,58,79,106,22,34,67,89,"
                            "17,-17,regular\n")

        self.eventDetailsWriter(mockdata.mockSingleEventData, eventStrings)

    def test_writeMultipleEventDetails(self):

        eventStrings = list()
        eventStrings.append("20130131,OKC,MEM,106,89,32,58,79,106,22,34,67,89,"
                            "17,-17,regular\n")
        eventStrings.append("20130131,GS,DAL,100,97,28,55,80,100,23,53,79,97,"
                            "3,-3,regular\n")

        self.eventDetailsWriter(mockdata.mockTwoEventsData, eventStrings)

    def test_writeSingleEventFutureDetails(self):

        eventStrings = list()
        eventStrings.append("20150614,GS,CLE,scheduled,post\n")

        self.eventDetailsWriter(mockdata.mockSingleFutureEventData,
                                eventStrings)

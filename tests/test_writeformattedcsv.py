from unittest import TestCase
from xmlstatsnbaeventdownloader import writeformattedcsv as csv
import codecs
from tests import mockdata
from os import remove

__author__ = 'Rich Pearce'


class TestWriteformattedcsv(TestCase):

    formatted_csv_writter = None
    file_name = 'testCSV.csv'

    def test_write_header(self):

        # Setup the file in the test case, so tests are isolated, as the
        # WriteFormattedCsv functionality is appending writes
        self.formatted_csv_writter = csv.WriteFormattedCsv(self.file_name)

        self.formatted_csv_writter.write_header()

        header = "date,home,away,homescore,awayscore,homeq1,homeq2,homeq3," \
                 "homeq4,awayq1,awayq2,awayq3,awayq4,pointspreadhome," \
                 "pointspreadaway,seasonType\n"

        data_file = codecs.open(self.file_name, 'r', "utf-8")
        string = data_file.readline()

        self.assertEqual(header, string)

        # remove the file
        remove(self.file_name)

    def event_details_writer(self, event_details, list_of_test_strings):
        # Setup the file in the test case, so tests are isolated, as the
        # WriteFormattedCsv functionality is appending writes
        self.formatted_csv_writter = csv.WriteFormattedCsv(self.file_name)

        self.formatted_csv_writter.write_event_details(event_details)

        data_file = codecs.open(self.file_name, 'r', "utf-8")
        test_data_index = 0
        for line in data_file.readlines():
            self.assertEqual(line, list_of_test_strings[test_data_index])
            test_data_index = test_data_index + 1

        # remove the file
        remove(self.file_name)

    def test_write_single_event_details(self):

        event_strings = list()
        event_strings.append("20130131,OKC,MEM,106,89,32,58,79,106,22,34,67,"
                             "89,17,-17,regular\n")

        self.event_details_writer(mockdata.mock_single_event_data,
                                  event_strings)

    def test_write_multiple_event_details(self):

        event_strings = list()
        event_strings.append("20130131,OKC,MEM,106,89,32,58,79,106,22,34,67,"
                             "89,17,-17,regular\n")
        event_strings.append("20130131,GS,DAL,100,97,28,55,80,100,23,53,79,"
                             "97,3,-3,regular\n")

        self.event_details_writer(mockdata.mock_two_events_data, event_strings)

    def test_write_single_event_future_details(self):

        event_strings = list()
        event_strings.append("20150614,GS,CLE,scheduled,post\n")

        self.event_details_writer(mockdata.mock_single_future_event_data,
                                  event_strings)

"""
.. module:: main
   :synopsis: Main
.. moduleauthor:: MA Raza

This is the mian file to run the app.

Example

    >>> python file_processor/main.py --file_name test_data/sample1.txt  --start_datetime 2000-01-01T17:25:49Z  --end_datetime 2000-01-06T06:27:36Z

Todo:
    * Add configuration file to control the parameters --Done
    * Covert the code into API version
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from loguru import logger
from file_processor.utils.helpers import  filter_json_date
data_path = '../test_data/'
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', type=str, help='The name of the file to process', required=True)
    parser.add_argument('--start_datetime', type=str, help='UTC Start Date Time', required=True)
    parser.add_argument('--end_datetime', type=str, help='UTC Start Date Tim', required=True)
    args = parser.parse_args()
    logger.info('Starting the Application')

    file_name = args.file_name
    start_datetime = args.start_datetime
    end_datetime = args.end_datetime
    logger.info(f'Parameters: File name : {file_name}, Start Date Time : {start_datetime}, End Date Time: {end_datetime}')

    response = filter_json_date(file_name, start_datetime, end_datetime)
    print(response)

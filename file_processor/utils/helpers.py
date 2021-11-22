"""
.. module:: helpers
   :synopsis: helpers
.. moduleauthor:: MA Raza

This module contains helpers functions

Todo:
    * Add more helper functions
"""

import sys
sys.path.append('.')
import pandas as pd
from loguru import logger
import re

regex = r'^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9]Z)?$'
match_iso8601 = re.compile(regex).match


def validate_iso8601_utc(str_val):
    """
    To check the valid ISO UTC format
    Args:
        str_val: UTC String format

    Returns: Bool

    """
    try:
        if match_iso8601( str_val ) is not None:
            return True
    except:
        pass
    return False


def filter_json_date(file_path, start_datetime, end_datetime):
    """
    This function reads the text file and filters based on given datetime ranges.
    After the filtering, df is deleted to free up the memory space.
    Args:
        file_path: Location of uploaded text file
        start_datetime: Start Datetime range in UTC format
        end_datetime: End Datetime range in UTC format

    Returns: Json Object

    """
    if validate_iso8601_utc(start_datetime) & validate_iso8601_utc(end_datetime):
        logger.info('Date Time formats are correct')
        logger.info('Loading the file')
        # df = pd.read_csv(StringIO(str(file_path.read(), 'utf-16')), encoding='utf-16')
        # logger.info(df.head())
        df = pd.read_csv(file_path, sep=" ", header=None)
        # logger.info(df.head())
        df.columns = ['eventTime', 'email', 'sessionId']
        logger.info('filtering the data')
        result = df[df['eventTime'].between(start_datetime, end_datetime)].to_json(orient='records', lines=False)
        # Delete the df to free up memory
        del df
        logger.info('The pandas df has been deleted to free up memory')
        return result
    else:
        logger.info('Input Date Time format is incorrect')
        return [{'message':'Input Date Time format is incorrect'}]

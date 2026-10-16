"""
time_conversion.py

This module contains functions that convert a number of seconds
into various non-conventional time units.

Each function accepts an integer number of seconds
and returns the converted value.
"""

def decaseconds_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to decaseconds.
        1 decasecond = 10 seconds.

    Output:
        Return the equivalent number of decaseconds.
    """
    return seconds/10
    # This will convert the number of seconds into the equivalent number of  decaseconds



def jiffies_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to jiffies.
        1 jiffy = 10 milliseconds.

    Output:
        Return the equivalent number of jiffies.
    """
    return seconds/0.01
    # This will convert the number of seconds into the equivalent number of jiffies


def new_york_minutes_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to New York Minutes.
        1 New York Minute = 1/20 of a second

    Output:
        Return the equivalent number of New York Minutes.
    """
    return  seconds * 20
    # This will convert the number of seconds into the equivalent number of New York Minutes


def nanocenturies_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to Nanocenturies.
         1 Nanocentury = 3.156 seconds

    Output:
        Return the equivalent number of Nanocenturies.
    """

    return seconds/3.156
    # This will convert the number of seconds into the equivalent number of nanocenturies


def snapchat_streak_days_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to Snapchat Streak Days.
        1 Snapchat Streak Day = 24 hours

    Output:
        Return the equivalent number of Snapchat Streak Days.
    """
    return seconds/86400
    # This will convert the number of seconds into the equivalent number of snapchat streak days

def custom_time_conversion(seconds: float) -> float:
    """
Input:
    seconds (int): A number of seconds.

Process:
    Convert the number of seconds to minutes.
    1 minute = 60 seconds.

Output:
    Return the equivalent number of minutes.
"""
    return seconds/60
# This will convert the  number of seconds into the equivalent number of minutes

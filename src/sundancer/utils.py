from datetime import datetime

from sundancer.conf.settings import DPN_DATE_FORMAT

def dpn_strftime(dt):
    """
    Returns a string formatted datetime as per the DPN message format and
    localized as per the configured value in settings.TIME_ZONE.
    :param dt: Datetime object to convert to a string.
    :return:  String of datetime with local timezone.
    """
    return dt.strftime(DPN_DATE_FORMAT)


def dpn_strptime(dt_string):
    """
    Parses a datetime object from a DPN formatted Datetime string as configured
    in localsettings.
    :param dt_string:  String in DPN datetime format to parse as a datetime object.
    :return:  Datetime object
    """
    return datetime.strptime(dt_string, DPN_DATE_FORMAT)
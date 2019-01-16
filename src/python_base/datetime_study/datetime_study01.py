# -*- coding=utf-8 -*-

import datetime

DATETIME_FORMAT = "%Y%m%d_%H%M%S"
DATETIME_YMD_FORMAT = "%Y-%m-%d"


def get_ymd_hms():
    """
    :return: '20181122_195951'
    """
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


def get_ymd_hms2():
    """
    :return: '2018-11-22_19:59:51'
    """
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def get_days(date_now, date2):
    date2 = datetime.datetime.strptime(date2, DATETIME_FORMAT)
    return (date_now - date2).days


if __name__ == '__main__':
    time1 = "20180910_224201"
    print time1[:15]
    date_now=datetime.datetime.now()
    t = get_days(date_now,"20180910_224201")
    print t




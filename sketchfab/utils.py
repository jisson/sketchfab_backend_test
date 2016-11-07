import datetime

__author__ = 'Pierre Rodier | pierre@buffactory.com'


def is_date_timeout(date, timeout):
    """
    Compare the given date to: date_now - timeout.
    If the given date is inferior, True will be returned.

    :param date:    The date to verify
    :type date:     datetime
    :param timeout: The timeout to subtract to date_now. Have to be expressed
                    in seconds
    :type timeout:  int
    :return:
    """

    now = datetime.datetime.now()
    timeout_date = now - datetime.timedelta(seconds=timeout)

    if date < timeout_date:
        return True
    return False



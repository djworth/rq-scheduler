import calendar
import croniter

from datetime import datetime

# from_unix from times.from_unix()
def from_unix(string):
    """Convert a unix timestamp into a utc datetime"""
    return datetime.utcfromtimestamp(float(string))


# to_unix from times.to_unix()
def to_unix(dt):
    """Converts a datetime object to unixtime"""
    return calendar.timegm(dt.utctimetuple())

def crontab_get_next_scheduled_time(crontab_string):
    """Calculate the next scheduled time by creating a crontab object
    with a crontab string"""
    job = croniter.croniter(crontab_string)
    return job.get_next(datetime)

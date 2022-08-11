"""

Date range and Datetime range generators.


Basic usage:

for d in date_range(date(2000, 1, 1), date(2000, 1, 10)):
    ...

for dt in datetime_range(datetime(2000, 1, 1), datetime(2000, 1, 10)):
    ...


Using step:

for d in date_range(date(2000, 1, 1), date(2000, 1, 10), step=timedelta(days=2)):
    ...

for dt in datetime_range(datetime(2000, 1, 1), datetime(2000, 1, 10), step=timedelta(days=2)):
    ...


Reverse iteration:

for d in date_range(date(2000, 1, 10), date(2000, 1, 1), step=timedelta(days=-2)):
    ...

for dt in datetime_range(datetime(2000, 1, 10), datetime(2000, 1, 1), step=timedelta(days=-2)):
    ...

"""

def datetime_range(start_datetime, end_datetime, step = None):
    """ Generator for a datetime range """
    from datetime import datetime, timedelta

    # VALIDATIONS

    assert isinstance(start_datetime, datetime), 'start must be a datetime'
    assert isinstance(end_datetime, datetime), 'end must be a datetime'

    if step is None:
        step = timedelta(seconds=1) # default
    else:
        assert isinstance(step, timedelta), 'step must be a timedelta'

    assert (
        (start_datetime <= end_datetime and step.total_seconds() > 0)
        or
        (start_datetime >= end_datetime and step.total_seconds() < 0)
    ), '(start must be less than end and step must be positive)'\
       'or (start must be greater than end and step must be negative)'

    # PROCESSING

    current_datetime = start_datetime
    while current_datetime <= end_datetime:
        yield current_datetime
        current_datetime += step


def date_range(start_date, end_date, step = None):
    """ Generator for a date range """
    from datetime import date, timedelta

    # VALIDATIONS

    assert isinstance(start_date, date), 'start must be a date'
    assert isinstance(end_date, date), 'end must be a date'

    if step is None:
        step = timedelta(days=1) # default
    else:
        assert isinstance(step, timedelta), 'step must be a timedelta'

    is_step_positive = step.days > 0

    assert (
        (start_date <= end_date and is_step_positive)
        or
        (start_date >= end_date and not is_step_positive)
    ), '(start must be less than end and step must be positive)'\
       'or (start must be greater than end and step must be negative)'

    # PROCESSING

    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += step

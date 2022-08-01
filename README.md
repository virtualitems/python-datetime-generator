# Python Datetime Generator

## Description
Generator function to iterate between dates.

## Usage

Example with dates:
```
for d in date_range(date(2020, 1, 1), date(2020, 1, 31), timedelta(days=1)):
    print(d)
```

Example with datetimes:
```
for dt in datetime_range(datetime(2020, 1, 1, 1), datetime(2020, 1, 1, 10), timedelta(hours=1)):
    print(dt)
```

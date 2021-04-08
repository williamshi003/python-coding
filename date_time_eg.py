from datetime import date, datetime, time, timedelta

# 实例化时间对象
date_obj = date(2021, 4, 7)
datetime_obj = datetime(2021, 4, 7, 10, 50, 10)
time_obj = time(4, 7)
print(time_obj)

# 时间对象转字符串
date_string = datetime.strftime(date_obj, "%Y-%m-%d")
print(date_string)

datetime_string = datetime.strftime(datetime_obj, "%Y-%m-%d %H:%M:%s")
print(datetime_string)

# 时间字符串转时间对象
datetime_object = datetime.strptime(date_string, "%Y-%m-%d")
print(datetime_object)

# 时间运算
datetime_delta = datetime_object + timedelta(days=1, hours=2, minutes=10)
print(datetime_delta)

# 时间组合：日期 + 时间
print(datetime.combine(date(2021, 4, 7), time(4, 7)))

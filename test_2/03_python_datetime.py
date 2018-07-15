from datetime import date, time, datetime, timedelta

# 对日期进行处理的练习 --获取年月日
today = datetime.today()
print(today)
today_1 = date.today()
print(today_1)
print('year: {0!s}年'.format(today.year))
print('month: {0!s}月'.format(today.month))
print('day: {0!s}日'.format(today.day))

# 对日期进行加减处理
one_day = timedelta(days=-1)
tomorrow = today + one_day
print('tomorrow:{0!s}'.format(tomorrow))
eight_hour = timedelta(hours=25)
next_time = today + eight_hour
print('next time:{0!s}'.format(next_time))
print('eight_hour:{0!s} {1!s}'.format(eight_hour.days, eight_hour.seconds))

date_diff = next_time - today
print('date_diff: {0!s}'.format(date_diff))
print('date_diff: {0!s}'.format(str(date_diff).split()[0]))

# 自定义日期格式 & 文本格式的日期转为日期
today_format = today.strftime('%b %d,%Y')
print('#自定义日期显示：{}'.format(today_format))
print('#文本转日期包含时分秒: {}'.format(datetime.strptime(today_format, '%b %d,%Y')))
print('#文本转日期不含时分秒: {}'.format(datetime.date(datetime.strptime(today_format, '%b %d,%Y'))))

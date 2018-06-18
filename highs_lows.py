#！/usr/bin/env.python
# _*_ coding:utf-8 _*_


import csv
from datetime import datetime as dt
import matplotlib.pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 读取文件中第一行：标题行

    dates, highs, lows = [], [], []
    # 从文件的第二行开始循环
    for row in reader:
        try:
            date = dt.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print(date, 'missing data')

        else:
            dates.append(date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='blue', alpha=0.5)
    plt.plot(dates, lows, c='r', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='r', alpha=0.1)

    # 设置图像格式
    plt.title('daily max and min temperature in July 2014', fontsize=10)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()   # 绘制日期标签以免重叠
    plt.ylabel('Temperature F', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

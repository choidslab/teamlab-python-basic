import datetime
import os
import random

if not os.path.isdir('log'):
    os.mkdir('log')

if not os.path.exists('log/count_log2.txt'):
    with open('log/count_log2.txt', 'w', encoding='utf-8') as f:
        f.write('기록이 시작됩니다.\n')

with open('log/count_log2.txt', 'a', encoding='utf-8') as f:
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + '\t' + str(value) + '값이 생성되었습니다.' + '\n'
        f.write(log_line)

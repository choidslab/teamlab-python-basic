
with open('count_log.txt', 'w', encoding='utf-8') as f:

    for i in range(1, 100):
        f.write("최두섭 {0}번째 줄입니다.\n".format(i))

with open('count_log.txt', 'a', encoding='utf-8') as f:

    for i in range(100, 201):
        f.write("최두섭 {0}번째 줄을 추가했습니다.\n".format(i))

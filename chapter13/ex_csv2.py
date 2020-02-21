import csv

seongnam_data = []
header = []
rownum = 0

with open('korea_floating_population_data.csv', 'r', encoding='cp949') as csv_file:
    csv_data = csv.reader(csv_file)
    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[7]

        if location.find(u"성남시") != -1:
            seongnam_data.append(row)
        rownum += 1

with open('seongnam_floating_population_data.csv', 'w', encoding='utf-8') as sn_csv_file:
    # writer = csv.writer(sn_csv_file, delimiter=',', quotechar="!", quoting=csv.QUOTE_ALL)
    writer = csv.writer(sn_csv_file, delimiter=',')
    writer.writerow(header)
    for row in seongnam_data:
        writer.writerow(row)

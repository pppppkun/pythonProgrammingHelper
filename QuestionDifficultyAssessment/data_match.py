import csv

file1 = csv.reader(open('csv_test_by_Qin.csv', 'r'))
rows = [row for row in file1]
file2 = csv.reader(open('csv_test_by_pkun.csv', 'r'))
final = open('final.csv', 'w', newline="")
content = csv.writer(final)
for k in file1:
    print(k)
x = 0
number = 0
case_id = '2061'
avgs = []
for i in range(1, len(rows)):
    if case_id != rows[i][1][0:4]:
        average = x/number
        avgs.append([case_id, average])
        x = 0
        number = 0
        case_id = rows[i][1][0:4]
    x = x + float(rows[i][3])
    number += 1
File2 = list(file2)
header = File2[0]
header.append("average_complexity")
content.writerow(header)
for k in range(1, len(File2)):
    new_row = File2[k]
    for m in avgs:
        if m[0] == new_row[0]:
            new_row.append(m[1])
            content.writerow(new_row)
            break
    #content.writerow(new_row)
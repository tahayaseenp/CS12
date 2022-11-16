import csv


def copy():
    f = open('csv1.csv', 'r')
    if not f:
        print("File not found!")
        exit()
    r = csv.reader(f)
    f1 = open('csv2.csv', 'w', newline='')
    w = csv.writer(f1)
    for row in r:
        w.writerow(row)
    f.close()
    f1.close()


copy()
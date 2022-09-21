import csv
f = open("test.csv", "w+")
w = csv.writer(f)
w.writerow(['id', 'name', 'email'])
w.writerow([100, 'Ronald', 'ronald@comp.com'])
f.close()
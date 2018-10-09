from math import exp, sqrt, pi
import csv
import operator

mean = []
var = []

#membaca file mean dan variance
with open('meanvar.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        res = []
        vres =[]
        #digunakan untuk membagi mean dan variance
        if (line_count%2)==0:
            for x in range(0,4):
                res.append(float(row[x]))
            line_count += 1
            mean.append(res)
        else:
            for x in range(0,4):
                vres.append(float(row[x]))
            line_count += 1
            var.append(vres)

# menghitung likelihood dengan variabel data, mean, dan variance
def p(x, mean, var):
    like = 1/sqrt(2*pi*var)*exp((-(x - mean)*(x - mean))/(2*var))
    return like

# membaca file untuk testing
testCsv = []
with open('newtest.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        tres = []
        for x in range(0,4):
            tres.append(float(row[x]))
        line_count += 1
        testCsv.append(tres)


prior = [1/3, 1/3, 1/3]
# melakukan perhitungan posterior dari testing terhadap mean dan variance yang telah ada
for i in range(0,75):
    result = []
    for j in range(0,3):
        likelihood = 1
        for k in range(0,4):
            likelihood *= p(testCsv[i][k], mean[j][k], var[j][k])

        result.append(likelihood )
        key = ['setosa', 'versicolor', 'virginica']
        iris = dict(zip(key,result))
    print(i+1, max(iris.items(), key=operator.itemgetter(1))[0])


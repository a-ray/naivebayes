from math import exp, sqrt, pi
import csv
import operator

mean = []
var = []


with open('meanvar.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        res = []
        vres =[]
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

# print(mean)
# print(var)

# def p(x, mean, var):
def p(x, mean, var):
    like = 1/sqrt(2*pi*var)*exp((-(x - mean)*(x - mean))/(2*var))
    # print(x, " ", like)
    return like

# print(p(5.7, 5.028, 0.16))

# print(p(5.1, 4.984, 0.092233333)  *p(3.5, 3.356, 0.152566667) *p(1.4, 1.468, 0.022266667)  *p(0.2, 0.24, 0.0125))

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

# print(testCsv)


testing = [5.9,3.0,5.1,1.8]

prior = [1/3, 1/3, 1/3]
result = []
# print(prior[2])
for i in range(0,75):
    result = []
    for j in range(0,3):
        likelihood = 1
        # print(likelihood)
        # likelihood = p(testing[0], mean[j][0], var[j][0]) \
        #              * p(testing[1], mean[j][1], var[j][1]) \
        #              * p(testing[2], mean[j][2], var[j][2]) \
        #              * p(testing[3], mean[j][3], var[j][3])

        # print((testing[0], mean[j][0], var[j][0]) \
        #              ,"", (testing[1], mean[j][1], var[j][1]) \
        #              ,"", (testing[2], mean[j][2], var[j][2]) \
        #              ,"", (testing[3], mean[j][3], var[j][3]))
        # print(p(testing[0], mean[j][0], var[j][0]) \
        #              ,"", p(testing[1], mean[j][1], var[j][1]) \
        #              ,"", p(testing[2], mean[j][2], var[j][2]) \
        #              ,"", p(testing[3], mean[j][3], var[j][3]))
        for k in range(0,4):
        # print([j]," likelihood " ,likelihood)
        #     print(testCsv[i][k])
            likelihood *= p(testCsv[i][k], mean[j][k], var[j][k])
            # likelihood *= p(testing[k], mean[j][k], var[j][k])

        result.append(likelihood )
        # print("posterior ", result)
        key = ['setosa', 'versicolor', 'virginica']
        iris = dict(zip(key,result))
    # print(likelihood)
    print(i+1, max(iris.items(), key=operator.itemgetter(1))[0])


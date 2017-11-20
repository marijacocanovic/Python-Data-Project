import csv
from datetime import datetime, timedelta
# Q1
yearset1, yearset2, yearset3, yearset4, yearset5, yearset6, yearset7, yearset8, yearset9, yearset10, yearset11, yearset12, yearset13, yearset14, yearset15, yearset16, yearset17, yearset18, yearset19, yearset20, yearset21, yearset22, yearset23, yearset24 = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
def highestDiff(list, i):
    with open("weather_data.csv") as myFile:
        lines = myFile.readlines()
    for line in lines[1:]:
        info = line.split(",")
        date = info[0].rstrip()
        actual_mean_temp = info[1].rstrip
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        actual_mean_temp_object = actual_mean_temp()
        year = datetime.strptime(info[0].rstrip(), '%Y-%m-%d').year
        if year==(i + 1992):
            list.append(actual_mean_temp_object)
        if year==(i + 1 + 1992):
            list.append(actual_mean_temp_object)
        if year==(i + 2 + 1992):
            list.append(actual_mean_temp_object)

highestDiff(yearset1, 0)
highestDiff(yearset2, 1)
highestDiff(yearset3, 2)
highestDiff(yearset4, 3)
highestDiff(yearset5, 4)
highestDiff(yearset6, 5)
highestDiff(yearset7, 6)
highestDiff(yearset8, 7)
highestDiff(yearset9, 8)
highestDiff(yearset10, 9)
highestDiff(yearset11, 10)
highestDiff(yearset12, 11)
highestDiff(yearset13, 12)
highestDiff(yearset14, 13)
highestDiff(yearset15, 14)
highestDiff(yearset16, 15)
highestDiff(yearset17, 16)
highestDiff(yearset18, 17)
highestDiff(yearset19, 18)
highestDiff(yearset20, 19)
highestDiff(yearset21, 20)
highestDiff(yearset22, 21)
highestDiff(yearset23, 22)
highestDiff(yearset24, 23)

differeces_list=[]
def difference(yearset, differences_list):
    diff=(int(max(yearset)))-(int(min(yearset)))
    differeces_list.append(diff)

difference(yearset1, differeces_list)
difference(yearset2, differeces_list)
difference(yearset3, differeces_list)
difference(yearset4, differeces_list)
difference(yearset5, differeces_list)
difference(yearset6, differeces_list)
difference(yearset7, differeces_list)
difference(yearset8, differeces_list)
difference(yearset9, differeces_list)
difference(yearset10, differeces_list)
difference(yearset11, differeces_list)
difference(yearset12, differeces_list)
difference(yearset13, differeces_list)
difference(yearset14, differeces_list)
difference(yearset15, differeces_list)
difference(yearset16, differeces_list)
difference(yearset17, differeces_list)
difference(yearset18, differeces_list)
difference(yearset19, differeces_list)
difference(yearset20, differeces_list)
difference(yearset21, differeces_list)
difference(yearset22, differeces_list)
difference(yearset23, differeces_list)
difference(yearset24, differeces_list)

highestChange=int(max(differeces_list))
#print(highestChange)

for i, j in enumerate(differeces_list):
    if j == highestChange:
        print(i)
        i=i+1992
        n=i+2
        print("1. The period with the highest change in actual mean temperature is: " + str(i) + "-" + str(n))

#Q2
jan_list, feb_list, mar_list, apr_list, may_list, jun_list, jul_list, aug_list, sep_list, oct_list, nov_list, dec_list, averages = [], [], [], [], [], [], [], [], [], [], [], [], []
def avgmonth(num_month, list, averages):
    with open("weather_data.csv") as myFile:
        lines = myFile.readlines()
    for line in lines[1:]:
        info = line.split(",")
        date = info[0].rstrip()
        actual_max_temp = info[3].rstrip
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        actual_max_temp_object = actual_max_temp()
        month = datetime.strptime(info[0].rstrip(), '%Y-%m-%d').month
        if (month == num_month):
            list.append(int(actual_max_temp_object))
    month_sum=sum(list)
    #print(month_sum)
    avg=month_sum/len(list)
    #print(avg)
    averages.append(avg)
    return averages
avgmonth(1, jan_list, averages)
avgmonth(2, feb_list, averages)
avgmonth(3, mar_list, averages)
avgmonth(4, apr_list, averages)
avgmonth(5, may_list, averages)
avgmonth(6, jun_list, averages)
avgmonth(7, jul_list, averages)
avgmonth(8, aug_list, averages)
avgmonth(9, sep_list, averages)
avgmonth(10, oct_list, averages)
avgmonth(11, nov_list, averages)
avgmonth(12, dec_list, averages)
num=averages.index(max(averages))
monthDict={0:'January', 1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11:'December'}
for key, value in monthDict.items():
    if num==key:
        print("2. " + value + " has the highest actual Max Temperature on Average.")

# Q3
jan_list, feb_list, mar_list, apr_list, may_list, jun_list, jul_list, aug_list, sep_list, oct_list, nov_list, dec_list, average_temp = [], [], [], [], [], [], [], [], [], [], [], [], []
def highestDiff(num_Month, list, average_temp):
    with open("weather_data.csv") as myFile:
        lines = myFile.readlines()
    for line in lines[1:]:
        info = line.split(",")
        date = info[0].rstrip()
        actual_min_temp = info[2].rstrip
        actual_max_temp = info[3].rstrip
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        actual_max_temp_object = actual_max_temp()
        actual_min_temp_object = actual_min_temp()
        month = datetime.strptime(info[0].rstrip(), '%Y-%m-%d').month
        if (month == num_Month):
            diff=float(actual_max_temp_object)-float(actual_min_temp_object)
            list.append(int(diff))
    month_Sum = sum(list)
    #print(month_Sum)
    avg_month = month_Sum / len(list)
    #print(avg_month)
    average_temp.append(avg_month)
    return average_temp

highestDiff(1, jan_list, average_temp)
highestDiff(2, feb_list, average_temp)
highestDiff(3, mar_list, average_temp)
highestDiff(4, apr_list, average_temp)
highestDiff(5, may_list, average_temp)
highestDiff(6, jun_list, average_temp)
highestDiff(7, jul_list, average_temp)
highestDiff(8, aug_list, average_temp)
highestDiff(9, sep_list, average_temp)
highestDiff(10, oct_list, average_temp)
highestDiff(11, nov_list, average_temp)
highestDiff(12, dec_list, average_temp)
number = average_temp.index(max(average_temp))
monthDict = {0: 'January', 1: 'February', 2: 'March', 3: 'April', 4: 'May', 5: 'June', 6: 'July', 7: 'August', 8: 'September', 9: 'October', 10: 'November', 11: 'December'}
for key, value in monthDict.items():
    if number == key:
        print("3. " + value + " on average had the highest difference between the actual low and actual high temperature.")

#Q4
jan_list, feb_list, mar_list, apr_list, may_list, jun_list, jul_list, aug_list, sep_list, oct_list, nov_list, dec_list, rainMonths = [], [], [], [], [], [], [], [], [], [], [], [], []
def rainiestMonth(Num_Month, list, rainMonths):
    with open("weather_data.csv") as myFile:
        lines = myFile.readlines()
    for line in lines[1:]:
        info = line.split(",")
        date = info[0].rstrip()
        average_precipitation = info[11].rstrip
        datetime_object = datetime.strptime(date, '%Y-%m-%d')
        average_precipitation_object = average_precipitation()
        month = datetime.strptime(info[0].rstrip(), '%Y-%m-%d').month
        if (month == Num_Month):
            list.append(float(average_precipitation_object))
        rain_sum = sum(list)
        rainMonths.append(rain_sum)
        return rainMonths

rainiestMonth(1, jan_list, rainMonths)
rainiestMonth(2, feb_list, rainMonths)
rainiestMonth(3, mar_list, rainMonths)
rainiestMonth(4, apr_list, rainMonths)
rainiestMonth(5, may_list, rainMonths)
rainiestMonth(6, jun_list, rainMonths)
rainiestMonth(7, jul_list, rainMonths)
rainiestMonth(8, aug_list, rainMonths)
rainiestMonth(9, sep_list, rainMonths)
rainiestMonth(10, oct_list, rainMonths)
rainiestMonth(11, nov_list, rainMonths)
rainiestMonth(12, dec_list, rainMonths)
monthNum=rainMonths.index(max(rainMonths))
for key, value in monthDict.items():
    if monthNum==key:
        print("4. " + value + " is the rainest month on average.")

#Q5
daysBelow=[]
daysAbove=[]
total_sum_list=[]
with open('weather_data.csv') as myfile:
    count = sum(1 for line in myfile)
with open("weather_data.csv") as myFile:
    lines = myFile.readlines()
for line in lines[1:]:
    info = line.split(",")
    date = info[0].rstrip()
    average_precipitation = info[11].rstrip
    datetime_object = datetime.strptime(date, '%Y-%m-%d')
    average_precipitation_object = average_precipitation()
    total_sum_list.append(float(average_precipitation_object))
    total_sum = sum(total_sum_list)
    average = total_sum / (count - 1)  # minus header line
    if (float(average_precipitation_object) > float(average)):
        daysAbove.append(float(average_precipitation_object))
    else:
        daysBelow.append(float(average))
if len(daysAbove) > len(daysBelow):
    print ("5. More days are above average precipitation.")
else:
    print ("5. More days are below average precipitation.")

#Q6
minTemps=[]
maxTemps=[]
with open('weather_data.csv') as myfile:
    count = sum(1 for line in myfile)
with open("weather_data.csv") as myFile:
    lines = myFile.readlines()
for line in lines[1:]:
    info = line.split(",")
    date = info[0].rstrip()
    actual_min_temp = info[2].rstrip
    actual_max_temp = info[3].rstrip
    average_min_temp = info[4].rstrip
    average_max_temp = info[5].rstrip
    datetime_object = datetime.strptime(date, '%Y-%m-%d')
    actual_min_temp_object = actual_min_temp()
    actual_max_temp_object = actual_max_temp()
    average_min_temp_object = average_min_temp()
    average_max_temp_object = average_max_temp()
    if (actual_max_temp_object>average_max_temp_object):
        maxTemps.append(int(actual_max_temp_object))
    if (actual_min_temp_object<average_min_temp_object):
        minTemps.append(int(actual_min_temp_object))
if (len(maxTemps)>len(minTemps)):
    print ("6. Washington DC is getting warmer on average.")
else:
    print ("6. Washington DC is getting colder on average.")
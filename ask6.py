import datetime

yy = input("Type the year (1-9999):")
mm = input("Type the month's number (1-12):")

DayCnt = 1
date = datetime.date(yy, mm, 1)
rows = [[" "]*7 for _ in range(6)]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if (date.weekday() >= 0 and date.weekday() <= 5):
    for i in range(1+date.weekday(),7):
        rows[0][i] = DayCnt
        DayCnt = DayCnt + 1
else:
    for i in range(7):
        rows[0][i] = DayCnt
        DayCnt = DayCnt + 1

if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm ==8 or mm == 10 or mm == 12):
    for j in range(1,6):
        i = 0
        while (i <= 6 and DayCnt <= 31):
            rows[j][i] = DayCnt
            DayCnt = DayCnt + 1
            i = i + 1
            if (DayCnt == 32 and i<7):
                for k in range(i,7):
                    rows[j][k] = "  "
elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
    for j in range(1,6):
        i = 0
        while (i <= 6 and DayCnt <= 30):
            rows[j][i] = DayCnt
            DayCnt = DayCnt + 1
            i = i + 1
            if (DayCnt == 31 and i<7):
                for k in range(i,7):
                    rows[j][k] = "  "
elif ((yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0)):
    for j in range(1,5):
        i = 0
        while (i <= 6 and DayCnt <= 29):
            rows[j][i] = DayCnt
            DayCnt = DayCnt + 1
            i = i + 1
            if (DayCnt == 30 and i<7):
                for k in range(i,7):
                    rows[j][k] = "  "
else:
    for j in range(1,5):
        i = 0
        while (i <= 6 and DayCnt <= 28):
            rows[j][i] = DayCnt
            DayCnt = DayCnt + 1
            i = i + 1
            if (DayCnt == 29 and i<7):
                for k in range(i,7):
                    rows[j][k] = "  "
                    
print months[mm - 1], yy
print "S | M | T | W | T | F | S"
print ' | '.join(map(str, rows[0]))
print ' | '.join(map(str, rows[1]))
print '| '.join(map(str, rows[2]))
print '| '.join(map(str, rows[3]))
print '| '.join(map(str, rows[4]))
if (rows[5][0] != " "):
    print '| '.join(map(str, rows[5]))

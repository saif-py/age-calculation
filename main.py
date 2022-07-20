from datetime import date

while True:
    try:
        a = input('enter your dob(dd/mm/yyyy)')
        a = a.split('/')
        Bdate = int(a[0])
        Bmonth = int(a[1])
        Byear = int(a[2])

        b = date.today()
        b = str(b)
        b = b.split('-')
        Tdate: int = int(b[2])
        Tmonth = int(b[1])
        Tyear: int = int(b[0])


        def numberOfDays(y, m):
            leap = 0
            if y % 400 == 0:
                leap = 1
            elif y % 100 == 0:
                leap = 0
            elif y % 4 == 0:
                leap = 1
            if m == 2:
                return 28 + leap
            list = [1, 3, 5, 7, 8, 10, 12, 0]
            if m in list:
                return 31
            return 30


        if Bmonth > Tmonth:
            years = Tyear - Byear - 1
            if Bdate > Tdate:
                months = 12 - Bmonth + Tmonth - 1
                days = numberOfDays(Tyear, Tmonth - 1) - Bdate + Tdate
            else:
                months = 12 - Bmonth + Tmonth
                days = Tdate - Bdate

        elif Tmonth > Bmonth:
            years = Tyear - Byear
            if Bdate > Tdate:
                months = Tmonth - Bmonth - 1
                days = numberOfDays(Tyear, Tmonth) - Bdate + Tdate
            else:
                months = Tmonth - Bmonth
                days = Tdate - Bdate
        else:
            if Bdate > Tdate:
                years = Tyear - Byear - 1
                months = 11
                days = numberOfDays(Tyear, Tmonth) - Bdate + Tdate
            else:
                years = Tyear - Byear
                months = 0
                days = Tdate - Bdate
        print(f'you are {years} years {months} months and {days} days old')
    except:
        print("done")
        break
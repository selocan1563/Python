# Python program to Find day of 
# the week for a given date 
import calendar
import datetime


def findDay(date):    #Günün tarihini alır
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()  # günün yazdırır.
    return (calendar.day_name[born]) #döngüye tekrar sokar .


# Driver program 
date = '03 02 2019'
print(findDay(date))

import schedule
import time
import PyQt5
import datetime
import csv


class Task:
    def __init__(self):
        pass

    def store(NAME):
        date=datetime.datetime.now()
        Cat=input("Wich category? ").lower()
        #Use the file to refer to the file object
        with open("Tasks.csv", mode='a') as file: 
            data_writer=csv.writer(file,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow([NAME, Cat, str(date.strftime("%d/%m/%Y %H:00")) , "0"])

    def read():
        with open("Tasks.csv") as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                print(row)



#Task.store(input("Input the new task: "))
Task.read()


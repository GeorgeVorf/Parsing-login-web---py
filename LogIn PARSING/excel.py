import xlsxwriter
from main import base

def writer(parametr):
    book = xlsxwriter.Workbook(r"/Users/egormacpro/Desktop/LogIn PARSING/data.xlsx")
    page = book.add_worksheet("famous_people")

    row = 0
    column = 0

    page.set_column("A:A", 100)
    page.set_column("B:B", 10)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])

        row += 1

    book.close()

writer(base)
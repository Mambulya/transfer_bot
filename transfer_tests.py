import transfer_bot_oop as tr
import xlrd
from xlutils.copy import copy

excel_file = xlrd.open_workbook("./test_data.xlsx") # load an excel  file
sheet = excel_file.sheet_by_index(0)
row_number = sheet.nrows

file_write = copy(excel_file)
w_sheet = file_write.get_sheet(0)


#for 2 table
for row in range(1, row_number):
    base = float(str(sheet.row(row)[6]).replace("number:", "").replace("text:", "").replace("'", ""))
    number = str(sheet.row(row)[7]).replace("text:", "").replace("'", "").replace("number:", "")
    answer = str(sheet.row(row)[8])
    final_base = float(str(sheet.row(row)[9]).replace("number:", "").replace("text:", "").replace("'", ""))

    number0 = tr.Transfer_bot(number, final_base, base)
    myResult = str(number0.transform_other_sys())

    if (answer in myResult) or (myResult in answer):
        w_sheet.write(row, 11, '+') # calculations are right?   --->   write "+"
    else:
        w_sheet.write(row, 11, myResult) # calculations are not right? --->  look at the result
        
    file_write.save("results1.xls") # save the check inan excel file


# for 1 table ( numbers of decimal notation initially )
for row in range(12, 13):
    base = 10
    number = str(sheet.row(row)[0]).replace("text:", "").replace("'", "").replace("number:", "")
    answer = str(sheet.row(row)[1])

    final_base = float(str(sheet.row(row)[2]).replace("number:", "").replace("text:", "").replace("'", "").replace("empty:", "0"))

    number0 = tr.Transfer_bot(number, final_base, base)
    myResult = str(number0.from_decimal())

    if (answer in myResult) or (myResult in answer):
        w_sheet.write(row, 3, '+') 
    else:
        w_sheet.write(row, 3, myResult)
        
    file_write.save("results1.xls") # save the check in an excel file

""" create an instance to check a definite instance """
number = tr.Transfer_bot("6", "7", '16')  # number, final_base, base
print(number.transform_other_sys())


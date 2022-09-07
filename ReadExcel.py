import xlrd

loc = ("C:\\Users\\ibrah\\Downloads\\ReadingExcel.xls")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

print(sheet.cell_value(0, 0))
print(sheet.nrows)
print(sheet.ncols)
print(sheet.row_values(1))

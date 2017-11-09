import xlrd

#implement a excel file
file = "mnistdata.xlsx"

#open excel file
data = xlrd.open_workbook(file)

#check the sheets
sheetNames = data.sheet_names()

#two approaches to get excle sheet
sh = data.sheet_by_index(0)
sh = data.sheet_by_name(u'sheet1')

#get row counts
nrows = sh.nrows
print ("row counts = %d" % nrows)

#get colum counts
ncols = sh.ncols
print ("col counts = %d" % ncols)

#get all contents of row or col
rows = sh.row_values(3)
cols = sh.col_values(1)
print ("content of row four: %s" % rows)
#print ("content of col two: %s" % cols)

#get value of cell
cellA1 = sh.cell(0,0)
print ("content at cell A1: %s" % cellA1)



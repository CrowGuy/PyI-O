import xlwt

#create a excel
file = xlwt.Workbook()

#create a sheet and assign name
sheet1 = file.add_sheet(u'sheet1',cell_overwrite_ok=True)
row0 = [u'row1',u'row2']

#write
for i in range(0,len(row0)):
  sheet1.write(0,i,row0[i])

for i in range(5):
  sheet1.write(i+1,0,"2")
  sheet1.write(i+1,1,"3")

#save file
file.save('test.xlsx')

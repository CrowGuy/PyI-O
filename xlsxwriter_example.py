import xlsxwriter

#Create an new excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet('sheet2')

#Widen the first column to make the text clearer
worksheet.set_column('A:A', 20)

#Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})

#Write some simple text.
worksheet.write('A1', 'Hello')

#Text with formatting
worksheet.write('A2', 'world', bold)

#write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

workbook.close()

import os
import xlsxwriter
import xlrd
class pyIO:
    def __init__(self, fileName, path=''):
        self.fileName = fileName   # the operate file name
        self.path = path           # the path of file

    def writeTxt(self, data, delimiter, header=None):
        file = open(str(self.path) + str(self.fileName), "w")
        if header:
            for field in header:
                file.write(field + "\n")
        for row in data:
            for cell in row:
                file.write(str(cell) + str(delimiter))
            file.write("\n")
        file.close()
    
    def writeExcel(self, sheet, data, header=None):
        """docstring for fname"""
        workbook = xlsxwriter.Workbook(str(self.path) + str(self.fileName))
        worksheet = workbook.add_worksheet(sheet)
        if header:
            for index, field in enumerate(header):
                worksheet.write(0, index, field)
        for rowind, row in enumerate(data):
            for cellind, cell in enumerate(row):
                worksheet.write(rowind + 1, cellind, cell)
        workbook.close()
        
    def readTxt(self, delimiter=None):
        data = []
        with open(str(self.path) + str(self.fileName)) as file:
            if delimiter:
                rows = file.read().split("\n")
                if '' in rows:
                    rows.remove('')
                for row in rows:
                    item = row.split(delimiter)
                    if '' in item:
                        item.remove('')
                    data.append(item)
            else:
                data.append(file.readline())
        file.close()
        return data
    
    def renameFile(self, newName, newPath=''):
        os.rename(str(self.path) + str(self.fileName), str(newPath) + str(newName))
    
    def removeFile(self):
        os.remove(str(self.path) + str(self.fileName))
    
if __name__ == '__main__':
    #statistic = [[1,50],[2,100],[2,300]]
    file1 = pyIO("mnistdata.txt")
    #file1.writeTxt(statistic,",")
    data = file1.readTxt( ",")
    file2 = pyIO("mnistdata.xlsx")
    file2.writeExcel("sheet1",data)
    """
    file2 = pyIO("exltest.xlsx")
    file2.writeExcel("sheet1", statistic, ["A","B"])
    """


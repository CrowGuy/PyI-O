
"""This is an class function for python file read/write. 
   @author: CowGuy
"""
import os
import xlsxwriter
import xlrd

class fileRW:
    """ Summary of this class
    This class provide Write and Read function for txt, xls, xlsx files.

    Attributes:
        fileNme: The name of the file
        path: The location of the file
    """
    def __init__(self, fileName, path=''):
        """Initial pyClass."""
        self.fileName = fileName   # the operate file name
        self.path = path           # the path of file

    def writeTxt(self, data, delimiter, header=None):
        """Write data to text file. 
        Args:
            data: The content you want to write.
            delimiter: A string format, the delimiter txt file between 
                       strings, which is split symbol.
            header: The field name of data statistics. 
        """
        if self.path:
            if not os.path.isdir(self.path):
                os.makedirs(self.path)
                
        with open(str(self.path) + str(self.fileName), "w") as file:
            if header:
                for field in header:
                    file.write(field + "\n")
            for row in data:
                file.write(str(delimiter).join(map(str, row)))
                """
                for i, cell in enumerate(row):
                    if i == len(row) - 1:
                        file.write(str(cell))
                    else:
                        file.write(str(cell) + str(delimiter))"""
                file.write("\n")
        file.close()
    
    def writeExcel(self, sheet, data, header=None):
        """Write data to excel file.
        Args:
            sheet: A string format, the nameof sheet.
            data: A list format, the content you want to write.
            header: The field name of data statistics.
        """
        if self.path: 
            if not os.path.isdir(self.path):
                os.makedirs(self.path)

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
        """Read content of txt file, and insert to list.
        Args:
            delimiter: A string format, the delimiter txt file between 
                       strings, which is split symbol.

        Return:
            A list which contains all row and col in txt file.
            For example:
            [['Field 1','Field 2', 'Field 3'], [1, 2 , 3]]
        """
        data = []
        with open(str(self.path) + str(self.fileName)) as file:
            if delimiter:
                rows = file.read().splitlines()
                for row in rows:
                    item = row.split(delimiter)
                    if '' in item:
                        item.remove('')
                    data.append(item)
            else:
                data.append(file.readline())
        file.close()
        return data
    
    def readExcel(self, sheet_ind):
        """Read data in excel into list.
        Args:
            sheet_ind: The index of sheet.
        
        Return:
            A list which contains all row and col in excel file.
            For example:
            [['Field 1','Field 2', 'Field 3'], [1, 2 , 3]]
        """
        data = []
        with xlrd.open_workbook(str(self.path) + str(self.fileName)) as workbook:
            worksheet = workbook.sheet_by_index(sheet_ind)
            for nrow in range(worksheet.nrows):
                data.append(worksheet.row_values(nrow))
        workbook.release_resources()
        return data

    def renameFile(self, newName, newPath=''):
        os.rename(str(self.path) + str(self.fileName), str(newPath) + str(newName))
    
    def removeFile(self):
        os.remove(str(self.path) + str(self.fileName))
    
if __name__ == '__main__':
    """The example to test functions"""
    
    # Initialize the testing data list 
    statistic = [[1,50],[2,100],[2,300]]

    # The example of writting and reading for txt file.
    file1 = fileRW("mnistdata.txt","./test/")
    file1.writeTxt(statistic,",")
    data = file1.readTxt( ",")
    
    # The example of writting and reading for xlsx file.
    #file2 = fileRW("mnistdata.xlsx")
    #file2.writeExcel("sheet1",data)
    #data = file2.readExcel(0)


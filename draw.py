import openpyxl as xl
wb = xl.load_workbook("py_project.xlsx")
sheet = wb["Sheet1"]
cell = sheet["a1"]
#cell= sheet.cell(1,1)
print(cell.value)

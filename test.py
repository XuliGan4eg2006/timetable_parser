import openpyxl
from config import *

dataframe = openpyxl.load_workbook("lmao.xlsx")
dataframe1 = dataframe.active
for group_let in group_map:
    if group_let in dataframe1[group_map[group_let] + "" + str(y_offset)].value:
        pass
    else:
        print(group_let + " - bad")

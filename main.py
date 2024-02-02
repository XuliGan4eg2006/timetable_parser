import openpyxl
from config import *

dataframe = openpyxl.load_workbook("book.xlsx")
dataframe1 = dataframe.active


def get_groups():
    groups = []
    # getting all cell values in whole line 6
    for cell in dataframe1[y_offset]:
        if cell.value is not None and cell.value not in filter_words:
            groups.append(cell.value)
    return groups


def get_group_lessons():
    classes = {}
    groups = get_groups()
    selected_group = None
    skip_one = False

    day_counter = 0
    classes_counter = 0

    for row in dataframe1["E6":"E43"]:
        for cell in row:
            if skip_one:
                skip_one = False
                continue

            if cell.value in groups:
                print("Creating group json: " + cell.value)
                classes[cell.value] = {}
                selected_group = cell.value
                skip_one = True
            else:
                if classes_counter == 6:
                    classes_counter = 0
                    day_counter += 1
                    print("============NEW DAY - " + str(day_counter) + "============")

                if classes_counter == 0:
                    print("value: " + str(cell.value))
                    print("creating classes arry: " + selected_group + " day_counter " + str(day_counter))
                    classes[selected_group][day_counter] = []

                    class_to_write = str(cell.value).replace("None", "Нет урока")

                    replace_class = dataframe1.cell(row=cell.row, column=cell.column + 1).value
                    class_room_number = str(dataframe1.cell(row=cell.row, column=cell.column + 2).value).replace(".0",
                                                                                                                 "")

                    if replace_class is not None:
                        class_to_write += " | " + str(replace_class)

                    classes[selected_group][day_counter].append(class_to_write + " ~ " + class_room_number)
                else:
                    print("adding class: " + str(cell.value).replace("None", "Нет урока"))
                    class_to_write = str(cell.value).replace("None", "Нет урока")

                    replace_class = dataframe1.cell(row=cell.row, column=cell.column + 1).value
                    class_room_number = str(dataframe1.cell(row=cell.row, column=cell.column + 2).value).replace(".0",
                                                                                                                 "")

                    if replace_class is not None:
                        print(replace_class)
                        class_to_write += " | " + str(replace_class)

                    classes[selected_group][day_counter].append(class_to_write + " ~ " + class_room_number)

                classes_counter += 1

    print(classes)

get_group_lessons()
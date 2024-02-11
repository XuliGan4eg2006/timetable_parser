import json

import openpyxl
import uvicorn

from config import *
from fastapi import FastAPI

dataframe = openpyxl.load_workbook("lol.xlsx")
dataframe1 = dataframe.active

app = FastAPI()

breaks = ["Перемена 10 минут", "Перемена 30 минут", "Перемена 30 минут", "Перемена 10 минут", "Перемена 10 минут",
          "Конец пар"]


@app.get("/")
def read_root():
    return {"Hello": "World"}


def get_groups():
    groups = []
    # getting all cell values in whole line 6
    for cell in dataframe1[y_offset]:
        if cell.value is not None and cell.value not in filter_words:
            groups.append(cell.value)
    return groups


@app.get("/breaks")
def get_breaks():
    return {"breaks": breaks}


@app.get("/groups")
def return_groups():
    groups = get_groups()
    return {"groups": groups}


@app.get("/lmao/{group}")
def get_lessons(group: str):
    classes = {"scheduleItems": []}
    groups = get_groups()
    selected_group = None
    skip_one = False

    day_counter = 0
    classes_counter = 0
    classes_arr = []

    for row in dataframe1[group_map[group] + "6": group_map[group] + "43"]:
        for cell in row:
            if skip_one:
                skip_one = False
                continue

            if cell.value in groups:
                print("Got group name: " + cell.value)
                skip_one = True
            else:
                if classes_counter == 6:

                    classes["scheduleItems"].append({"day_num": day_counter, "classes": classes_arr})
                    classes_arr = []
                    classes_counter = 0
                    day_counter += 1
                    print("============NEW DAY - " + str(day_counter) + "============")
                else:
                    class_to_write = str(cell.value).replace("None", "Нет урока")

                    replace_class = dataframe1.cell(row=cell.row, column=cell.column + 1).value
                    class_room_number = str(dataframe1.cell(row=cell.row, column=cell.column + 2).value).replace(
                        ".0",
                        "")

                    if replace_class is not None:
                        class_to_write += " | " + str(replace_class)

                    if "НО" in class_room_number:
                        rings_time = time_map_NO[classes_counter]
                    else:
                        rings_time = time_map[classes_counter]

                    classes_arr.append(class_to_write + " # " + rings_time)

                classes_counter += 1

    print(classes)
    # for lesson in classes:
    #     classes[lesson] = [val for pair in zip(classes[lesson], breaks) for val in pair]

    return classes


@app.get("/timetable/{group}")
def get_group_lessons(group: str):
    classes = {}
    groups = get_groups()
    selected_group = None
    skip_one = False

    day_counter = 0
    classes_counter = 0
    try:
        for row in dataframe1[group_map[group] + "6": group_map[group] + "43"]:
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
                        class_room_number = str(dataframe1.cell(row=cell.row, column=cell.column + 2).value).replace(
                            ".0",
                            "")

                        if replace_class is not None:
                            class_to_write += " | " + str(replace_class)

                        classes[selected_group][day_counter].append(class_to_write + " ~ " + class_room_number)
                    else:
                        print("adding class: " + str(cell.value).replace("None", "Нет урока"))
                        class_to_write = str(cell.value).replace("None", "Нет урока")

                        replace_class = dataframe1.cell(row=cell.row, column=cell.column + 1).value
                        class_room_number = str(dataframe1.cell(row=cell.row, column=cell.column + 2).value).replace(
                            ".0",
                            "")

                        if replace_class is not None:
                            print(replace_class)
                            class_to_write += " | " + str(replace_class)

                        classes[selected_group][day_counter].append(class_to_write + " ~ " + class_room_number)

                    classes_counter += 1
    except:
        classes[group] = {
            "0": ["Server Error", "Server Error", "Server Error", "Server Error", "Server Error", "Server Error"],
            "1": ["Server Error", "Server Error", "Server Error", "Server Error", "Server Error", "Server Error"],
            "2": ["Server Error", "Server Error", "Server Error", "Server Error", "Server Error", "Server Error"],
            "3": ["Server Error", "Server Error", "Server Error", "Server Error", "Server Error", "Server Error"],
            "4": ["Server Error", "Server Error", "Server Error", "Server Error", "Server Error", "Server Error"],
            "5": ["Server Error", "Server Error", "Server Error", "Server Error", "Server Error", "Server Error"]}

    return classes


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

import json
import os
import ijson 
import csv

#json_file_path = 'E:\\Fast Api Alembic\\employees_10-level_1-GB_formatted.json'
json_file = 'E:\Fast Api Alembic\employees_10-level_1-GB_formatted.json'

json_file_path = os.path.join(os.getcwd(),'employees_10-level_1-GB_formatted.json')

MAKE_DIR = os.makedirs("CSV",exist_ok=True)
csv_file_path = os.path.join("CSV", "emp_data.csv")
file_exists = os.path.exists(csv_file_path)

BUFFER_SIZE = 50
with open(json_file_path,'r',encoding='utf-8') as f:
    # parser = ijson.parse(f)
    # count = 0
    # for prefix, event, value in parser:
    #     print(prefix, event, value)
    #     count +=1
    #     if count==10:
    #         break

    emp = ijson.items(f,"employees.item")

    # chunk =[]
        # for e in list(emp):
    #     chunk.append(e)

    #     # if len(chunk)==BUFFER_SIZE:
    #     for chun in chunk:
    #         with open(csv_file_path, "a", newline="", encoding="utf-8") as csv_file:
    #             fieldnames = chun.keys()
    #             print(fieldnames)
    #             writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    #             if not file_exists:
    #                 writer.writeheader()

    #             writer.writerow(chun)   
    #             chunk.pop(-1)
    count=0
        # single_data_process = iter(emp)
        # iter_data = next(single_data_process)
    
    
    with open(csv_file_path, "a", newline="", encoding="utf-8") as csv_file:
        writer = None
        while True:
            try:
                iter_data = next(emp)
                fieldnames = iter_data.keys()
                print(fieldnames)
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                if not file_exists:
                    writer.writeheader()

                writer.writerow(iter_data)   
                count+=1

            except StopIteration:
                break


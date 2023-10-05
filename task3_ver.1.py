# Задача № 3

import os


def combine_files():
    """Объединяет три файла в один по правилам"""

    files_path = os.getcwd() + "/sorted/"
    file1_path = os.path.join(files_path, "1.txt")
    file2_path = os.path.join(files_path, "2.txt")
    file3_path = os.path.join(files_path, "3.txt")

    file1_name = os.path.basename(file1_path)
    file2_name = os.path.basename(file2_path)
    file3_name = os.path.basename(file3_path)

    with open(file1_path, encoding="utf-8") as f1:
        lines_1 = f1.readlines()
    with open(file2_path, encoding="utf-8") as f2:
        lines_2 = f2.readlines()
    with open(file3_path, encoding="utf-8") as f3:
        lines_3 = f3.readlines()

    file_lines_count_dict = {
        "Кол-во строк в file1": len(lines_1),
        "Кол-во строк в file2": len(lines_2),
        "Кол-во строк в file3": len(lines_3),
    }
    print(file_lines_count_dict)

    file_write_order_lst = [
        len(lines_1),
        len(lines_2),
        len(lines_3),
    ]
    file_write_order_lst.sort()

    with open("result_task3.txt", "w", encoding="utf-8") as f:
        f.write(f"{file2_name}\n")
        f.write(f"{len(lines_2)}\n")
        f.write(f"{lines_2}".strip())
        f.write(f"\n{file1_name}\n")
        f.write(f"{len(lines_1)}\n")
        f.write(f"{lines_1}".strip())
        f.write(f"\n{file3_name}\n")
        f.write(f"{len(lines_3)}\n")
        f.write(f"{lines_3}".strip())


print(combine_files())

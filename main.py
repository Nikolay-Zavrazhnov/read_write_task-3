def txt_file_sorter():
    import glob

    total_list = []
    new_list = sorted(total_list, key=len)
    for file_text in glob.glob("*.txt"):
        if file_text != 'new_file.txt':
            def file_worker(file_name: str, mode: str = 'r'):
                list_lines = []
                with open(file_name, 'r', encoding='utf-8') as file:
                    list_lines.append(file.readlines())
                    list_lines[0].insert(0, f"{file_text}\n{len(list_lines[0])}\n")

                total_list.append(list_lines[0])

            file_worker(file_text)

    for list_of_string in sorted(total_list, key=len):
        for lines in list_of_string:
            print(lines.strip())
            with open('new_file.txt', 'a', encoding='utf-8') as nfile:
                nfile.write(f"{lines.strip()}\n")
    print(sorted(total_list, key=len))
txt_file_sorter()


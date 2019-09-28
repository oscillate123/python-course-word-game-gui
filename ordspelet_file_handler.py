def file_reader(read_file, encoding):
    # reads file, returns list, and removes line breakers if there are such
    with open(read_file, "r", encoding=encoding) as file:
        reader = file.readlines()
        data = list(reader)
        data = [item.replace("\n", "") for item in data]
        return data

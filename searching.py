import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    #file_path = os.path.join(cwd_path, file_name)
    with open(file_name) as data_file:
        data = json.load(data_file)
        #print(data)
    if field in data.keys():
        return data[field]
    else:
        return None



data = read_data("sequential.json", "unordered_numbers")
print(data)


def linear_search(numbers, searched_number):
    """
    """
    positions = []
    count = 0
    for position, number in enumerate(numbers):
        if number == searched_number:
            positions.append(position)
            count += 1
    result = dict()
    result["positions"] = positions
    result["count"] = len(positions)
    return result


print(linear_search(data, 2))


def main():
    pass


if __name__ == '__main__':
    main()
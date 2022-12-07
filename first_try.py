import json
import sys
import argparse
from datetime import date, datetime

path_a = sys.argv[1]
path_b = sys.argv[2]
path_result = sys.argv[3]

parser = argparse.ArgumentParser()

parser.add_argument('path_a', type=str, help='Enter the path to the first file (log_a)')
parser.add_argument('path_b', type=str, help='Enter the path to the second file (log_b)')
parser.add_argument('-o', '--path_result', type=str, help='Enter the path where you want to create a new file',
                    required=True)

args = parser.parse_args()

a = []
b = []
result = []


def get_result(path_a: str, path_b: str, path_result: str):
    print('Gluing files together..')
    with open(path_a, 'r') as file_a, open(path_b, 'r') as file_b:

        for line in file_a:
            line_a = json.loads(line)
            a.append(line_a)
            print(a)
        for line in file_b:
            line_b = json.loads(line)
            b.append(line_b)

    for i in a:
        datetime_a = datetime.strptime(i['timestamp'], '%Y-%m-%d %H:%M:%S')
        for j in b:
            datetime_b = datetime.strptime(j['timestamp'], '%Y-%m-%d %H:%M:%S')
            if i not in result and j not in result:
                if datetime_a < datetime_b:
                    result.append(i)
                else:
                    result.append(j)

    print(len(a))
    print(len(b))

    if len(a) == len(b):
        if a[-1]['timestamp'] > b[-1]['timestamp']:
            result.append(a[-1])
        else:
            result.append(b[-1])

    elif len(a) < len(b):
        for i in b[len(a) - len(b) - 1:]:
            if i not in result:
                result.append(i)
    else:
        for i in a[len(b) - len(a) - 1:]:
            if i not in result:
                result.append(i)

    # print('++++')
    # for i in result:
    #     print(i)
    #
    with open(path_result, 'w') as file:
        for line in result:
            file.write(str(line) + '\n')

    print('Done!')


get_result(args.path_a, args.path_b, args.path_result)

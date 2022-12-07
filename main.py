import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument('path_a', type=str, help='Enter the path to the first file (log_a)')
parser.add_argument('path_b', type=str, help='Enter the path to the second file (log_b)')
parser.add_argument('-o', '--path_result', type=str, help='Enter the path where you want to create a new file',
                    required=True)

args = parser.parse_args()


def get_result(path_a: str, path_b: str, path_result: str):
    print('Gluing files together..')

    with open(path_a, 'r') as file_a, \
            open(path_b, 'r') as file_b, \
            open(path_result, 'w') as file_result:

        line_from_log_a = file_a.readline()
        line_from_log_b = file_b.readline()

        while True:
            if not line_from_log_a:
                while line_from_log_b:
                    file_result.write(line_from_log_b)
                    line_from_log_b = file_b.readline()

            if not line_from_log_b:
                while line_from_log_a:
                    file_result.write(line_from_log_a)
                    line_from_log_a = file_a.readline()

            if line_from_log_a and line_from_log_b:
                convert_to_dict_line_a = json.loads(line_from_log_a)
                convert_to_dict_line_b = json.loads(line_from_log_b)
                datetime_a = datetime.strptime(convert_to_dict_line_a['timestamp'], '%Y-%m-%d %H:%M:%S')
                datetime_b = datetime.strptime(convert_to_dict_line_b['timestamp'], '%Y-%m-%d %H:%M:%S')

                if datetime_a < datetime_b:
                    file_result.write(line_from_log_a)
                    line_from_log_a = file_a.readline()
                else:
                    file_result.write(line_from_log_b)
                    line_from_log_b = file_b.readline()

            if not line_from_log_a and not line_from_log_b:
                print('Done')
                break


get_result(args.path_a, args.path_b, args.path_result)

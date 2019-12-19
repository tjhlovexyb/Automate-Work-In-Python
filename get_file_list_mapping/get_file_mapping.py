import json
import os
import re

model_and_cube_list = []
acl_list = []
auto_model_list = []
datasource_list = []
diag_list = []
query_list = []
oam_list = []

# init a dict for wanted tags
# of cause, there are samples down.
total_dict = {
    'model_and_cube': {},
    'acl': {},
    'auto_model': {},
    'data_source': {},
    'diag': {},
    'query': {},
    'oam': {}
}

# data_dir for original wanted_mapping, such as test_0001 in test_0001_0010,
# the test_0001 is original wanted_mapping,
# and test_0001_0010 is the target mapped file
# in this path, the original mapped list file exists. NOTO: It's a file, not files.

# need to change
data_dir = '/data/of/original_wanted_mapping_list'

root_path = '/target/files/path'


# get the target mapped file list
# you should input the path of target mapped file list
def get_files_list(file_path):
    for child in os.listdir(file_path):
        child_path = os.path.join(file_path, child)
        if os.path.isdir(child_path):
            get_files_list(child_path)
        else:
            clear_path = child_path.split('/')[-1].split('.')[0]
            if 'model_and_cube' in clear_path:
                model_and_cube_list.append(clear_path)
            elif 'acl' in clear_path:
                acl_list.append(clear_path)
            elif 'auto_model' in clear_path:
                auto_model_list.append(clear_path)
            elif 'data_source' in clear_path:
                datasource_list.append(clear_path)
            elif 'diag' in clear_path:
                diag_list.append(clear_path)
            elif 'query' in clear_path:
                query_list.append(clear_path)
            elif 'oam' in clear_path or 'operation' in clear_path:
                oam_list.append(clear_path)


# full the dict, after step get files list
def set_dict():
    total_dict['model_and_cube'].update(anlysic_cases(model_and_cube_list))
    total_dict['diag'].update(anlysic_cases(diag_list))
    total_dict['data_source'].update(anlysic_cases(datasource_list))
    total_dict['query'].update(anlysic_cases(query_list))
    total_dict['acl'].update(anlysic_cases(acl_list))
    total_dict['auto_model'].update(anlysic_cases(auto_model_list))
    total_dict['oam'].update(anlysic_cases(oam_list))


# you can also use this fuction to show the current target file list
def print_file_list():
    print("=========system operation===========")
    print(oam_list)
    print("=========model and cube===========")
    print(model_and_cube_list)
    print("=========query===========")
    print(query_list)
    print("=========diag===========")
    print(diag_list)
    print("=========datasource===========")
    print(datasource_list)
    print("=========auto model===========")
    print(auto_model_list)
    print("=========acl===========")
    print(acl_list)


# from targets to extract cases num!
def anlysic_cases(cases):
    temp_dict = {}
    num_list = []
    for case in cases:
        num_str = re.findall(r'\d+', case)
        num_list.append(num_str)
        temp_dict[case] = full_hole(num_list)
    return temp_dict


# full the hole of case numbers, such as ['0010','0012','0008'] will extract to ['0010','0011','0008']
def full_hole(number):
    for num in number:
        total_list = []
        if len(num) == 1:
            total_list.append(map(int, num))
            continue
        num_lis = list(map(int, num))
        temp_list = num_lis
        for i in num_lis[1:]:
            if i - num_lis[num_lis.index(i) - 1] > 1:
                for j in range(num_lis[num_lis.index(i) - 1] + 1, i):
                    temp_list.insert(num_lis.index(i), j)
        total_list.append(temp_list)
    total_list = [index for key in total_list for index in key]
    return total_list


# write to mapped file
def map_file_step(test_type, mapped_file, file_ls, mapped_type):
    with open(os.path.join(data_dir, test_type, mapped_file), 'w+') as map_34, \
            open(os.path.join(data_dir, test_type, file_ls), 'r') as file_list:
        file_list = json.load(file_list)
        # print(file_list)
        file_case_num = list(map(int, sum([re.findall(r'\d+', file) for file in file_list], [])))

        for file in file_case_num:
            str_s = ''
            for key, value in total_dict[mapped_type].items():
                if file in value:
                    str_s = f"{file_list[file_case_num.index(file)]}      ->      {key}"
                    print(str_s)

            if str_s:
                map_34.write(str_s + '\n')
            else:
                map_34.write(f"{file_list[file_case_num.index(file)]}      <->\n")


def main():
    # step 1: get file and list
    get_files_list(root_path)
    # step 2: set dict
    set_dict()
    # step 3: write mapped relationship to files
    map_file_step(test_type='system_operation', mapped_file='map_oam_34', file_ls='oam_34', mapped_type='oam')
    map_file_step('model_and_cube', 'map_model_and_cube_34', 'model_and_cube_34', 'model_and_cube')
    map_file_step(test_type='acl', mapped_file='map_acl_34', file_ls='acl_34', mapped_type='acl')
    map_file_step(test_type='auto_model', mapped_file='map_auto_model_34', file_ls='auto_model_34', mapped_type='auto_model')
    map_file_step(test_type='diag', mapped_file='map_diag_34', file_ls='diag_34', mapped_type='diag')
    map_file_step(test_type='query', mapped_file='map_query_34', file_ls='query_34', mapped_type='query')
    map_file_step(test_type='datasource', mapped_file='map_datasource_34', file_ls='datasource_34', mapped_type='data_source')


if __name__ == '__main__':
    main()

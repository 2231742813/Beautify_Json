import json


# json中字段路径查找
def find_all_field_paths_and_values(json_data, field_name, path=None, paths=None):
    if path is None:
        path = []
    if paths is None:
        paths = []

    if isinstance(json_data, dict):
        for key, value in json_data.items():
            if key == field_name:
                paths.append((path + [key], value))  # 将字段的路径和对应的值添加到列表中
            if isinstance(value, (dict, list)):
                find_all_field_paths_and_values(value, field_name, path + [key], paths)  # 递归调用
    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            find_all_field_paths_and_values(item, field_name, path + [str(index)], paths)  # 递归调用

    return paths  # 返回所有字段的路径和对应的值列表
# def find_all_field_paths_and_values(json_data, field_name, path=None, paths=None):
#     if path is None:
#         path = []
#     if paths is None:
#         paths = []
#     if isinstance(json_data, dict):
#         for key, value in json_data.items():
#             if key == field_name:
#                 paths.append((path + [key], value))  # 将字段的路径和对应的值添加到列表中
#             if isinstance(value, (dict, list)):
#                 find_all_field_paths_and_values(value, field_name, path + [key], paths)  # 递归调用
#     elif isinstance(json_data, list):
#         for index, item in enumerate(json_data):
#             find_all_field_paths_and_values(item, field_name, path + [str(index)], paths)  # 递归调用
#     return paths  # 返回所有字段的路径和对应的值列表



# if __name == "__main__":
#     dats = '{"emailType":"alarm","screens":[{"deviceInfo":{"id":"0ae374b1-01f5-4454-af04-fcdc8241e777","name":"screen-1","type":65280,"typeName":"SCREEN_FULL_COLOR","model":"screen","addr":"FullColorScreen","secondBrightnessEnable":false},"sendBoxs":[{"deviceInfo":{"id":"8df8d14e-008a-4670-a284-41aa92fa3bd7","name":"V3US02_GD","type":81,"typeName":"V3US02_GD","model":"sendBox","addr":"192.168.209.2"},"addr":"192.168.209.2","alarms":[],"scanBoards":[{"deviceInfo":{"id":"3156df73-78fd-42e6-b6f2-41b66789f457","name":"ScanBoard_19","type":120,"typeName":"V3CG11","model":"scanBoard","addr":"192.168.144.1"},"addr":"192.168.144.1","alarms":[{"type":"Communicate Error","level":"warning","startTimeMS":1702348465501,"upCount":199,"curStatus":0,"reported":true}]},{"deviceInfo":{"id":"ca84d43b-7405-4da6-9ea6-02c6a178bb06","name":"ScanBoard_22","type":120,"typeName":"V3CG11","model":"scanBoard","addr":"192.168.144.4"},"addr":"192.168.144.4","alarms":[{"type":"Communicate Error","level":"warning","startTimeMS":1702348465501,"upCount":199,"curStatus":0,"reported":true}]}]}]}]}'
#     # 示例的json数据
#     json_str = '{"name": "John", "age": 30, "address": {"city": "New York", "zip": "10001", "zip2": "20002"}}'
#     json_data = json.loads(dats)
#     # 在json数据中查找字段"zip"的位置，并打印字段的值
#     all_paths = find_all_field_paths_and_values(json_data, "id")
#     # print(all_paths)  # 在函数外打印所有字段的路径
#     for i in all_paths :
#         url, values = i
#         print(url)
#         print(values)


import json



def beautify_json_function(datas):
    try:
        json_obj = json.loads(datas)
        # 使用json.dumps函数美化JSON数据并返回
        pretty_json = json.dumps(json_obj, indent=4, ensure_ascii=False)
        # print(pretty_json)
        return pretty_json
    except json.JSONDecodeError:
        return 0


# if __name__ == '__main__':
#     beautify_json_function(datas = {"filename" : "v3pro-123-20231211140813-initial setup.zip", "md5" : "8c19463f443c752027f8efbbdfb1550f",
#             "sha1" : "8cd77b1e26d0fc97786dd88631a2d41d0f88e293",
#             "sha256" : "b5f80f46c092e680391f152a44d72f947b54baca2482ccdc3933593fb0ca514e",
#             "sha512" : "c59a7ea03fcb783a04e42e271053a196b568e5532551c91ea9dd839b9b600b87ae0f97c3e0c9539070d234e34d10278750e1a8594b43408cce98c7dc041d6eb2"})
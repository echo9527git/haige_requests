import json


def create_data(start,end):
    # send_data = [(str(random.randint(0,9999999)),
    #          "zhangsan",
    #          str(random.randint(13888880000, 13888889999))) for x in range(0,10)]

    data = [("aaa125bbb" + str(x), "zhansan", "138%08d" % x) for x in range(start, end)]
    print(data)
    return data

def print_json(j):
    print(json.dumps(j, indent=2, ensure_ascii=False))





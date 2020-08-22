from ruamel import yaml

def dump_yaml(yaml_name,data:dict):
    """
    将字典格式数据写入到yaml文件
    :param yaml_name:将被创建的yaml文件名
    :param data:字典格式数据
    :return:没有返回值
    """
    # 创建env.yaml文件，给可写权限，将env中数据写入env.yaml
    with open(yaml_name,"w") as f:
        yaml.safe_dump(data=data,stream=f)

def load_yaml(yaml_file):
    """
    从yaml文件中读取数据
    :param yaml_file:yaml文件名
    :return:字典格式数据
    """
    return yaml.safe_load(open(yaml_file))

if __name__ == '__main__':
    env = {
        "default": "test",
        "testing-studio":
            {
                "dev": "https://ceshiren.com",
                "test": "https://baidu.com"
            }
    }

    data1 = {
        "method": "get",
        "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        "params": {
            'corpid': "ww3c6b51ae743ae4ec",
            'corpsecret': "xvmyVvTMnJaR0q2eitVBAOqJA-vQKt6zPjpQXixT8do"
        },
        "json": None
    }
    dump_yaml("get_token.yaml",data1)
    # y = load_yaml("get_token.yaml")
    # print(y)
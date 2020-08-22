from ruamel import yaml
from requests_demo_framwork.env_demo import API

class TestEnv:
    def test1(self):
        data = {
            "method": 'get',
            "url":"url",
            "headers": None
        }
        env = yaml.safe_load(open("env.yaml"))
        # 替换
        # default: test
        # testing - stutio: {dev: https: // ceshiren.com, test: https: // baidu.com}
        data['url'] = str(data['url']).replace("url", env["testing-studio"][env['default']])
        res = API.send_env(data)
        print(res.text)

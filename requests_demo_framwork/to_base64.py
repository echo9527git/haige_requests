import base64
import json

bytes_url = {"topics":
    {
        "orange":"movie",
        "school":"testing-studio",
        "president":"seveniruby"
    }
}
data = json.dumps(bytes_url, indent=2)
str_url = base64.b64encode(data.encode("utf-8"))  # 被编码的参数必须是二进制数据
print(str_url)



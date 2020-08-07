def request(flow):
    flow.request.headers["myheader"] = "value"

"""Send a reply from the proxy without sending any send_data to the remote server."""
from mitmproxy import http

# def request(flow: http.HTTPFlow) -> None:
#     if flow.request.pretty_url == "http://www.baidu.com/":
#         flow.response = http.HTTPResponse.make(
#             200,  # (optional) status code
#             b"Hello World12345",  # (optional) content
#             {"Content-Type": "text/html"}  # (optional) headers
#         )

def request(flow: http.HTTPFlow) -> None:
    if "get_token=abcdef" in flow.request.pretty_url:
        with open("C:/Users/Administrator/Desktop/map1.json",encoding="UTF-8") as f:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),
                {"Content-Type": "text/html"}  # (optional) headers
            )
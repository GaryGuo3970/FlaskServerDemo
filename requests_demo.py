import requests
from bs4 import  BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0"

def general_get(url,useragent=USER_AGENT):
    response = requests.get(
        url=url,
        headers={
            "user-agent": useragent
        },
        cookies={
            "_xsrf": "xWSiR94IL2gi4idmnqIiZXDfUwbdaU9P"
        }
    )
    return response

def process_html(html,id,tag="div"):
    if html is None:
        return None

    if isinstance(html,(str,bytes)):
        soup = BeautifulSoup(html,features="html.parser")
    else:
        soup = html

    if(id):
        parted_ares = soup.find(
            name=tag,
            attrs={
                "id": id
            }
        )
    else:
        parted_ares = soup.find_all(
            name=tag
        )
    return parted_ares

# url = "https://www.zhihu.com/api/v4/comment_v5/articles/25049221110/root_comment?order_by=score&limit=20&offset="
#
# response = general_get(url)
# print(response.json())
#
# url = "https://api.luffycity.com/api/v1/course/free/"
# response = general_get(url)
# print(response.json())

url = "https://www.autohome.com.cn/news"
response = general_get(url)
response.encoding = "GB2312"
parted_ares = process_html(response.text,"auto-channel-lazyload-article")
#print(parted_ares)
li_list = process_html(parted_ares,"","li")
for li_node in li_list:
    h3_node_list = process_html(li_node,"","h3")
    for h3_node in h3_node_list:
        print(h3_node.text)
import configparser
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE_PATH = os.path.join(BASE_DIR,'my.ini')

config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH,encoding="utf-8")

#获取所有节点
print(os.path.exists(CONFIG_FILE_PATH))  # 必须返回 True
nodes = config.sections()

#获取节点下键值
node_list= []
for node in nodes:
    node_list.append(node)

#添加节点到文件
# config.add_section("newNode")
# config.set("newNode","new1","newvalue1")
# config.set("newNode","new2","newvalue2")
# with open(CONFIG_FILE_PATH,mode="w",encoding="utf-8") as f:
#     config.write(f)

#读取节点到一个字典中
result = {}
for node in nodes:
    result[node]= {}

print(result)

#读取节点，读取键值，新增节点，新增键值，删除节点，删除键值等都可以
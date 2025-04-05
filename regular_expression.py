import  re

#验证
email = input("输入您的邮箱：")

is_valiad = re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email)
if is_valiad:
    print("合法")
else:
    print("不合法")

#查找
text  = "ad1s111fsdfll@123123 s15688882222,dtest@test.com.ddfdf,dtadfa"
result = re.findall(r"s\d+",text)
print(result)

#默认贪婪匹配：符合要求的最长字符串
result = re.findall(r"a.+1",text)
print(result)

#使用?不要贪婪匹配
result = re.findall(r"a.+?1",text)
print(result)
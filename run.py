#启动文件
from common import function
from test_data import  test_data

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
url=test_data.url["url"]
username=test_data.login_data[0]["username"]
password=test_data.login_data[1]["password"]
s_key=test_data.s_key["s_key"]
print(url)
print(username)
print(password)
print(s_key)
num=function.search_key(driver=driver,url=url,username=username,password=password,s_key=s_key)
if s_key in num:
    print("查询结果是正确的！")
else:
    print("测试用例不通过！")




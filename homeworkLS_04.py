# -*-coding:utf-8 -*-
# @Time: 2020/7/21 15:30
# @Author:lemon_su
# @Email:854001151@qq.com
# @File: homeworkLS_04.py
# @Software: PyCharm

# 完成上节课的作业讲解
[[11,12,13,14,15,16,17,18],
 [21,22,23,24,25,26,27,28],
 [31,32,33,34,35,36,37,38],
 [41,42,43,44,45,46,47,48]]
# 按行读取
# openpyxl 第三方
# from openpyxl import load_workbook
#
# wb = load_workbook('new_big_file.xlsx')
# sheet = wb['test_case']
# # 读取第一行数据
# # 获取所有行的数据
# all_case = []
# for i in range(sheet.max_row): # 4
#     case = [] # 存每一行的数据
#     for j in range(sheet.max_column): # 8 这一行代码和下面一行代码是指定完成指定行的所有数据的读取
#         case.append(sheet.cell(row=i+1,column=j+1).value)
#         # print(sheet.cell(row=i+1,column=j+1).value)
#     all_case.append(case)
# print(all_case)

# 讲解HTTP请求的作业
# 讲解测试用例的设计
import requests # 调用requests库

def http_request(url,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2','Authorization': token}
    if method == 'get':
        result = requests.get(url,json=data,headers=header)
    else:
        result = requests.post(url,json=data,headers=header)
    return result.json() # return返回指定的结果

if __name__ == '__main__':
    # 调用函数
    # # 注册
    # reg_url = "http://120.78.128.25:8766/futureloan/member/register"
    # reg_data = {'mobile_phone':15526425540,'pwd':'12345678901'}
    # print(http_request(reg_url,reg_data,header))

    # 登录
    log_url = "http://120.78.128.25:8766/futureloan/member/login"
    log_data = {'mobile_phone':15526425540,'pwd':'12345678901'}
    response = http_request(log_url,log_data) # 用变量response接收

    # 充值
    token = response['data']['token_info']['token']
    # print(token)
    rec_url = "http://120.78.128.25:8766/futureloan/member/recharge"
    rec_data = {'member_id':2047545,'amount':50000}

    print(http_request(rec_url,rec_data,"Bearer "+ token))

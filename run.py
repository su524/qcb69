# -*-coding:utf-8 -*-
# @Time: 2020/7/21 17:55
# @Author:lemon_su
# @Email:854001151@qq.com
# @File: run.py
# @Software: PyCharm
# from lemon_69.R_W_EXCEL import  read_data
# from lemon_69.homeworkLS_04 import http_request
# # 执行文件
# # 获取到所有的测试数据
# all_case = read_data('lemon_69.xlsx','test_case')
# print('获取到的所有测试数据是：',all_case)
#
# # 执行测试 -- 先执行第一条
# print("第一条用例的数据：",all_case[0])
# test_data = all_case[0]
#
# expected = eval(test_data[6]) # 期望值
#
# ip = "http://120.78.128.25:8766"
# response = http_request(ip+test_data[4],eval(test_data[5]),token=None,method=test_data[3])
# print("最后的结果值：",response)

# 代码优化
from R_W_EXCEL import  read_data
from homeworkLS_04 import http_request
# from openpyxl import load_workbook
from R_W_EXCEL import write_data
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")

# 全局变量   局部变量
# 函数内的变量---局部变量    函数外的变量---全局变量
# 执行文件
# 获取到所有的测试数据
Token = None # 全局变量，初始值设置为None

def run(file_name,sheet_name,c1,c2):
    global Token # 在这里声明 函数外的Token和函数内的Token是同一个值
    all_case = read_data(file_name,sheet_name)
    print('获取到的所有测试数据是：',all_case)
    for test_data in all_case: # 在http_request进行请求的时候，判断是否是登录请求
        # test_data = all_case[i]
        # if test_data[0]==1: # 他就是一个登录的用例
        # if test_data[1]=='登录': 判断两边是否相等 比较运算符
        ip = "http://120.78.128.25:8766"
        response = http_request(ip + test_data[4], eval(test_data[5]), token=Token, method=test_data[3])
        if 'login' in test_data[4]: # 成员运算符

            Token ="Bearer "+ response['data']['token_info']['token']
        print("最后的结果值：", response)

        # # 1.开始写入结果
        # wb = load_workbook('lemon_69.xlsx')
        # sheet = wb['test_case']
        # # 定位单元格存值  行  列  值
        # sheet.cell(row=test_data[0]+1,column=8).value=str(response)

        # 2.开始写入结果
        write_data(file_name,sheet_name,test_data[0]+1,c1,str(response))

        # 进行判断，期望值与实际值是否相等，判断这个用例是否执行通过
        actual = {'code':response['code'],'msg':response['msg']}
        if eval(test_data[6])==actual:
            print('测试用例执行通过')
            write_data(file_name,sheet_name,test_data[0]+1,c2,'PASS')
        else:
            print('测试用例执行不通过')
            write_data(file_name,sheet_name,test_data[0]+1,c2,'FAIL')

        # # 保存
        # wb.save('lemon_69.xlsx')

# 调用函数
run('lemon_69.xlsx','test_case',8,9) # 执行的充值的接口


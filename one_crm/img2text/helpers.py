# -*- encoding: utf-8 -*-
"""
@File    :   helpers
@Time    :   2020/7/12 8:33 下午
@Author  :   Fan Lingjie
@Version :   1.0
@Contact :   fanlingjie@laiye.com
"""

import re

import jieba.posseg as pseg


def isname(single_word_string):
    """
        判断是否是人名
    """
    pair_word_list = pseg.lcut(single_word_string)
    for _, cixing in pair_word_list:
        if cixing == "nr":
            return True
    return False


def extract_name(s):
    """
        提取人名
    """
    name = "未知"
    data = s.split("\n")
    for i in data:
        i = i.replace(" ", "")
        if isname(i):
            name = i
            break
    return name


def extract_email(s):
    emails = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", s)
    if emails:
        return emails[0]
    else:
        return ""


def extract_phone(s):
    numbers = re.findall("(1\\d{2}-?\\d{4}-?\\d{4})", s)
    if numbers:
        return numbers[0]
    else:
        return ""


if __name__ == "__main__":
    # print(extract_phone("138-1678-8989"))
    print(
        extract_name(
            """
        张 叁

    专 业 打 杂

    电 话 :
    邮 箱 :
    官 网 :
    地 址 :

    什 么 都 不 干 网 络 科 技 有 限 公 司

    139-8888-6666
    example@qq.com

    www.example.cn

    上 海 市 长 宁 区 中 山 公 园 龙 之 梦 氮 空 间 18 楼
    """
        )
    )

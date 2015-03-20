# -*- coding: utf-8 -*-
"""
注明：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
注意：由于中文乱码问题，输出时请先decode("utf8")，例如你要输出ans = "零圆", print ans.decode("utf8").
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示
"""
import re

NUM = {'0': '零', '1': '壹', '2': '贰', '3': '叁', '4': '肆',
       '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'}
shi = '拾'
bai = '佰'
qian = '仟'
wan = '万'


def trans(num):
    """将整数转化成RMB大写格式, 范围为：1-9999 9999 9999"""
    num_str = str(num).lstrip('0')
    ptn = re.compile(r'^0*\d{1,12}$')
    if not ptn.match(num_str):
        raise ValueError('invalid input num.')

    part1 = part2 = part3 = ''
    last_four = num_str[-4:]
    part1 = zip_zero(''.join(reversed([k+v for k, v in zip(reversed(last_four), ['圆', shi, bai, qian])])))
    if len(num_str) > 4:
        mid_four = num_str[:-4]
        part2 = zip_zero(''.join(reversed([k+v for k, v in zip(reversed(mid_four), ['万', shi, bai, qian])])))
    if len(num_str) > 8:
        first_four = num_str[:-8]
        part3 = zip_zero(''.join(reversed([k+v for k, v in zip(reversed(first_four), ['亿', shi, bai, qian])])))

    result = part3+part2+part1

    return num_to_chn(result)


def zip_zero(num_str):
    """将每4位中多余的零去掉"""
    result = ''
    for i in range(0, len(num_str), 2):
        print(result)
        if num_str[i] == '0':
            if i == len(num_str)-2:
                result += num_str[-1]
            else:
                if i != len(num_str)-2 and num_str[i+2] == '0':
                    continue
                else:
                    result += '零'
        else:
            result += num_str[i:i+2]

    return result


def num_to_chn(num):
    result = ''
    for i in str(num):
        result += NUM.get(i, i)
    return result


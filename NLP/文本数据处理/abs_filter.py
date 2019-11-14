import re
import xlrd

bra = ['【', '（', '{', '[']  # 左括号
ket = ['】', '）', '}', ']']  # 右括号，必须和左括号匹配
list0 = ['本文约', '预计阅读时间', '文']
list1 = ['消息', '讯', '通报', '转载', '报道', '日电']
list2 = ['', ' ', '：', '，']
list3 = [' ', '：', '，']
words = [i + j for i in list1 for j in list2]  # 包含空字符，用于匹配句尾
words2 = [i + j for i in list1 for j in list3]  # 不包含空字符，用于查找句子中的关键词


def drop(string):
    if string == '':
        return ''
    for i in range(len(bra)):
        if string[0] == bra[i]:
            if string[-1] == ket[i]:
                return ''
            else:
                output = re.split(ket[i], string, 1)  # 只匹配第一个右括号，返回括号后面的句子
                return output[-1]
    # 判断是否以 "本文约" 等语句开头
    for word in list0:
        if re.match(word, string):
            return ''
    #  判断是否以 "报道：" 等语句结尾
    for word in words:
        if re.match(word[::-1], string[::-1]):
            output = re.split(word, string)
            return ''  # output[-1]
    # 判断句子中是否有关键词，如果有，返回这个词后面的句子部分
    for word in words2:
        if word in string:
            output = re.split(word, string)
            return output[-1]
    # 没有找到关键词，返回原字符串
    return string


def abs_filter(document):
    """
    :param document:读入一篇文章
    返回过滤后的文章
    """
    # output = []
    output = ''
    sentences = re.split('[。？?！!\n]', document)
    for sentence in sentences:
        # output.append(drop(sentence))
        output += drop(sentence)
    return output


if __name__ == '__main__':
    excel = xlrd.open_workbook('摘要关键字.xlsx')
    sheet = excel.sheet_by_index(0)
    lists = sheet.col_values(1)
    print(lists)
    for item in lists:
        result = abs_filter(item)
        print(result)


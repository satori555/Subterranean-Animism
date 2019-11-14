# encoding:utf8
"""
过滤敏感词
"""


# 去掉匹配的括号
def drop(string):
    if len(string) <= 6:
        return string
    out = ''
    tag1, tag2 = '%%%(((', '%%%)))'
    flag = 0  # 判断括号是否嵌套
    i = 0
    while i < len(string) - 6:
        if string[i:i + 6] != tag1 and string[i:i + 6] != tag2:
            out += string[i]
            i += 1
        elif string[i:i + 6] == tag1:  # 发现左括号
            flag += 1
            if flag == 1:
                out += string[i:i + 3]
            i += 6
        elif string[i:i + 6] == tag2:  # 发现右括号
            flag -= 1
            if flag == 0:
                out += string[i:i + 3]
            i += 6
    out += string[-6:]
    return out


# 返回加上敏感词标记的文本
def check(src, max_length, senti_list):
    dict_senti = dict.fromkeys(senti_list, 0)  # 建立哈希表
    for i in range(max_length, 0, -1):
        if max_length > len(src):
            continue
        start = 0
        s = ''
        for _ in range(len(src) - i + 1):
            word = src[start:start + i]
            # print(word)
            if word in dict_senti:
                if start == 0 or i == 1:
                    s += '%%%(((' + word + '%%%)))'
                else:
                    s = s[:-(i - 1)] + '%%%(((' + word + '%%%)))'
            else:
                if start == 0:
                    s += word
                else:
                    s += word[i - 1:]
            start = start + 1
        src = s
    src = drop(src)
    return src


def senti_filter(src_content, senti_list):
    out_content = ''
    max_length = 0  # 最长的敏感词长度
    for _ in senti_list:
        if len(_) > max_length:
            max_length = len(_)
    pointer = 0
    while pointer < len(src_content):
        if src_content[pointer] == '<':
            out_content += src_content[pointer]
            pointer += 1
            while src_content[pointer] != '>':
                out_content += src_content[pointer]
                pointer += 1
            out_content += src_content[pointer]
            pointer += 1
            if pointer >= len(src_content):
                break
        else:
            temp = ''
            while src_content[pointer] != '<':
                temp += src_content[pointer]
                pointer += 1
                if pointer >= len(src_content):
                    break
            out_content += check(temp, max_length, senti_list)
    return out_content


if __name__ == '__main__':
    data = \
        {'content': '''
        <article> <p>据湖北省黄冈市政府官网消息，11月11日，黄冈市第五届人民代表大会常务委员会第二十四次会议通过：<strong>任命刘忠诚为黄冈市人民政府副市长。</strong></p > <p><strong>17年前，29岁的刘忠诚被明确为副处级，1年后，30岁的他成为正处级干部。</strong></p > <div class="pgc-img"> < img class="image" src="https://rmrbcmsonline.peopleapp.com/rb_recsys/img/2019/1112/1c91f41ade10c0bc712a8f24ff6a2bd8_378673551701438464.jpeg" width="640" height="519" thumb_width="120" thumb_height="97"/> <p class="pgc-img-caption">资料图</p > </div> <p><strong>29岁的刘忠诚被明确为副县级干部</strong>，并于同年调任瞿家湾镇党<span style="background:#FFC100;">委书记</span>。<strong>明确副县级仅一年后，2003年，时任30岁的刘忠诚任荆州市大沙湖农场管理区党<span style="background:#FFC100;">委书记</span>（正县级）。</strong><strong>2014年，刘忠诚调任<span style="background:#FFC100;">公安</span>县县长。</strong>在当年召开的领导干部大会上，时任荆州市委组织部常务副<span style="background:#FFC100;">部长</span>田新华介绍了刘忠诚的工作经历。他说，<strong>刘忠诚同志经验丰富，阅历较深，能吃苦，有担当，工作中注意创新，能发挥和团结一班人的作用，对自己严格要求，能自觉遵守廉洁从政各项规定。</strong><strong>2016年，刘忠诚调任石首市<span style="background:#FFC100;">委书记</span>，主政石首三年半。</strong><strong>刘忠诚说，石首走传统的发展模式已不可行，绿色发展代表了新的发展方向，是我们作为后发地区进行赶超的历史机遇。</strong>传统工业化道路带来了不可持续的环境和社会代价，这在中部传统农区表现尤为突出。特别是随着中国经济发展步入新常态，经济增速由高速增长转向中高速增长，以石首为典型的欠发达中部传统农区面临的挑战进一步凸显。如果不尽快找到新的发展出路，有可能陷入所谓的“中等收入陷阱”。<strong>“绝不容许长江生态环境在我们这一代人手上继续恶化下去，一定要给子孙后代留下一条清洁美丽的万里长江!”</strong><strong>现在我们党员干部习惯当“管理型干部”，不会当“发展型干部”</strong>，在抓招商引资等经济工作中暴露出能力不足、方向不清、“本领恐慌”等问题。市委专门组织招商引资培训，就是要开阔党员干部的视野，提升党员干部抓经济工作的能力。</p > <p>据官网信息显示，目前，黄冈市政府领导班子为1正7副，市长为邱丽新，市委<span style="background:#FFC100;">常委</span>、常务副市长为易先荣。<strong>刘忠诚简历</strong></p > </article> <footer/>"
        ''', 'senti_word': ['黄', '政府官网', '黄冈', '市']}
    result = senti_filter(data['content'], data['senti_word'])
    print(data['content'])
    print(result)

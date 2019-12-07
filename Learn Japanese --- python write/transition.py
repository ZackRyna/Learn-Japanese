from pykakasi  import kakasi
# 读取文件，如果不加encoding='utf-8'的话，会报编码错误
read_me = open('as_a_rule.txt','r',encoding='utf-8') # 读
read_to = open('output.txt','w') # 输出

#  //转换器1
bachongying = kakasi()
# 转换成平假名
bachongying.setMode('J','H')
Bachongying = bachongying.getConverter()

#  //转换器2,平假名，片假名转换成罗马音 :
hequanshawu = kakasi()
hequanshawu.setMode('H','a') # 平转罗
hequanshawu.setMode('K','a') # 片转罗
Hequanshawu = hequanshawu.getConverter()


# 转化器已经写好了，接下来就是无脑读。。。
while True:
    s = read_me.readline()
    if s == '':
        break

# number:数字   jp：日语   jph：平和片   jpa：罗马音   cn：中文
    number = jp = jph = jpa = cn = ''
    index = 0
    for char in s:
        if index == 0:
            if char == '、':
                index = 1
            else:
                number += char
        elif index == 1:  # 代表正在读取当前日语
            jp += char
            if char == '。':
                index = 2
        else:
            cn += char
            # print(number,jp,cn)

    jph = Bachongying.do(jp)  # print(jph)    ----- 已经转换成为假名了
    jpa = Hequanshawu.do(jph)  # pring(jpa)

    read_to.writelines(number+'\n')
    read_to.writelines(jp+'\n')
    read_to.writelines(jph+'\n')
    read_to.writelines(jpa[:-1]+'\n')
    read_to.writelines(cn+'\n')
# 跑的时候需要重载一下GBK编码
























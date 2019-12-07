# 如果你想每次输出不排在一起 那me就需要导入OS库
import os
class Sentence:
    def __init__(self,number,jp,jph,jpa,cn):
        # 去掉尾巴和前面空格
        self.number = number.strip()
        self.jp = jp.strip()
        self.jph = jph.strip()
        self.jpa = jpa.strip()
        self.cn = cn.strip()

sentences = []
read_me = open('output.txt','r')

# 无脑读。。。。
while True:
    number = read_me.readline()
    if number == '':
        break
    jp = read_me.readline() # 日语
    jph = read_me.readline() # 平假名 片假名
    jpa = read_me.readline() #  罗马音
    cn = read_me.readline()#  中文
    # 因为尾巴留出了一行，所以让它在多读一行
    _ = read_me.readline()

    new_sentence = Sentence(number,jp,jph,jpa,cn)
    sentences.append(new_sentence)

os.system('clear')
for sentence in sentences:  # 1000句话挨个循环,不答对就不退出，直到答对为止 heihei
    while True:
        print(sentence.jp)
        print(sentence.jph)
        answer = input('Roma: ')
        if answer == sentence.jpa:
            print('Right!')
            _ = input('Good 欧尼酱!~~ Press enter to continue !')
            os.system('clear')
            break
        else:
            print('欧尼酱。。八嘎。。')
            # 提示答案 按 y键
            reveal = input('Press enter to continue,y to reveal the answer')
            if reveal == 'y':
                print(sentence.jpa)
                _ = input('Good 欧尼酱!~~ Press enter to continue !')
            os.system('clear')

















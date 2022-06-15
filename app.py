
import PySimpleGUI as sg
import random
from subject import dict


sg.theme('GreenMono')

layout = [
    [sg.Text("这是HDU中国近代史客观题刷题app", size=(64, 2), font=20, text_color='Black', auto_size_text=True)],
    [sg.Text("由于开发者的技术水平较弱且极为懒惰", size=(64, 2), font=20, text_color='Black')],
    [sg.Text("只能设计出如此简陋敷衍的UI界面", size=(64, 2), font=20, text_color='Black')],
    [sg.Text("相信大家最在乎的不是这个所谓的皮囊而且接下来有趣的灵魂", size=(64, 2), font=20, text_color='Black')],
    [sg.Text("那请选择模式吧", size=(64, 2), font=20, text_color='Black')],
    [sg.Text("                                                 ", size=(64, 1), font=10, text_color='Red')],
    [sg.Button('  顺序模式  ', key="1", font=20), sg.Button('  随机模式  ', key="2", font=20),sg.Button('  错题模式  ', key="3", font=20),sg.Button('  退出程序  ',key='3',font=20)],
    [sg.Text("                                                                                                        By HDU_钟鑫")]]
window = sg.Window('近代史题库', layout, default_element_size=(24, 2), auto_size_text=True)
event, values = window.read()
window.close()
# 模式
if event =='1':
    mode = 'linear'
elif event=='2':
    mode = 'random'
elif event=='3':
    mode = 'mistake'
    mistake_fp = open('source/错题编号.txt','r')
    mistake_list = mistake_fp.readline().split(',')
    with open('source/错题编号.txt','w') as fp:
        fp.write('')
else:
    exit(0)

count = 0
acc = 0
i=-1
mistake_id = -1
while True:
    if mode == 'random':
        i = random.randint(0, 288)
    elif mode=='linear':
        i += 1
        if i > 287:
            break
    elif mode=='mistake':
        mistake_id+=1
        if mistake_id >= len(mistake_list)-1:
            break
        i = eval(mistake_list[mistake_id])

    layout = [
        [sg.Text(dict[i]['tm'], size=(64, 3), font=20, text_color='Black', auto_size_text=True)],
        [sg.Text(dict[i]['xs'], size=(64, 5), font=20, text_color='navy')],
        [sg.Button(' A ', key="A", font=20), sg.Button(' B ', key="B", font=20),sg.Button(' C ', key="C", font=20),sg.Button(' D ', key="D", font=20),],
        [sg.Text("正确率:%d/%d"%(acc,count) , size=(64, 1), font=30, text_color='black')],
        [sg.Button('退出', key="exit", font=20), ],
    ]
    window = sg.Window('近代史题库', layout, default_element_size=(24, 2), auto_size_text=True)
    event, values = window.read()
    window.close()
    if event=='exit':
        break
    answer = dict[i]['an']
    if event!=answer:
        # 记录错题
        with open('错题本.txt', 'a') as wrong_fp:
            wrong_fp.write(dict[i]['tm'] + '\n')
            wrong_fp.write(dict[i]['xs'] + '\n')
            wrong_fp.write('正确答案: %s ' % (answer) + '\n\n')
        with open('source/错题编号.txt','a') as mistake_fp:
            mistake_fp.write('%d'%(i)+',')

        str = '正确答案是: %s '%(answer)
        layout_ = [
            [sg.Text(dict[i]['tm'], size=(64, 2), font=20, text_color='Black', auto_size_text=True)],
            [sg.Text(dict[i]['xs'], size=(64, 5), font=20, text_color='navy')],
            [sg.Text(str , size=(64,2),font=20,text_color='red')],
            [sg.Button('下一题', key="continue", font=20), ],
            [sg.Button('退出', key="exit", font=20), ],
        ]
        window = sg.Window('近代史题库', layout_, default_element_size=(24, 2), auto_size_text=True)
        event, values = window.read()
        window.close()
        if event == 'exit':
            break

    else:
        acc+=1
    count+=1



